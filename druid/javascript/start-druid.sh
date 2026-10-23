#!/bin/bash
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

set -euo pipefail

readonly config="conf/druid/single-server/nano-quickstart"
pids=()

start() {
  "$@" &
  pids+=("$!")
}

shutdown() {
  trap - EXIT INT TERM
  kill -TERM "${pids[@]}" 2>/dev/null || true
  wait "${pids[@]}" 2>/dev/null || true
}

trap shutdown EXIT INT TERM

start bin/run-zk conf
start bin/run-druid coordinator-overlord "$config"
start bin/run-druid broker "$config"
start bin/run-druid router "$config"
start bin/run-druid historical "$config"
start bin/run-druid middleManager "$config"

set +e
wait -n "${pids[@]}"
status=$?
set -e

# A service exiting normally still means the container is no longer healthy.
if [[ $status -eq 0 ]]; then
  status=1
fi
exit "$status"
