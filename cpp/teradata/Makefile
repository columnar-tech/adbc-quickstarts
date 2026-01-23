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

CXXFLAGS = -std=c++17 -Wall -Werror -I$(CONDA_PREFIX)/include
LIBS = -L$(CONDA_PREFIX)/lib -ladbc_driver_manager -larrow -Wl,-rpath,$(CONDA_PREFIX)/lib

teradata_demo: main.cpp
	$(CXX) $(CXXFLAGS) -o teradata_demo main.cpp $(LIBS)

clean:
	rm -f teradata_demo

.PHONY: clean
