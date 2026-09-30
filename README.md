# connectkit

Connector toolkit for Perplexity Computer.

Computer gives a skill a connector surface and very little to debug it with. When a
call fails you get a status code, with no indication of whether the fault is your
skill, the environment, or the connector. These are the tools we ended up writing.

## Install

```bash
pip install connectkit
```

## Getting started

```bash
connectkit status     # what did this sandbox resolve?
connectkit list --connected
connectkit describe gcal
```

## Commands

| Command | Does |
| --- | --- |
| `connectkit status` | Resolved base URLs and pair completeness |
| `connectkit list [--connected]` | List connectors |
| `connectkit find <query>` | Search connectors by id or display name |
| `connectkit describe <source_id>` | Tool schemas, cached for an hour |
| `connectkit call <source_id> <tool>` | Call a connector tool |
| `connectkit new <name>` | Scaffold a skill directory |
| `connectkit validate <dir>` | Check a skill against the Agent Skills layout |

## Why pairs matter

Each service is configured as a pair: a public base URL requests are sent to, and an
internal target base URL the pass-through proxy forwards to. The proxy rejects any
request whose `X-Base-Url` is not in the session's allowed set, so a half-configured
pair fails like a permissions problem rather than a configuration one. `connectkit
status` reports which pairs are complete.

## Docs

<https://connectkit-tools.vercel.app>
