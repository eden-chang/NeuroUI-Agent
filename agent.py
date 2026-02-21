"""NeuroUI Agent — core agent loop using Claude API tool-use pattern.

This module implements the agentic loop: send user message to Claude,
handle tool calls, feed results back, repeat until a final text response.
"""

from __future__ import annotations

import json
import os
from typing import Any

from anthropic import Anthropic
from dotenv import load_dotenv

from tools import generate_component_code, get_guidelines, search_components

load_dotenv()

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# ---------------------------------------------------------------------------
# Tool definitions (Claude API format)
# ---------------------------------------------------------------------------

TOOLS: list[dict[str, Any]] = [
    {
        "name": "search_components",
        "description": (
            "Search the NeuroUI component catalog by keyword or neurodiversity "
            "condition. Use this to find components that match the user's needs."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": (
                        "Search keyword (e.g., 'task list', 'notification', "
                        "'navigation', 'form')"
                    ),
                },
                "condition": {
                    "type": "string",
                    "description": (
                        "Neurodiversity condition to filter by "
                        "(e.g., 'ADHD', 'autism', 'dyslexia', 'sensory-sensitivity')"
                    ),
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "get_guidelines",
        "description": (
            "Retrieve cognitive science-based accessibility guidelines for a "
            "specific neurodiversity condition. Use this to understand design "
            "principles before making recommendations."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "condition": {
                    "type": "string",
                    "description": (
                        "The neurodiversity condition "
                        "(e.g., 'ADHD', 'autism', 'dyslexia', "
                        "'sensory-sensitivity', 'motor-impairment')"
                    ),
                },
            },
            "required": ["condition"],
        },
    },
    {
        "name": "generate_component_code",
        "description": (
            "Generate import statements and usage code for a specific NeuroUI "
            "component. Use this after selecting the best component for the user."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "component_id": {
                    "type": "string",
                    "description": "The ID of the component from the catalog",
                },
                "custom_props": {
                    "type": "object",
                    "description": (
                        "Optional custom prop values to include in generated code"
                    ),
                },
            },
            "required": ["component_id"],
        },
    },
]

# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are NeuroUI Agent, an AI assistant that helps developers build accessible \
web interfaces for neurodivergent users.

You have access to the NeuroUI component library and cognitive science-based \
accessibility guidelines. When a user describes what they need, you should:

1. First, understand which neurodiversity condition(s) are relevant
2. Look up the accessibility guidelines for that condition to ground your reasoning
3. Search the component catalog for matching components
4. Recommend the best component(s) with a clear explanation of WHY they are \
   suitable, referencing specific cognitive science principles
5. Generate ready-to-use code

Always explain your reasoning in terms of cognitive science principles. \
For example, don't just say "this reduces clutter" — explain WHY reduced clutter \
helps (e.g., "reduces demands on working memory, which is particularly important \
for users with ADHD whose executive function may be affected").

When recommending multiple components, explain how they work together and why \
the combination serves the user's needs.\
"""

# ---------------------------------------------------------------------------
# Tool dispatch
# ---------------------------------------------------------------------------

TOOL_FUNCTIONS: dict[str, Any] = {
    "search_components": search_components,
    "get_guidelines": get_guidelines,
    "generate_component_code": generate_component_code,
}

# ---------------------------------------------------------------------------
# Agent loop
# ---------------------------------------------------------------------------


def run_agent(user_message: str, *, verbose: bool = True) -> str:
    """Run the agent loop for a single user message.

    Args:
        user_message: The natural-language request from the user.
        verbose: If True, print tool call information to stdout.

    Returns:
        The agent's final text response.
    """
    messages: list[dict[str, Any]] = [
        {"role": "user", "content": user_message},
    ]

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )

        if response.stop_reason == "end_turn":
            final_text = ""
            for block in response.content:
                if hasattr(block, "text"):
                    final_text += block.text
            return final_text

        if response.stop_reason == "tool_use":
            # Add assistant message (with tool_use blocks) to conversation
            messages.append({"role": "assistant", "content": response.content})

            # Process each tool call
            tool_results: list[dict[str, Any]] = []
            for block in response.content:
                if block.type == "tool_use":
                    tool_name = block.name
                    tool_input = block.input

                    if verbose:
                        print(
                            f"  [Tool Call] {tool_name}"
                            f"({json.dumps(tool_input, ensure_ascii=False)})"
                        )

                    if tool_name in TOOL_FUNCTIONS:
                        result = TOOL_FUNCTIONS[tool_name](**tool_input)
                    else:
                        result = json.dumps(
                            {"error": f"Unknown tool: {tool_name}"}
                        )

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    })

            messages.append({"role": "user", "content": tool_results})

        else:
            return f"Unexpected stop reason: {response.stop_reason}"
