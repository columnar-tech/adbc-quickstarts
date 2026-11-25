<!--
Copyright 2026 Columnar Technologies Inc.
SPDX-License-Identifier: Apache-2.0
-->

# AGENTS.md

Guidelines for writing quickstarts in this repo.

- In C++ and Ruby examples, install drivers with `dbc install --level user` so the driver isn't unexpectedly installed into the user's Conda environment.
- Run the database in Docker (not Podman) unless it's a cloud service. Use `docker run -d --rm` (or `docker compose up -d`) and include clean-up steps.
- Keep `docker run` commands close to the vendor's docs (e.g. container names); don't standardize them across examples.
- Run setup steps from the host with `docker exec`; don't make users open a shell inside the container.
- Install drivers with dbc and load them through the driver manager (e.g. `adbc-driver-manager` in Python), not language packages that bundle a driver.
- Add the example for every language. If a language can't support it, stop and check with the user that this is expected and prompt them to add a note in the README explaining why.
- Don't edit the root or per-language READMEs by hand. Add the database to `.github/data/databases.json`; the READMEs are generated from it.
- Use the vendor's official product name (e.g. "OceanBase Database"). If you don't know the vendor's official product name, stop and ask the user for it.
- Note known platform issues (e.g. amd64-only images, port conflicts on macOS).
