# Copyright 2025 Columnar Technologies Inc.
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

cmake_minimum_required(VERSION 3.15)
project(mysql_demo CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Use conda environment paths
if(DEFINED ENV{CONDA_PREFIX})
    list(APPEND CMAKE_PREFIX_PATH "$ENV{CONDA_PREFIX}")
endif()

find_package(Arrow REQUIRED)

add_executable(mysql_demo main.cpp)

if(DEFINED ENV{CONDA_PREFIX})
    target_include_directories(mysql_demo PRIVATE $ENV{CONDA_PREFIX}/include)
    target_link_directories(mysql_demo PRIVATE $ENV{CONDA_PREFIX}/lib)
endif()

target_link_libraries(mysql_demo
    adbc_driver_manager
    Arrow::arrow_shared
)

target_compile_options(mysql_demo PRIVATE
    -Wall
    -Werror
)
