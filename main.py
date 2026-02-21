"""NeuroUI Agent — CLI entry point.

Run this script to start an interactive session with the agent.
"""

from __future__ import annotations

import io
import sys

# Fix Windows console encoding — allow emoji and unicode output
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding="utf-8", errors="replace"
    )
    sys.stderr = io.TextIOWrapper(
        sys.stderr.buffer, encoding="utf-8", errors="replace"
    )

from agent import run_agent


def main() -> None:
    print("=" * 60)
    print("  NeuroUI Agent")
    print("  Accessible component recommendations powered by AI")
    print("=" * 60)
    print()
    print("Describe what you need and I'll recommend NeuroUI components")
    print("with cognitive-science-backed reasoning.")
    print("Type 'quit' or 'exit' to stop.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        print("\nAgent is thinking...\n")

        try:
            result = run_agent(user_input)
        except Exception as exc:
            print(f"Error: {exc}", file=sys.stderr)
            continue

        print(f"\nAgent: {result}\n")


if __name__ == "__main__":
    main()
