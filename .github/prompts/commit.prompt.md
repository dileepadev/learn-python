---
agent: "agent"
model: GPT-4o (copilot)
tools: ["execute", "read", "search"]
description: "Generate a new commit message based on the provided code changes."
---

Your goal is to generate the most appropriate and effective commit message based on the provided code changes.

## Commit Message Guidelines

Commit messages should be written clearly and consistently, following the project’s template.

- **Follow the commit message guidelines** outlined in the project's COMMIT_MESSAGE_GUIDELINES.md file.
- **Provide the commit message as a Zsh-ready command**, so it can be run directly in the terminal.
- **Check the changes first**: identify added, modified, or deleted files.
- **Describe the changes according to the template**:
  - For **multiple files**, summarize changes at a high level.
  - For **a single file**, describe the exact modification.
- Include **code snippets or terminal commands in Zsh format** where indicated by the template.
- **Consistency is key**: ensure every commit follows the template to keep project history clear and uniform.
- Current references for the commit message: N/A
