# awesome-grok-agents

**10 production-ready Grok agents. One command to install.**

A curated gallery of grok-install-compatible agent templates built on xAI's
Grok models. Every template is end-to-end runnable, permission-scoped, and
shipped with a working demo.

```bash
pip install grok-install
grok-install install github.com/agentmindcloud/awesome-grok-agents/templates/<name>
```

## Gallery

| # | Name | What it does | Install |
|---|------|--------------|---------|
| 1 | [hello-grok](templates/hello-grok) | The simplest possible Grok agent. Single agent, single tool. | `grok-install install github.com/agentmindcloud/awesome-grok-agents/templates/hello-grok` |
| 2 | [reply-engagement-bot](templates/reply-engagement-bot) | Watches your X mentions and drafts thoughtful replies with approval gate. | `grok-install install github.com/agentmindcloud/awesome-grok-agents/templates/reply-engagement-bot` |
| 3 | [trend-to-thread](templates/trend-to-thread) | Monitors X trends and drafts a full thread on topics you care about. | `grok-install install github.com/agentmindcloud/awesome-grok-agents/templates/trend-to-thread` |
| 4 | [research-swarm](templates/research-swarm) | Researcher + critic + publisher swarm. Multi-agent reasoning. | `grok-install install github.com/agentmindcloud/awesome-grok-agents/templates/research-swarm` |
| 5 | [code-reviewer](templates/code-reviewer) | Reviews GitHub PRs with Grok reasoning. Posts inline comments. | `grok-install install github.com/agentmindcloud/awesome-grok-agents/templates/code-reviewer` |
| 6 | [thread-ghostwriter](templates/thread-ghostwriter) | Turns a rough idea into a polished X thread. | `grok-install install github.com/agentmindcloud/awesome-grok-agents/templates/thread-ghostwriter` |
| 7 | [personal-knowledge](templates/personal-knowledge) | Builds a persistent memory of your X history you can query. | `grok-install install github.com/agentmindcloud/awesome-grok-agents/templates/personal-knowledge` |
| 8 | [scientific-discovery](templates/scientific-discovery) | Summarizes new papers + the X discussion around them. | `grok-install install github.com/agentmindcloud/awesome-grok-agents/templates/scientific-discovery` |
| 9 | [voice-agent-x](templates/voice-agent-x) | Voice-to-X: speak a post, review a transcript, publish. | `grok-install install github.com/agentmindcloud/awesome-grok-agents/templates/voice-agent-x` |
| 10 | [live-event-commentator](templates/live-event-commentator) | Live event commentary on X with rate-limited posting. | `grok-install install github.com/agentmindcloud/awesome-grok-agents/templates/live-event-commentator` |

## Quick start

```bash
pip install grok-install

# Install any template
grok-install install github.com/agentmindcloud/awesome-grok-agents/templates/hello-grok

# Configure
cd hello-grok
cp .env.example .env  # fill in XAI_API_KEY and any other secrets

# Run
grok-install run
```

Every template validates with `grok-install validate` and passes
`grok-install scan` with zero warnings.

## Grok-Native Certified

Templates tagged `certified: true` in [featured-agents.json](featured-agents.json)
meet every item on this bar:

- Runs end-to-end (CI enforced on every PR)
- Declares permissions explicitly
- Sets an appropriate `safety_profile`
- Every tool has a complete JSON schema
- X-writing tools gated behind human approval
- Rate limits declared
- No hardcoded credentials
- Under 150 lines of YAML total

## Contributing

Want to add your agent to the gallery? See
[CONTRIBUTING.md](CONTRIBUTING.md) and
[docs/submitting-your-own.md](docs/submitting-your-own.md).

Your PR must pass `.github/workflows/validate-templates.yml` — which runs
`grok-install validate`, `grok-install scan`, a mock run, and `yamllint` on
every template.

## License

Apache 2.0. See [LICENSE](LICENSE).
