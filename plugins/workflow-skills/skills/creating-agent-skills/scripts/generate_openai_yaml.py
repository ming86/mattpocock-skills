#!/usr/bin/env python3
"""
OpenAI YAML Generator - Creates agents/openai.yaml for a skill folder.

Usage:
    generate_openai_yaml.py <skill_dir> [--name <skill_name>] [--interface key=value]
"""

import argparse
import re
import sys
from pathlib import Path

import yaml

ACRONYMS = {
    "GH",
    "MCP",
    "API",
    "CI",
    "CLI",
    "LLM",
    "PDF",
    "PR",
    "UI",
    "URL",
    "SQL",
}

BRANDS = {
    "openai": "OpenAI",
    "openapi": "OpenAPI",
    "github": "GitHub",
    "pagerduty": "PagerDuty",
    "datadog": "DataDog",
    "sqlite": "SQLite",
    "fastapi": "FastAPI",
}

SMALL_WORDS = {"and", "or", "to", "up", "with"}

ALLOWED_INTERFACE_KEYS = {
    "display_name",
    "short_description",
    "icon_small",
    "icon_large",
    "brand_color",
    "default_prompt",
}


def yaml_quote(value):
    escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    return f'"{escaped}"'


def format_display_name(skill_name):
    words = [word for word in skill_name.split("-") if word]
    formatted = []
    for index, word in enumerate(words):
        lower = word.lower()
        upper = word.upper()
        if upper in ACRONYMS:
            formatted.append(upper)
            continue
        if lower in BRANDS:
            formatted.append(BRANDS[lower])
            continue
        if index > 0 and lower in SMALL_WORDS:
            formatted.append(lower)
            continue
        formatted.append(word.capitalize())
    return " ".join(formatted)


def generate_short_description(display_name):
    description = f"Help with {display_name} tasks"

    if len(description) < 25:
        description = f"Help with {display_name} tasks and workflows"
    if len(description) < 25:
        description = f"Help with {display_name} tasks with guidance"

    if len(description) > 64:
        description = f"Help with {display_name}"
    if len(description) > 64:
        description = f"{display_name} helper"
    if len(description) > 64:
        description = f"{display_name} tools"
    if len(description) > 64:
        suffix = " helper"
        max_name_length = 64 - len(suffix)
        trimmed = display_name[:max_name_length].rstrip()
        description = f"{trimmed}{suffix}"
    if len(description) > 64:
        description = description[:64].rstrip()

    if len(description) < 25:
        description = f"{description} workflows"
        if len(description) > 64:
            description = description[:64].rstrip()

    return description


def read_frontmatter_name(skill_dir):
    skill_md = Path(skill_dir) / "SKILL.md"
    if not skill_md.exists():
        print(f"[ERROR] SKILL.md not found in {skill_dir}")
        return None
    content = skill_md.read_text()
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        print("[ERROR] Invalid SKILL.md frontmatter format.")
        return None
    frontmatter_text = match.group(1)
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as exc:
        print(f"[ERROR] Invalid YAML frontmatter: {exc}")
        return None
    if not isinstance(frontmatter, dict):
        print("[ERROR] Frontmatter must be a YAML dictionary.")
        return None
    name = frontmatter.get("name", "")
    if not isinstance(name, str) or not name.strip():
        print("[ERROR] Frontmatter 'name' is missing or invalid.")
        return None
    return name.strip()


def parse_interface_overrides(raw_overrides):
    overrides = {}
    optional_order = []
    for item in raw_overrides:
        if "=" not in item:
            print(f"[ERROR] Invalid interface override '{item}'. Use key=value.")
            return None, None
        key, value = item.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            print(f"[ERROR] Invalid interface override '{item}'. Key is empty.")
            return None, None
        if key not in ALLOWED_INTERFACE_KEYS:
            allowed = ", ".join(sorted(ALLOWED_INTERFACE_KEYS))
            print(f"[ERROR] Unknown interface field '{key}'. Allowed: {allowed}")
            return None, None
        overrides[key] = value
        if key not in ("display_name", "short_description") and key not in optional_order:
            optional_order.append(key)
    return overrides, optional_order


def read_existing_openai_yaml(output_path):
    if not output_path.exists():
        return "", {}

    content = output_path.read_text()
    try:
        metadata = yaml.safe_load(content)
    except yaml.YAMLError as exc:
        print(f"[ERROR] Invalid existing agents/openai.yaml: {exc}")
        return None, None

    if metadata is None:
        metadata = {}
    if not isinstance(metadata, dict):
        print("[ERROR] Existing agents/openai.yaml must be a YAML dictionary.")
        return None, None

    interface = metadata.get("interface", {})
    if interface is None:
        interface = {}
    if not isinstance(interface, dict):
        print("[ERROR] Existing agents/openai.yaml 'interface' must be a YAML dictionary.")
        return None, None

    return content, interface


def replace_interface_block(existing_content, interface_lines):
    rendered = "\n".join(interface_lines)
    if not existing_content.strip():
        return rendered + "\n"

    lines = existing_content.splitlines()
    start = next((i for i, line in enumerate(lines) if line == "interface:"), None)
    if start is None:
        return rendered + "\n\n" + existing_content.lstrip("\n")

    end = len(lines)
    for i in range(start + 1, len(lines)):
        line = lines[i]
        if line and not line[0].isspace():
            end = i
            break

    before = lines[:start]
    after = lines[end:]
    result = before + interface_lines
    if after and result and result[-1] != "" and after[0] != "":
        result.append("")
    result.extend(after)
    return "\n".join(result).rstrip("\n") + "\n"


def write_openai_yaml(skill_dir, skill_name, raw_overrides):
    overrides, optional_order = parse_interface_overrides(raw_overrides)
    if overrides is None:
        return None

    agents_dir = Path(skill_dir) / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    output_path = agents_dir / "openai.yaml"

    existing_content, existing_interface = read_existing_openai_yaml(output_path)
    if existing_content is None:
        return None

    display_name = overrides.get("display_name") or format_display_name(skill_name)
    short_description = overrides.get("short_description") or generate_short_description(display_name)

    if not (25 <= len(short_description) <= 64):
        print(
            "[ERROR] short_description must be 25-64 characters "
            f"(got {len(short_description)})."
        )
        return None

    interface_lines = [
        "interface:",
        f"  display_name: {yaml_quote(display_name)}",
        f"  short_description: {yaml_quote(short_description)}",
    ]

    preserved_optional_order = [
        key
        for key in existing_interface
        if key not in ("display_name", "short_description") and key in ALLOWED_INTERFACE_KEYS
    ]
    for key in optional_order:
        if key not in preserved_optional_order:
            preserved_optional_order.append(key)

    for key in preserved_optional_order:
        value = overrides.get(key, existing_interface.get(key))
        if value is not None:
            if not isinstance(value, str):
                print(f"[ERROR] Existing interface field '{key}' must be a string.")
                return None
            interface_lines.append(f"  {key}: {yaml_quote(value)}")

    output_path.write_text(replace_interface_block(existing_content, interface_lines))
    print(f"[OK] Created agents/openai.yaml")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Create agents/openai.yaml for a skill directory.",
    )
    parser.add_argument("skill_dir", help="Path to the skill directory")
    parser.add_argument(
        "--name",
        help="Skill name override (defaults to SKILL.md frontmatter)",
    )
    parser.add_argument(
        "--interface",
        action="append",
        default=[],
        help="Interface override in key=value format (repeatable)",
    )
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    if not skill_dir.exists():
        print(f"[ERROR] Skill directory not found: {skill_dir}")
        sys.exit(1)
    if not skill_dir.is_dir():
        print(f"[ERROR] Path is not a directory: {skill_dir}")
        sys.exit(1)

    skill_name = args.name or read_frontmatter_name(skill_dir)
    if not skill_name:
        sys.exit(1)

    result = write_openai_yaml(skill_dir, skill_name, args.interface)
    if result:
        sys.exit(0)
    sys.exit(1)


if __name__ == "__main__":
    main()
