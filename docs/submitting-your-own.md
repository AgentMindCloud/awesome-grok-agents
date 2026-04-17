# Submitting your own template

Got a Grok agent that might help others? Here's the path from idea to merged
PR.

## 1. Build locally

Start from `templates/hello-grok` — it has the minimum viable structure.

```bash
cp -r templates/hello-grok templates/my-awesome-agent
cd templates/my-awesome-agent
```

Edit `grok-install.yaml`, the files in `.grok/`, and `tools/custom_tools.py`.
Keep YAML under 150 lines total. If you need more, your agent is probably
doing two jobs — split it.

## 2. Validate locally

```bash
pip install grok-install yamllint
grok-install validate .
grok-install scan . --fail-on warning
yamllint -c ../../.yamllint.yml .
```

Then do a real run against your own X or GitHub credentials to confirm the
agent actually works.

## 3. Write the README

Use the structure in [template-anatomy.md](template-anatomy.md). The demo
gif should be short (≤60s) and show the end-to-end flow — install, configure,
first useful output.

## 4. Register it

Add an entry to the root `featured-agents.json`. The CI registry check
validates the path, the required files, and the safety profile.

Set `certified: false` if you're not yet meeting the full quality bar —
your template can still land, it just won't carry the certified badge.

## 5. Open a PR

CI will run four checks:

1. `yamllint` on every YAML file
2. `grok-install validate` on your template
3. `grok-install scan --fail-on warning`
4. A mock run (no real API calls)

Two reviewer approvals land a new template; one lands doc or fix PRs.

## Design tips

- **One job per agent.** If your template description needs the word "and",
  you probably want two templates.
- **Gate every external write.** Anything that posts to X, comments on a
  PR, or sends a message belongs under `requires_approval`.
- **Name your permissions tightly.** `x.post` is better than `x.*`. Least
  privilege keeps the safety scan green.
- **Reference prompts by key.** Inline prompts make the agent file hard to
  read. Put them in `grok-prompts.yaml`.
- **Don't fake outputs in the mock.** `GROK_INSTALL_MODE=mock` should
  exercise the same code path, just with stub API clients.

Questions? Open a discussion before you open the PR — happy to help shape
the idea.
