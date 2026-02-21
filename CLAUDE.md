# Project Instructions for Claude Code

## Git Authorship Rules

**CRITICAL: Never add Claude Code as a co-author in any git commit.**

- Do NOT add `Co-authored-by:` trailers to commit messages
- Do NOT add `Signed-off-by:` trailers referencing Claude or Anthropic
- Do NOT modify git config to add Claude as an author
- The ONLY author for all commits is: **eden-chang <eden.chang27@gmail.com>**
- When creating commits, use ONLY the user's configured git identity

## Project: neuroui-agent

- Python 3.10+ project using Anthropic Claude API tool-use
- No frameworks (LangChain, etc.) — raw Anthropic SDK only
- JSON files in `data/` for component catalog and guidelines
