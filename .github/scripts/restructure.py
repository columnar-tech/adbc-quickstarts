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
import json
import shutil
from pathlib import Path

# Languages in the repository
LANGUAGES = ["python", "go", "java", "cpp", "r", "rust"]

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


def discover_databases(
    source_root: Path, database_info: dict[str, dict]
) -> dict[str, dict[str, Path]]:
    """
    Discover all databases and their locations per language.

    Args:
        source_root: Path to the source repository root
        database_info: Database information from JSON

    Returns:
        Dict mapping database names to dict of {language: source_path}
    """
    # Determine which directories are protocol/parent directories
    # (those with non-null display_name_when_parent)
    protocol_dirs = {
        slug
        for slug, info in database_info.items()
        if info.get("display_name_when_parent") is not None
    }

    databases: dict[str, dict[str, Path]] = {}

    for lang in LANGUAGES:
        lang_dir = source_root / lang
        if not lang_dir.is_dir():
            continue

        for item in lang_dir.iterdir():
            if not item.is_dir() or item.name in LANGUAGE_ROOT_EXCLUDE:
                continue

            if item.name in protocol_dirs:
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


def load_display_names() -> tuple[dict[str, str], dict[str, dict]]:
    """
    Load display name mappings from JSON files.

    Returns:
        Tuple of (language_display_names, database_info)
        where database_info maps slug to {"name": str, "parent": str|None}
    """
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / "data"

    with open(data_dir / "languages.json") as f:
        language_names = json.load(f)

    with open(data_dir / "databases.json") as f:
        database_info = json.load(f)

    return language_names, database_info


def generate_database_readme(
    database: str,
    languages: list[str],
    language_display_names: dict[str, str],
    database_info: dict[str, dict],
) -> str:
    """
    Generate a README.md for a database directory.

    Args:
        database: Database slug (e.g., "duckdb")
        languages: List of language slugs that have examples for this database
        language_display_names: Mapping of language slugs to display names
        database_info: Mapping of database slugs to {"name": str, "parent": str|None}

    Returns:
        README content as a string
    """
    # Load template
    script_dir = Path(__file__).parent
    template_path = script_dir.parent / "data" / "database-readme-template.md"
    template = template_path.read_text()

    # Prepare values
    db_info = database_info.get(database, {})
    db_display_name = db_info.get("name", database.title())
    sorted_languages = sorted(languages)
    language_bullets = "\n".join(
        f"- {language_display_names.get(lang, lang.title())}"
        for lang in sorted_languages
    )

    # Substitute placeholders
    return template.format(
        database_name=db_display_name,
        languages_list=language_bullets,
    )


def generate_go_mod(database: str) -> str:
    """Generate a standalone go.mod file for a database example."""
    return GO_MOD_TEMPLATE.format(database=database)


def generate_by_database_root_readme(
    databases: dict[str, dict[str, Path]],
    language_display_names: dict[str, str],
    database_info: dict[str, dict],
) -> str:
    """
    Generate the root README.md for the by-database branch.

    Args:
        databases: Dict mapping database names to dict of {language: source_path}
        language_display_names: Mapping of language slugs to display names
        database_info: Database information from JSON

    Returns:
        README content as a string
    """
    # Load template
    script_dir = Path(__file__).parent
    template_path = script_dir.parent / "data" / "by-database-root-readme-template.md"
    template = template_path.read_text()

    # Generate languages list
    # Determine which languages are present
    all_languages = set()
    for lang_paths in databases.values():
        all_languages.update(lang_paths.keys())

    languages_list = "\n".join(
        f"- {language_display_names.get(lang, lang.title())}"
        for lang in sorted(all_languages)
    )

    # Generate databases list (only databases in database_info)
    database_slugs = [slug for slug in databases.keys() if slug in database_info]

    # Group databases by parent
    by_parent: dict[str | None, list[str]] = {}
    for slug in database_slugs:
        info = database_info.get(slug, {})
        parent = info.get("parent")
        if parent not in by_parent:
            by_parent[parent] = []
        by_parent[parent].append(slug)

    # Create list of entries with slugs and display names
    entries: list[tuple[str, str, str | None]] = []

    # Add standalone databases (parent is None)
    if None in by_parent:
        for slug in by_parent[None]:
            info = database_info.get(slug, {})
            name = info.get("name", slug.title())
            entries.append((slug, name, None))

    # Add parent groups
    for parent in by_parent.keys():
        if parent is not None:
            parent_info = database_info.get(parent, {})
            parent_name = parent_info.get("display_name_when_parent", parent)
            entries.append((parent, parent_name, parent))

    # Sort all entries alphabetically by slug
    entries.sort(key=lambda x: x[0])

    # Build the markdown list
    lines = []
    for slug, name, parent in entries:
        if parent is None:
            # Standalone database
            lines.append(f"- {name}")
        else:
            # Parent group with children
            lines.append(f"- {name}")
            for child_slug in sorted(by_parent[parent]):
                child_info = database_info.get(child_slug, {})
                child_name = child_info.get("name", child_slug.title())
                lines.append(f"  - {child_name}")

    databases_list = "\n".join(lines)

    return template.format(
        databases_list=databases_list,
        languages_list=languages_list,
    )


def restructure(source_root: Path, output_root: Path) -> None:
    """
    Restructure the repository from language-first to database-first.

    Args:
        source_root: Path to the source repository root
        output_root: Path to the output directory
    """
    # Load display name mappings
    language_display_names, database_info = load_display_names()

    # Clean output directory if it exists
    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True)

    # Copy LICENSE file
    license_file = source_root / "LICENSE"
    if license_file.exists():
        shutil.copy2(license_file, output_root / "LICENSE")

    # Discover all databases
    databases = discover_databases(source_root, database_info)

    print(f"Discovered {len(databases)} databases:")
    for db_name in sorted(databases.keys()):
        langs = ", ".join(sorted(databases[db_name].keys()))
        print(f"  {db_name}: {langs}")

    # Generate root README.md for by-database branch
    root_readme = generate_by_database_root_readme(
        databases, language_display_names, database_info
    )
    root_readme_path = output_root / "README.md"
    root_readme_path.write_text(root_readme)
    print(f"Generated {root_readme_path}")

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

        # Generate README.md for this database
        readme_content = generate_database_readme(
            db_name,
            list(lang_paths.keys()),
            language_display_names,
            database_info,
        )
        readme_path = db_output / "README.md"
        readme_path.write_text(readme_content)
        print(f"  Generated {readme_path}")

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
