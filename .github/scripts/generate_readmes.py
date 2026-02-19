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
Generate README files for the ADBC quickstarts repository.

Generates:
- Root README.md
- Per-language README.md files (cpp, go, java, python, r, rust)
"""

import argparse
import json
from pathlib import Path


# Languages in the repository
LANGUAGES = ["cpp", "go", "java", "python", "r", "rust"]


def load_mappings() -> tuple[dict[str, str], dict[str, dict]]:
    """
    Load language and database mappings from JSON files.

    Returns:
        Tuple of (language_display_names, database_info)
    """
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / "data"

    with open(data_dir / "languages.json") as f:
        language_names = json.load(f)

    with open(data_dir / "databases.json") as f:
        database_info = json.load(f)

    return language_names, database_info


def discover_databases_for_language(
    language_dir: Path, database_info: dict[str, dict]
) -> list[str]:
    """
    Discover which databases are available for a given language.

    Args:
        language_dir: Path to the language directory (e.g., cpp/)
        database_info: Database information from JSON

    Returns:
        List of database slugs available for this language
    """
    if not language_dir.is_dir():
        return []

    # Determine which directories are parent directories
    # (those with non-null display_name_when_parent)
    parent_dirs = {
        slug
        for slug, info in database_info.items()
        if info.get("display_name_when_parent") is not None
    }

    databases = []

    for item in language_dir.iterdir():
        if not item.is_dir():
            continue

        # Check if this is a parent directory
        if item.name in parent_dirs:
            # This is a protocol directory, check subdirectories
            for db_dir in item.iterdir():
                if db_dir.is_dir() and db_dir.name in database_info:
                    databases.append(db_dir.name)
        elif item.name in database_info:
            # This is a direct database directory
            databases.append(item.name)

    return databases


def format_databases_list(
    database_slugs: list[str], database_info: dict[str, dict]
) -> str:
    """
    Format the list of databases with proper grouping.

    Args:
        database_slugs: List of database slugs
        database_info: Database information from JSON

    Returns:
        Formatted markdown list
    """
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
            name = database_info[slug]["name"]
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
                child_name = database_info[child_slug]["name"]
                lines.append(f"  - {child_name}")

    return "\n".join(lines)


def generate_root_readme(
    repo_root: Path, language_names: dict[str, str], database_info: dict[str, dict]
) -> str:
    """
    Generate the root README.md content.

    Args:
        repo_root: Path to repository root
        language_names: Language display names
        database_info: Database information

    Returns:
        README content
    """
    # Load template
    script_dir = Path(__file__).parent
    template_path = script_dir.parent / "data" / "main-root-readme-template.md"
    template = template_path.read_text()

    # Generate language list
    languages_list = "\n".join(
        f"- {language_names[lang]}" for lang in LANGUAGES if lang in language_names
    )

    # Discover all databases (use cpp as authoritative source)
    cpp_databases = discover_databases_for_language(
        repo_root / "cpp", database_info
    )
    databases_list = format_databases_list(cpp_databases, database_info)

    return template.format(
        languages_list=languages_list,
        databases_list=databases_list,
    )


def generate_language_readme(
    repo_root: Path,
    language: str,
    language_names: dict[str, str],
    database_info: dict[str, dict],
) -> str:
    """
    Generate a language-specific README.md content.

    Args:
        repo_root: Path to repository root
        language: Language slug (e.g., "cpp")
        language_names: Language display names
        database_info: Database information

    Returns:
        README content
    """
    # Load template
    script_dir = Path(__file__).parent
    template_path = script_dir.parent / "data" / "language-readme-template.md"
    template = template_path.read_text()

    # Get language display name
    language_name = language_names.get(language, language.upper())

    # Discover databases for this language
    language_dir = repo_root / language
    databases = discover_databases_for_language(language_dir, database_info)
    databases_list = format_databases_list(databases, database_info)

    return template.format(
        language_name=language_name,
        databases_list=databases_list,
    )


def generate_protocol_readme(
    repo_root: Path,
    language: str,
    protocol: str,
    language_names: dict[str, str],
    database_info: dict[str, dict],
) -> str:
    """
    Generate a protocol-specific README.md content.

    Args:
        repo_root: Path to repository root
        language: Language slug (e.g., "cpp")
        protocol: Protocol slug (e.g., "postgresql")
        language_names: Language display names
        database_info: Database information

    Returns:
        README content
    """
    # Load template
    script_dir = Path(__file__).parent
    template_path = script_dir.parent / "data" / "protocol-readme-template.md"
    template = template_path.read_text()

    # Get protocol info
    protocol_info = database_info.get(protocol, {})
    protocol_name = protocol_info.get("display_name_when_parent", protocol_info.get("name", protocol.title()))
    language_name = language_names.get(language, language.upper())

    # Get protocol description with language substitution
    protocol_description = protocol_info.get("protocol_description", "")
    protocol_description = protocol_description.replace("{language}", language_name)

    # Get source systems intro
    source_systems_intro = protocol_info.get("source_systems_intro", "")

    # Discover databases in this protocol directory
    protocol_dir = repo_root / language / protocol
    if not protocol_dir.is_dir():
        return ""

    databases = []
    for item in protocol_dir.iterdir():
        if item.is_dir() and item.name in database_info:
            databases.append(item.name)

    # Format database list (simple bulleted list, no grouping)
    databases_list = "\n".join(
        f"- {database_info[slug]['name']}" for slug in sorted(databases)
    )

    return template.format(
        language_name=language_name,
        protocol_name=protocol_name,
        protocol_description=protocol_description,
        source_systems_intro=source_systems_intro,
        databases_list=databases_list,
    )


def main():
    parser = argparse.ArgumentParser(
        description="Generate README files for ADBC quickstarts"
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root directory (default: current directory)",
    )

    args = parser.parse_args()

    if not args.repo_root.is_dir():
        parser.error(f"Repository root does not exist: {args.repo_root}")

    # Load mappings
    language_names, database_info = load_mappings()

    # Generate root README
    print("Generating root README.md...")
    root_readme = generate_root_readme(args.repo_root, language_names, database_info)
    root_readme_path = args.repo_root / "README.md"
    root_readme_path.write_text(root_readme)
    print(f"  Written to {root_readme_path}")

    # Generate language READMEs
    for language in LANGUAGES:
        language_dir = args.repo_root / language
        if not language_dir.is_dir():
            print(f"Skipping {language} (directory not found)")
            continue

        print(f"Generating {language}/README.md...")
        language_readme = generate_language_readme(
            args.repo_root, language, language_names, database_info
        )
        language_readme_path = language_dir / "README.md"
        language_readme_path.write_text(language_readme)
        print(f"  Written to {language_readme_path}")

        # Generate protocol READMEs for this language
        # Determine which directories are protocol directories
        protocol_dirs = [
            slug
            for slug, info in database_info.items()
            if info.get("display_name_when_parent") is not None
        ]

        for protocol in protocol_dirs:
            protocol_dir = language_dir / protocol
            if not protocol_dir.is_dir():
                continue

            print(f"Generating {language}/{protocol}/README.md...")
            protocol_readme = generate_protocol_readme(
                args.repo_root, language, protocol, language_names, database_info
            )
            if protocol_readme:
                protocol_readme_path = protocol_dir / "README.md"
                protocol_readme_path.write_text(protocol_readme)
                print(f"  Written to {protocol_readme_path}")

    print("\nAll README files generated successfully!")


if __name__ == "__main__":
    main()
