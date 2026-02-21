"""Tool functions for the NeuroUI Agent.

These are the 'hands' of the agent — callable functions that search the
component catalog, retrieve accessibility guidelines, and generate code.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

DATA_DIR = Path(__file__).parent / "data"


def search_components(query: str, condition: Optional[str] = None) -> str:
    """Search the NeuroUI component catalog by keyword or neurodiversity condition."""
    with open(DATA_DIR / "components.json", "r", encoding="utf-8") as f:
        components: list[dict] = json.load(f)

    results: list[dict] = []
    seen_ids: set[str] = set()

    for comp in components:
        searchable = (
            f"{comp['name']} {comp['description']} {comp['category']} "
            f"{' '.join(comp.get('neurodiversity_features', []))}"
        ).lower()

        matched = query.lower() in searchable

        if not matched and condition:
            matched = condition.lower() in [
                c.lower() for c in comp.get("suitable_for", [])
            ]

        if matched and comp["id"] not in seen_ids:
            results.append(comp)
            seen_ids.add(comp["id"])

    if not results:
        return json.dumps({"results": [], "message": "No matching components found."})
    return json.dumps({"results": results})


def get_guidelines(condition: str) -> str:
    """Retrieve cognitive-science-based accessibility guidelines for a condition."""
    with open(DATA_DIR / "guidelines.json", "r", encoding="utf-8") as f:
        guidelines: list[dict] = json.load(f)

    for g in guidelines:
        if g["condition"].lower() == condition.lower():
            return json.dumps(g)

    available = [g["condition"] for g in guidelines]
    return json.dumps({
        "error": f"No guidelines found for condition: {condition}",
        "available_conditions": available,
    })


def generate_component_code(
    component_id: str, custom_props: Optional[dict] = None
) -> str:
    """Generate import statement and usage code for a NeuroUI component."""
    with open(DATA_DIR / "components.json", "r", encoding="utf-8") as f:
        components: list[dict] = json.load(f)

    for comp in components:
        if comp["id"] == component_id:
            # Build custom props string if provided
            props_str = ""
            if custom_props:
                parts: list[str] = []
                for k, v in custom_props.items():
                    if isinstance(v, str):
                        parts.append(f'{k}="{v}"')
                    elif isinstance(v, bool):
                        parts.append(f"{k}={{{str(v).lower()}}}")
                    else:
                        parts.append(f"{k}={{{json.dumps(v)}}}")
                props_str = " ".join(parts)

            # Determine the base component name (strip parenthetical notes)
            base_name = comp["name"].split("(")[0].strip()
            # Handle compound exports like "Radio / RadioGroup"
            export_names = [n.strip() for n in base_name.split("/")]

            import_names = ", ".join(export_names)
            import_statement = (
                f"import {{ {import_names} }} from '@neuroui/components';"
            )

            return json.dumps({
                "component": comp["name"],
                "import_statement": import_statement,
                "usage": comp["usage_example"],
                "available_props": comp["props"],
                "custom_usage": f"<{export_names[0]} {props_str} />" if props_str else None,
            })

    available_ids = [comp["id"] for comp in components]
    return json.dumps({
        "error": f"Component not found: {component_id}",
        "available_ids": available_ids,
    })
