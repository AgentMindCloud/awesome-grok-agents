"""Validate featured-agents.json against the repo layout.

Schema v1.0 (marketplace-facing):
  id, name, tagline, category, tags, github, install_link, install_command,
  demo_url, safety_score, safety_profile, certifications, created_at, creator,
  path, poster
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "featured-agents.json"
TEMPLATES = ROOT / "templates"
AGENTS = ROOT / "agents"

REQUIRED_FIELDS = {
    "id",
    "name",
    "tagline",
    "category",
    "tags",
    "github",
    "install_link",
    "install_command",
    "demo_url",
    "safety_score",
    "safety_profile",
    "certifications",
    "created_at",
    "creator",
    "path",
    "poster",
}
VALID_SAFETY = {"strict", "standard", "permissive"}
VALID_CERTS = {"grok-native", "safety-max", "voice-ready", "swarm-ready"}
PLACEHOLDER_MARKERS = ("todo", "placeholder", "example.com", "xxx")


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    data = json.loads(REGISTRY.read_text())

    if data.get("version") != "1.0":
        fail("registry version must be '1.0'")

    seen_ids: set[str] = set()
    seen_names: set[str] = set()

    for agent in data.get("agents", []):
        missing = REQUIRED_FIELDS - agent.keys()
        if missing:
            fail(f"{agent.get('id', '?')}: missing fields {sorted(missing)}")

        agent_id = agent["id"]
        if agent_id in seen_ids:
            fail(f"duplicate agent id: {agent_id}")
        seen_ids.add(agent_id)

        if agent["name"] in seen_names:
            fail(f"duplicate agent name: {agent['name']}")
        seen_names.add(agent["name"])

        if agent["safety_profile"] not in VALID_SAFETY:
            fail(f"{agent_id}: invalid safety_profile {agent['safety_profile']!r}")

        score = agent["safety_score"]
        if not isinstance(score, int) or not (0 <= score <= 100):
            fail(f"{agent_id}: safety_score must be an int 0..100")

        for cert in agent["certifications"]:
            if cert not in VALID_CERTS:
                fail(f"{agent_id}: unknown certification {cert!r}")

        # demo_url: either null or a real https URL. Never a placeholder.
        demo = agent["demo_url"]
        if demo is not None:
            if not isinstance(demo, str) or not demo.startswith("https://"):
                fail(f"{agent_id}: demo_url must be null or an https URL")
            if any(m in demo.lower() for m in PLACEHOLDER_MARKERS):
                fail(f"{agent_id}: demo_url looks like a placeholder ({demo!r})")

        agent_dir = ROOT / agent["path"]
        if not agent_dir.is_dir():
            fail(f"{agent_id}: path {agent['path']} does not exist")
        for required in ("grok-install.yaml", "README.md"):
            if not (agent_dir / required).exists():
                fail(f"{agent_id}: missing {required}")
        if not (agent_dir / ".grok").is_dir():
            fail(f"{agent_id}: missing .grok/ directory")

        poster = ROOT / agent["poster"]
        if not poster.is_file():
            fail(f"{agent_id}: poster {agent['poster']} does not exist")

    # Cross-reference: every dir in templates/ and agents/ must be listed.
    listed = seen_ids
    on_disk: set[str] = set()
    for container in (TEMPLATES, AGENTS):
        if container.is_dir():
            on_disk |= {p.name for p in container.iterdir() if p.is_dir()}
    orphans = on_disk - listed
    if orphans:
        fail(f"agents on disk but not in registry: {sorted(orphans)}")
    ghosts = listed - on_disk
    if ghosts:
        fail(f"registry entries with no agent dir: {sorted(ghosts)}")

    print(f"registry OK: {len(seen_ids)} agents")


if __name__ == "__main__":
    main()
