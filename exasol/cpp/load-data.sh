#!/usr/bin/env bash
# Copyright 2026 Columnar Technologies Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This script is meant to be run inside the Exasol Docker container.
# The Exasol CLI doesn't have an easy flag to trust a self-signed TLS
# certificate, so extract the fingerprint from the error message.
# Also, wait for Exasol to be available.

EXAPLUS=/opt/exasol/db-2025.1.10/bin/Console/exaplus

while true; do
  HOST=$($EXAPLUS -u sys -p exasol -c localhost:8563 2>&1 | tail -n1 | awk '{print $NF}')
  if [ "$HOST" = "refused" ]; then
    echo Waiting for Exasol...
    sleep 2
    continue
  fi
  echo "Exasol available at $HOST"
  break
done
HOST=${HOST%.}

$EXAPLUS -u sys -p exasol -c "$HOST" -f /tmp/games.sql
