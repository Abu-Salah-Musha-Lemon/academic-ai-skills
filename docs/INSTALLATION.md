# Installation and use

This repository follows the open Agent Skills format: a skill is a folder with a `SKILL.md` containing YAML frontmatter (`name`, `description`) and instructions. Agent clients differ in where they load skills and how they import them.

## Platform-neutral method
1. Download or clone this repository.
2. Choose the skill folder you need.
3. Use your AI client’s documented import flow, or copy the folder to the client’s skills directory.
4. Make sure the skill folder and its `SKILL.md` stay together.
5. Ask the AI to use the skill by name and provide relevant context.

## Example: manual install

Copy one folder, such as `skills/sop-writing/`, into a skills directory supported by your AI tool. The exact directory varies by tool, operating system, and configuration. Check the target product's official documentation before copying.

## Example: instruction-only clients

If your AI client does not support folder-based skills, open the chosen `SKILL.md` and paste its contents into the relevant project, custom-agent, or custom-instruction area. Keep the skill-specific instructions intact.

## Use templates

Templates in `templates/` are optional intake forms. Fill only the fields relevant to your task. Avoid sharing unnecessary sensitive data.

## Compatibility

The skills are platform-neutral and intended for clients that support Agent Skills or can accept Markdown instructions. This repository does not currently provide installers for every client, nor does it claim that every client automatically discovers the skills.

## Specification reference

- Agent Skills specification: https://agentskills.io/specification
- Official specification repository: https://github.com/agentskills/agentskills

Each skill directory name must match its `name` metadata, and each `SKILL.md` includes a `description` that helps agents discover when to use it. The project includes additional `license` and `metadata` fields.
