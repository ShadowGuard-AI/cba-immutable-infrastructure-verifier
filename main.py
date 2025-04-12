import argparse
import logging
import os
import sys
import yaml
import json
from jsonschema import validate, ValidationError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
class ExitCodes:
    SUCCESS = 0
    INVALID_INPUT = 1
    CONFIGURATION_ERROR = 2
    VALIDATION_FAILED = 3
    FILE_NOT_FOUND = 4
    DEPENDENCY_ERROR = 5
    PERMISSION_ERROR = 6
    UNEXPECTED_ERROR = 99

# Helper Functions
def load_yaml(file_path):
    """Loads YAML data from a file."""
    try:
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        logging.error(f"YAML file not found: {file_path}")
        raise FileNotFoundError(f"YAML file not found: {file_path}") from None
    except yaml.YAMLError as e:
        logging.error(f"Error parsing YAML file: {file_path} - {e}")
        raise ValueError(f"Error parsing YAML file: {file_path} - {e}") from None
    except OSError as e:
        logging.error(f"OS error reading YAML file: {file_path} - {e}")
        raise OSError(f"OS error reading YAML file: {file_path} - {e}") from None


def load_json(file_path):
    """Loads JSON data from a file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"JSON file not found: {file_path}")
        raise FileNotFoundError(f"JSON file not found: {file_path}") from None
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing JSON file: {file_path} - {e}")
        raise ValueError(f"Error parsing JSON file: {file_path} - {e}") from None
    except OSError as e:
        logging.error(f"OS error reading JSON file: {file_path} - {e}")
        raise OSError(f"OS error reading JSON file: {file_path} - {e}") from None


def verify_file_exists(file_path):
    """Verifies that a file exists."""
    try:
        if not os.path.exists(file_path):
            logging.error(f"File not found: {file_path}")
            return False
        return True
    except OSError as e:
        logging.error(f"OS error checking file existence: {file_path} - {e}")
        return False


def verify_file_content(file_path, expected_content):
    """Verifies that a file's content matches the expected content."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            if content.strip() != expected_content.strip():  # Added strip() to ignore whitespace differences
                logging.error(f"File content mismatch: {file_path}")
                logging.debug(f"Expected: '{expected_content.strip()}', Actual: '{content.strip()}'")
                return False
            return True
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return False
    except OSError as e:
        logging.error(f"OS error reading file: {file_path} - {e}")
        return False


def verify_service_running(service_name):
    """Verifies that a service is running (Linux-specific)."""
    try:
        # Use systemctl to check service status.  Requires systemd.
        result = os.system(f"systemctl is-active --quiet {service_name}")
        if result == 0:
            return True
        else:
            logging.error(f"Service not running: {service_name}")
            return False
    except Exception as e:
        logging.error(f"Error checking service status: {service_name} - {e}")
        return False

def validate_json_against_schema(json_data, schema_data):
    """Validates JSON data against a JSON schema."""
    try:
        validate(instance=json_data, schema=schema_data)
        return True
    except ValidationError as e:
        logging.error(f"JSON validation failed: {e}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error during JSON validation: {e}")
        return False

# Core Functions
def setup_argparse():
    """Sets up the argument parser."""
    parser = argparse.ArgumentParser(description='Immutable Infrastructure Verifier')
    parser.add_argument('--definition', '-d', type=str, required=True,
                        help='Path to the infrastructure definition file (YAML or JSON).')
    parser.add_argument('--type', '-t', type=str, choices=['yaml', 'json'], required=True,
                        help='Type of the infrastructure definition file (yaml or json).')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output for debugging')
    parser.add_argument('--schema', '-s', type=str, help='Path to the JSON schema file for validation (if applicable)')

    return parser.parse_args()


def main():
    """Main function to execute the verifier."""
    args = setup_argparse()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug("Verbose mode enabled.")

    try:
        # Load infrastructure definition
        if args.type == 'yaml':
            definition = load_yaml(args.definition)
        elif args.type == 'json':
            definition = load_json(args.definition)
        else:
            logging.error("Invalid definition type.  Must be 'yaml' or 'json'.")
            sys.exit(ExitCodes.INVALID_INPUT)

        # Optionally validate the definition file against a schema
        if args.schema:
            logging.info(f"Validating definition against schema: {args.schema}")
            schema_data = load_json(args.schema)
            if not validate_json_against_schema(definition, schema_data):
                logging.error("Definition validation failed.")
                sys.exit(ExitCodes.VALIDATION_FAILED)
            logging.info("Definition validated successfully against schema.")


        # Process infrastructure definition
        if 'files' in definition:
            logging.info("Verifying file existence and content...")
            for file_def in definition['files']:
                file_path = file_def['path']
                if not verify_file_exists(file_path):
                    logging.error(f"File missing: {file_path}")
                    sys.exit(ExitCodes.VALIDATION_FAILED)

                if 'content' in file_def:
                    expected_content = file_def['content']
                    if not verify_file_content(file_path, expected_content):
                        logging.error(f"File content mismatch: {file_path}")
                        sys.exit(ExitCodes.VALIDATION_FAILED)
                logging.info(f"File {file_path} verified successfully.")

        if 'services' in definition:
            logging.info("Verifying service status...")
            for service_name in definition['services']:
                if not verify_service_running(service_name):
                    logging.error(f"Service not running: {service_name}")
                    sys.exit(ExitCodes.VALIDATION_FAILED)
                logging.info(f"Service {service_name} verified successfully.")
    except FileNotFoundError:
        sys.exit(ExitCodes.FILE_NOT_FOUND)
    except ValueError:
        sys.exit(ExitCodes.CONFIGURATION_ERROR)
    except PermissionError as e:
        logging.error(f"Permission error: {e}")
        sys.exit(ExitCodes.PERMISSION_ERROR)
    except Exception as e:
        logging.exception("An unexpected error occurred:")
        sys.exit(ExitCodes.UNEXPECTED_ERROR)


    logging.info("Infrastructure verification complete. All checks passed.")
    sys.exit(ExitCodes.SUCCESS)


if __name__ == "__main__":
    main()


# Example Usage (Not part of the executable code, but helpful for understanding how to use it)
# 1.  Create a definition file (e.g., infrastructure.yaml):
#
#     files:
#       - path: /etc/hostname
#         content: my-immutable-host
#       - path: /opt/app/config.json
#         content: '{"setting1": "value1", "setting2": "value2"}'
#
#     services:
#       - ssh
#       - nginx
#
# 2. Run the verifier:
#     python main.py -d infrastructure.yaml -t yaml
#
# 3.  Run the verifier with a schema validation:
#     First, define a schema (e.g., infrastructure_schema.json):
#     {
#       "type": "object",
#       "properties": {
#         "files": {
#           "type": "array",
#           "items": {
#             "type": "object",
#             "properties": {
#               "path": {"type": "string"},
#               "content": {"type": "string"}
#             },
#             "required": ["path"]
#           }
#         },
#         "services": {
#           "type": "array",
#           "items": {"type": "string"}
#         }
#       }
#     }
#     Then run:
#     python main.py -d infrastructure.yaml -t yaml -s infrastructure_schema.json
#
# Offensive Considerations:
#
# The tool itself is primarily defensive.  However, an attacker could target the
# infrastructure definition file or schema file if those are accessible.
# Therefore:
#
# - Protect the definition and schema files with appropriate permissions.
# - Use checksums or other integrity checks on the definition file to ensure it hasn't been tampered with.
# - Consider storing the definition file in a read-only location.
# - Log any changes to the definition file.