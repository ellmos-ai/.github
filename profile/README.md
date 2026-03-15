<p align="center">
  <img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/ellmos-logo.jpg" alt="ellmos logo" width="300">
</p>

<h3 align="center">Extra Large Language Model Operating Systems</h3>
<p align="center"><i>From a spring to a stream -- LLM operating systems that flow.</i></p>

**ellmos** (XLLM-OS) is a family of text-based operating systems that empower Large Language Models to work autonomously, learn, and self-organize.

## The ellmos Family

All projects follow a **water metaphor** -- growing from a spring to a stream:

<table>
<tr>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-usmc.jpg" width="200"><br>
<b><a href="https://github.com/ellmos-ai/usmc">USMC</a></b><br>
<i>The spring</i><br>
Shared memory for multi-agent coordination
</td>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-rinnsal.jpg" width="200"><br>
<b><a href="https://github.com/ellmos-ai/rinnsal">Rinnsal</a></b><br>
<i>The trickle</i><br>
USMC + LLM chain orchestration
</td>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-bach.jpg" width="200"><br>
<b><a href="https://github.com/ellmos-ai/bach">BACH</a></b><br>
<i>The stream that unites everything</i><br>
Full LLM-OS: 109+ handlers, 932+ skills, agents, GUI
</td>
</tr>
</table>

## MCP Servers & Tools

<table>
<tr>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-bach-codecommander.jpg" width="180"><br>
<b><a href="https://github.com/ellmos-ai/ellmos-codecommander-mcp">CodeCommander</a></b><br>
Code analysis & refactoring<br>
<code>npm i -g bach-codecommander-mcp</code>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-bach-filecommander.jpg" width="180"><br>
<b><a href="https://github.com/ellmos-ai/ellmos-filecommander-mcp">FileCommander</a></b><br>
File management & batch ops<br>
<code>npm i -g bach-filecommander-mcp</code>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-n8n-manager-mcp.jpg" width="180"><br>
<b><a href="https://github.com/ellmos-ai/n8n-manager-mcp">n8n Manager</a></b><br>
n8n workflow automation<br>
<code>npm i -g n8n-manager-mcp</code>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-marblerun.jpg" width="180"><br>
<b><a href="https://github.com/ellmos-ai/MarbleRun">MarbleRun</a></b><br>
Autonomous agent chains<br>
for Claude Code
</td>
</tr>
</table>

## More

<table>
<tr>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-n8n-workflow-manager.jpg" width="200"><br>
<b><a href="https://github.com/ellmos-ai/n8n-workflow-manager">n8n Workflow Manager</a></b><br>
Standalone GUI for n8n workflow creation
</td>
<td align="center" width="33%">
<b><a href="https://github.com/ellmos-ai/gardener">Gardener</a></b><br>
<i>The zen garden</i><br>
LLM-native OS: 1 table, 4 functions, FTS5 search
</td>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-recludos.jpg" width="200"><br>
<b><a href="https://github.com/ellmos-ai/recludos-legacy">recludOS</a></b><br>
<i>Archived predecessor to BACH</i><br>
Historical reference
</td>
</tr>
</table>

## Architecture: 3 Operating Systems + Pluggable Modules

The ellmos ecosystem consists of **three OS layers** (different philosophies, same goal) and **four pluggable modules** that can be integrated into any OS.

### Operating Systems

| | **BACH** | **Gardener** | **Rinnsal** |
|---|---|---|---|
| **Philosophy** | Maximalist: everything integrated | Minimalist: 1 table, 4 functions | Lightweight: zero dependencies |
| **Database** | SQLite (145+ tables) | SQLite (1 table `everything` + FTS5) | SQLite (structured) |
| **Memory** | 5-type cognitive model | Unified (memo/lesson/recall + decay) | Facts/Notes/Lessons/Sessions |
| **Tasks** | Full GTD (priority, deadline, tags) | type='task' in everything | Priority + Status + Agent assignment |
| **Tools** | 373+ specialized tools | 6 bridge+skin tools (extensible) | CLI commands |
| **Skills/Agents** | 932 skills, 5 boss agents, 28 experts | None (the LLM is the agent) | None |
| **Connectors** | Telegram, Email, WhatsApp | Planned (v0.2+) | Telegram, Discord, Home Assistant |
| **GUI** | PySide6 Desktop + Web | CLI only | CLI only |
| **Self-Extension** | `bach skills create` | No | No |
| **MCP** | 2 servers (CodeCommander, FileCommander) | Planned (v0.3+) | No |
| **Codebase** | ~50,000+ lines | ~1,600 lines | ~2,000 lines |
| **Best for** | Power users, all-in-one | Minimalists, LLM-native experiments | Developers wanting light infra |

### Pluggable Modules

These modules can be integrated into any OS or used standalone:

| Module | Purpose | Key Feature |
|---|---|---|
| **[clutch](https://github.com/ellmos-ai/clutch)** | Provider-neutral model routing | Auto-learning which model fits which task, budget zones |
| **[MarbleRun](https://github.com/ellmos-ai/MarbleRun)** | Chain orchestration | Autonomous multi-round agent loops with context handoff |
| **[swarm-ai](https://github.com/ellmos-ai/swarm-ai)** | Parallel LLM coordination | 5 patterns: Epstein, Hierarchy, Stigmergy, Consensus, Specialist |
| **[USMC](https://github.com/ellmos-ai/usmc)** | Cross-agent shared memory | Confidence-based conflict resolution, change tracking |

### How They Fit Together

```
┌─────────────────────────────────────────────────┐
│              Choose Your OS Layer               │
│                                                 │
│   BACH (full)   Gardener (minimal)   Rinnsal    │
│   ┌─────────┐   ┌──────────────┐   ┌────────┐  │
│   │ 932     │   │ 1 table      │   │ Zero   │  │
│   │ skills  │   │ 4 functions  │   │ deps   │  │
│   │ 5 boss  │   │ FTS5 search  │   │ Events │  │
│   │ agents  │   │ = everything │   │ + LLM  │  │
│   └────┬────┘   └──────┬───────┘   └───┬────┘  │
│        └───────────────┼────────────────┘       │
│                        │                        │
│         ┌──────────────┼──────────────┐         │
│         │    Pluggable Modules        │         │
│         │                             │         │
│         │  clutch   ── model routing  │         │
│         │  MarbleRun ── agent chains  │         │
│         │  swarm-ai ── parallel LLMs  │         │
│         │  USMC     ── shared memory  │         │
│         └─────────────────────────────┘         │
└─────────────────────────────────────────────────┘
```

All projects: **Python 3.10+** | **SQLite** | **MIT License** | **Zero or minimal dependencies**

---

**[Full documentation](https://github.com/ellmos-ai/ellmos)** | **License:** MIT
