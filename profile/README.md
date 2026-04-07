<p align="center">
  <img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/ellmos-logo.jpg" alt="ellmos logo" width="300">
</p>

<h3 align="center">Extra Large Language Model Operating Systems</h3>
<p align="center"><i>From a spring to a stream — LLM operating systems that flow.</i></p>
<p align="center"><b>🇩🇪 <a href="https://github.com/ellmos-ai/.github/blob/master/profile/README_de.md">Deutsche Version</a></b></p>

**ellmos** (XLLM-OS) is a family of text-based operating systems that empower Large Language Models to work autonomously, learn, and self-organize.

## The ellmos Family

Three operating systems — different philosophies, same goal:

<table>
<tr>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-bach.jpg" width="200"><br>
<b><a href="https://github.com/ellmos-ai/bach">BACH</a></b><br>
<i>The stream that unites everything</i><br>
Full LLM-OS: 109+ handlers, 932+ skills, agents, GUI
</td>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-rinnsal.jpg" width="200"><br>
<b><a href="https://github.com/ellmos-ai/rinnsal">Rinnsal</a></b><br>
<i>The trickle</i><br>
Lightweight LLM infra: memory, tasks, connectors, chains. Zero dependencies.
</td>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-gardener.jpg" width="200"><br>
<b><a href="https://github.com/ellmos-ai/gardener">gardener</a></b><br>
<i>The zen garden</i><br>
LLM-native OS: 1 table, 4 functions, FTS5 search. Everything is searchable.
</td>
</tr>
</table>

## Architecture: 3 OS Layers + Pluggable Modules

The ellmos ecosystem consists of **three OS layers** and **pluggable modules** that can be integrated into any OS — or used standalone.

### Operating Systems

| | **BACH** | **Rinnsal** | **gardener** |
|---|---|---|---|
| **Philosophy** | Maximalist: everything integrated | Lightweight: zero dependencies | Minimalist: 1 table, 4 functions |
| **Database** | SQLite (145+ tables) | SQLite (structured) | SQLite (1 table `everything` + FTS5) |
| **Memory** | 5-type cognitive model | Facts/Notes/Lessons/Sessions | Unified (memo/lesson/recall + decay) |
| **Tasks** | Full GTD (priority, deadline, tags) | Priority + Status + Agent assignment | type='task' in everything |
| **Tools** | 373+ specialized tools | CLI commands | 6 bridge+skin tools (extensible) |
| **Skills/Agents** | 932 skills, 5 boss agents, 28 experts | None | None (the LLM is the agent) |
| **Connectors** | Telegram, Email, WhatsApp | Telegram, Discord, Home Assistant | Planned (v0.2+) |
| **GUI** | PySide6 Desktop + Web | CLI only | CLI only |
| **Self-Extension** | `bach skills create` | No | No |
| **Codebase** | ~50,000+ lines | ~2,000 lines | ~1,600 lines |
| **Best for** | Power users, all-in-one | Developers wanting light infra | Minimalists, LLM-native experiments |

### Pluggable Modules

These modules can be integrated into any OS or used standalone:

| Module | Purpose | Key Feature |
|---|---|---|
| **[USMC](https://github.com/ellmos-ai/usmc)** | Cross-agent shared memory | Confidence-based conflict resolution, change tracking |
| **[clutch](https://github.com/ellmos-ai/clutch)** | Provider-neutral model routing | Auto-learning which model fits which task, budget zones |
| **[MarbleRun](https://github.com/ellmos-ai/MarbleRun)** | Chain orchestration | Autonomous multi-round agent loops with context handoff |
| **[swarm-ai](https://github.com/ellmos-ai/swarm-ai)** | Parallel LLM coordination | 5 patterns: Epstein, Hierarchy, Stigmergy, Consensus, Specialist |

### How They Fit Together

```
┌─────────────────────────────────────────────────┐
│              Choose Your OS Layer               │
│                                                 │
│   BACH (full)   Rinnsal (light)  gardener (min) │
│   ┌─────────┐   ┌────────────┐   ┌──────────┐  │
│   │ 932     │   │ Zero deps  │   │ 1 table   │  │
│   │ skills  │   │ Connectors │   │ 4 funcs   │  │
│   │ 5 boss  │   │ Chains     │   │ FTS5      │  │
│   │ agents  │   │ Events     │   │ = search  │  │
│   └────┬────┘   └─────┬──────┘   └─────┬────┘  │
│        └────────────┼─────────────────┘       │
│                       │                         │
│        ┌──────────────┼──────────────┐          │
│        │    Pluggable Modules        │          │
│        │                             │          │
│        │  USMC     ── shared memory  │          │
│        │  clutch   ── model routing  │          │
│        │  MarbleRun ── agent chains  │          │
│        │  swarm-ai ── parallel LLMs  │          │
│        └─────────────────────────────┘          │
└─────────────────────────────────────────────────┘
```

All projects: **Python 3.10+** | **SQLite** | **MIT License** | **Zero or minimal dependencies**

## Pluggable Skills

<table>
<tr>
<td align="center" width="100%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-skills.jpg" width="200"><br>
<b><a href="https://github.com/ellmos-ai/skills">skills</a></b><br>
<i>Pluggable Skill Library</i><br>
Reusable agent skills that slot into any ellmos OS.<br>
Development, research, education, infrastructure — pick what you need.
</td>
</tr>
</table>

---

## MCP Servers

<table>
<tr>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-ellmos-codecommander.jpg" width="160"><br>
<b><a href="https://github.com/ellmos-ai/ellmos-codecommander-mcp">CodeCommander</a></b><br>
Code analysis & refactoring<br>
<code>npm i -g ellmos-codecommander-mcp</code>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-ellmos-filecommander.jpg" width="160"><br>
<b><a href="https://github.com/ellmos-ai/ellmos-filecommander-mcp">FileCommander</a></b><br>
File management & batch ops<br>
<code>npm i -g ellmos-filecommander-mcp</code>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-clatcher.jpg" width="160"><br>
<b><a href="https://github.com/ellmos-ai/ellmos-clatcher-mcp">Clatcher</a></b><br>
Utility tools: file repair, format conversion, duplicate detection, batch operations<br>
<code>npm i -g ellmos-clatcher-mcp</code>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-n8n-manager-mcp.jpg" width="160"><br>
<b><a href="https://github.com/ellmos-ai/n8n-manager-mcp">n8n Manager</a></b><br>
n8n workflow automation<br>
<code>npm i -g n8n-manager-mcp</code>
</td>
</tr>
</table>

## Modules & More

| Project | Description |
|---|---|
| **[USMC](https://github.com/ellmos-ai/usmc)** | Cross-agent shared memory with confidence-based conflict resolution |
| **[clutch](https://github.com/ellmos-ai/clutch)** | Provider-neutral model routing with auto-learning and budget zones |
| **[MarbleRun](https://github.com/ellmos-ai/MarbleRun)** | Autonomous multi-round agent chains for Claude Code |
| **[swarm-ai](https://github.com/ellmos-ai/swarm-ai)** | 5 parallel LLM coordination patterns (Stigmergy, Consensus, ...) |
| **[n8n Workflow Manager](https://github.com/ellmos-ai/n8n-workflow-manager)** | Standalone GUI for n8n workflow creation |
| **[ellmos-stack](https://github.com/ellmos-ai/ellmos-stack)** | Self-hosted AI stack (Docker, Ollama, n8n) |
| **[skills](https://github.com/ellmos-ai/skills)** | Pluggable skill library (dev, research, education, infrastructure) |

## Legacy

<table>
<tr>
<td align="center" width="100%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-recludos.jpg" width="180"><br>
<b><a href="https://github.com/ellmos-ai/recludos-legacy">recludOS</a></b><br>
<i>Archived predecessor to BACH</i><br>
Historical reference
</td>
</tr>
</table>

---

**[Full documentation](https://github.com/ellmos-ai/ellmos)** | **License:** MIT
