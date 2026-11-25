<!--
Copyright 2026 Columnar Technologies Inc.
SPDX-License-Identifier: Apache-2.0
-->

# AGENTS.md

Guidelines for writing quickstarts in this repo.

- In C++ and Ruby examples, install drivers with `dbc install --level user` so the driver isn't unexpectedly installed into the user's Conda environment.
- Run the database in Docker (not Podman) unless it's a cloud service. Use `docker run -d --rm` (or `docker compose up -d`) and include clean-up steps.
- Apart from the above, keep `docker run` commands close to the vendor's docs (e.g. container names); don't standardize them across examples.
- Run setup steps from the host with `docker exec`; don't make users open a shell inside the container.
- Install drivers with dbc and load them through the driver manager (e.g. `adbc-driver-manager` in Python), not language packages that bundle a driver.
- Ensure that the added examples cover all the languages. If a language can't support it, stop and check with the user that this is expected and prompt them to add a note in the README explaining why.
- Don't edit the root or per-language READMEs by hand. Add the database to `.github/data/databases.json`; the READMEs are generated from it.
- Use the vendor's official product name (e.g. "OceanBase Database"). If you don't know the vendor's official product name, stop and ask the user for it.
- Note known platform issues (e.g. amd64-only images, port conflicts on macOS).
- The examples in this repository are intended to be regularized and templated. Avoid including arbitrary additional examples or details.
- Notice that many for many of the databases covered in these quickstarts, the database does not have a dedicated ADBC driver, but instead uses the driver for another database that it is wire-protocol-compatible with (often PostgreSQL, Flight SQL, or MySQL).
- When adding a set of quickstarts for a new database:
- Identify the most similar database that is already present in the quickstarts, and follow its examples.
- Ensure that all differences between each newly added example and the same-language example for the most similar database are explainable by the fact that they cover two different databases.
- Ensure that there are no inconsistencies between the different-language examples covering this new database that do not match the differences between the different-language examples covering the most similar database.
