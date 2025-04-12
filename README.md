# cba-Immutable-Infrastructure-Verifier
Validates that a system's configuration matches its declared immutable infrastructure definition (e.g., defined in Terraform or Ansible). Verifies the presence and integrity of specific files, services, and configurations defined in the infrastructure as code, ensuring that the system hasn't deviated from its intended state and alerting on any inconsistencies. - Focused on Compares system configurations (e.g., application settings, firewall rules expressed in YAML/JSON) against predefined security baselines. Identifies deviations from the approved configuration and reports potential vulnerabilities or misconfigurations. Aims to automate the process of ensuring consistent security hardening across environments.

## Install
`git clone https://github.com/ShadowStrikeHQ/cba-immutable-infrastructure-verifier`

## Usage
`./cba-immutable-infrastructure-verifier [params]`

## Parameters
- `-h`: Show help message and exit
- `--definition`: No description provided
- `--type`: No description provided
- `--verbose`: Enable verbose output for debugging
- `--schema`: No description provided

## License
Copyright (c) ShadowStrikeHQ
