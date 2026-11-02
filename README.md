![The hill before the keeper sets out: the copper gauge close in the foreground with overnight rain beaded on its funnel rim and its level bright in the window, three feet on a wet stone with a puddle reflecting a strip of orange sky, an empty path past a closed instrument shelter, cloud bands stacked above, and a lightning rod alone at the plot corner](intro-banner.png)

# cba-Immutable-Infrastructure-Verifier

![A hill weather station at dawn with the copper gauge in the foreground, a worn path past an instrument shelter with its louvred door ajar and a vane on its roof, a small keeper figure halfway up the path with a measure in hand, and the name cba-immutable-infrastructure-verifier painted in stone white on the panel grey shelter side](banner.png)

![A copper rain gauge in profile on a flat stone, wide funnel rim at the top, green filmed copper, a measuring window with its level about a third of the way up, and one fine rain line falling into the funnel from above the frame, the heading plate](logo.png)

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
