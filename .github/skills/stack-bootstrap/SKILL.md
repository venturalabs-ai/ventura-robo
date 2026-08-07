---
name: stack-bootstrap
description: Bootstrap the smallest VenturaRobo structure for the approved simulation-first robotics MVP using declared stack needs. Use when the repository is ready to move from incubation docs to executable simulation code. Do not use when a functional robotics project already exists or the task is direct physical-hardware control.
---

# Stack bootstrap

- Confirm the approved simulation scenario before adding dependencies.
- Add only packages required by the first planning perception or ROS 2 path.
- Separate planning perception interfaces simulation fixtures and tests.
- Keep hardware-specific commands behind explicit adapters and out of initial smoke tests.
- Add one deterministic simulation or algorithm test that can run in CI.
- Document ROS 2 simulator and environment assumptions.
- Reuse the shared repository CI standard.
