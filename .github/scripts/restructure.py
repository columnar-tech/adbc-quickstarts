#!/usr/bin/env python3
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

"""
Restructure the ADBC quickstarts repository from language-first to database-first organization.

Current structure:  <language>/<protocol>/<database>/ or <language>/<database>/
Target structure:   <database>/<language>/
"""

import argparse
import shutil
from pathlib import Path

# Languages in the repository
LANGUAGES = ["python", "go", "java", "cpp", "r", "rust"]

# Protocol directories that contain nested database subdirectories
PROTOCOL_DIRS = {"flightsql", "duckdb", "postgresql", "mysql"}

# Patterns to exclude from copying
EXCLUDE_PATTERNS = {
    "target",  # Rust/Java build output
    "Cargo.lock",  # Rust lockfile
    "go.sum",  # Go lockfile (we'll generate standalone go.mod)
    ".classpath",  # Eclipse IDE
    ".project",  # Eclipse IDE
    ".settings",  # Eclipse IDE
    "__pycache__",  # Python cache
    ".DS_Store",  # macOS
}

# Files to exclude at language root level
LANGUAGE_ROOT_EXCLUDE = {
    "README.md",  # Language-level READMEs
    "Cargo.toml",  # Rust workspace config
    "go.mod",  # Go shared module (replaced with per-example)
    "go.sum",  # Go lockfile
}

# Template for standalone Go modules
GO_MOD_TEMPLATE = """// Copyright 2026 Columnar Technologies Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

module github.com/columnar/adbc-quickstarts/{database}/go

go 1.24.0

require github.com/apache/arrow-adbc/go/adbc v1.8.0
"""


def should_exclude(path: Path) -> bool:
    """Check if a path should be excluded from copying."""
    return path.name in EXCLUDE_PATTERNS


def copy_directory_contents(src: Path, dst: Path) -> None:
    """Copy contents of src directory to dst, excluding specified patterns."""
    dst.mkdir(parents=True, exist_ok=True)

    for item in src.iterdir():
        if should_exclude(item):
            continue

        dst_item = dst / item.name

        if item.is_dir():
            copy_directory_contents(item, dst_item)
        else:
            shutil.copy2(item, dst_item)


def discover_databases(source_root: Path) -> dict[str, dict[str, Path]]:
    """
    Discover all databases and their locations per language.

    Returns:
        Dict mapping database names to dict of {language: source_path}
    """
    databases: dict[str, dict[str, Path]] = {}

    for lang in LANGUAGES:
        lang_dir = source_root / lang
        if not lang_dir.is_dir():
            continue

        for item in lang_dir.iterdir():
            if not item.is_dir() or item.name in LANGUAGE_ROOT_EXCLUDE:
                continue

            if item.name in PROTOCOL_DIRS:
                # This is a protocol directory - look for nested databases
                for db_dir in item.iterdir():
                    if db_dir.is_dir() and not should_exclude(db_dir):
                        db_name = db_dir.name
                        if db_name not in databases:
                            databases[db_name] = {}
                        databases[db_name][lang] = db_dir
            else:
                # This is a direct database directory
                db_name = item.name
                if db_name not in databases:
                    databases[db_name] = {}
                databases[db_name][lang] = item

    return databases


def generate_go_mod(database: str) -> str:
    """Generate a standalone go.mod file for a database example."""
    return GO_MOD_TEMPLATE.format(database=database)


def restructure(source_root: Path, output_root: Path) -> None:
    """
    Restructure the repository from language-first to database-first.

    Args:
        source_root: Path to the source repository root
        output_root: Path to the output directory
    """
    # Clean output directory if it exists
    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True)

    # Copy root-level files
    for root_file in ["LICENSE", "README.md"]:
        src_file = source_root / root_file
        if src_file.exists():
            shutil.copy2(src_file, output_root / root_file)

    # Discover all databases
    databases = discover_databases(source_root)

    print(f"Discovered {len(databases)} databases:")
    for db_name in sorted(databases.keys()):
        langs = ", ".join(sorted(databases[db_name].keys()))
        print(f"  {db_name}: {langs}")

    # Restructure each database
    for db_name, lang_paths in sorted(databases.items()):
        db_output = output_root / db_name

        for lang, src_path in sorted(lang_paths.items()):
            lang_output = db_output / lang
            print(f"  Copying {src_path} -> {lang_output}")
            copy_directory_contents(src_path, lang_output)

            # Generate standalone go.mod for Go examples
            if lang == "go":
                go_mod_path = lang_output / "go.mod"
                go_mod_path.write_text(generate_go_mod(db_name))

    print(f"\nRestructured repository written to: {output_root}")


def main():
    parser = argparse.ArgumentParser(
        description="Restructure ADBC quickstarts from language-first to database-first"
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path.cwd(),
        help="Source repository root (default: current directory)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output directory for restructured repository",
    )

    args = parser.parse_args()

    if not args.source.is_dir():
        parser.error(f"Source directory does not exist: {args.source}")

    restructure(args.source, args.output)


if __name__ == "__main__":
    main()
