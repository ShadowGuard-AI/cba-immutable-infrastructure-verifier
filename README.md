# cba-Immutable-Infrastructure-Verifier

![A foundry floor with rows of black iron castings standing beside their moulds and pine pattern blocks, a worker wearing one orange glove holding the nearest casting against its mould cavity to compare them](banner.png)

![An open sand mould seen straight on with a simple rectangular cavity, a pine pattern block resting beside it on the sand and a single orange glove laid at its lower edge, the heading plate](logo.png)

![Weather plot scene in three layers: cloud bands drift at three speeds across the top, the gauge in the middle stays still while its bright level pulses gently once and rests, and grass stirs in separate patches along the path at the front while a puddle ripples once and goes flat](scene.svg)

Validates that a system's configuration matches its declared immutable infrastructure definition (e.g., defined in Terraform or Ansible). Verifies the presence and integrity of specific files, services, and configurations defined in the infrastructure as code, ensuring that the system hasn't deviated from its intended state and alerting on any inconsistencies. - Focused on Compares system configurations (e.g., application settings, firewall rules expressed in YAML/JSON) against predefined security baselines. Identifies deviations from the approved configuration and reports potential vulnerabilities or misconfigurations. Aims to automate the process of ensuring consistent security hardening across environments.

A definition with no files and no services entries is a configuration error and exits 2, because nothing was checked. A passing run reports how many checks it performed.

> **Shelter notice: no files, no services, exit 2.** A definition with no files and no services entries is a configuration error and exits 2, because nothing was checked.

> **Shelter notice: three posts carry no description.** `--definition`, `--type`, and `--schema` are each listed with no description provided. This document does not guess which file `--definition` points to, what values `--type` takes, or what `--schema` validates against.

![Section divider: three stacked cloud bands, dark over mid over thin lit](sep-heavy.svg)

## Install
`git clone https://github.com/ShadowStrikeHQ/cba-immutable-infrastructure-verifier`

![Section divider: the thin lit cloud band only, short and centred](sep-light.svg)

## Usage
`./cba-immutable-infrastructure-verifier [params]`

![Section divider: three stacked cloud bands, dark over mid over thin lit](sep-heavy.svg)

## Parameters
- `-h`: Show help message and exit
- `--definition`: No description provided
- `--type`: No description provided
- `--verbose`: Enable verbose output for debugging
- `--schema`: No description provided

![Section divider: three stacked cloud bands, dark over mid over thin lit](sep-heavy.svg)

## License
Copyright (c) ShadowStrikeHQ
