<p align="center">
  <img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/ellmos-logo.jpg" alt="ellmos Logo" width="300">
</p>

<h3 align="center">Extra Large Language Model Operating Systems</h3>
<p align="center"><i>Von der Quelle zum Strom — LLM-Betriebssysteme die fließen.</i></p>
<p align="center"><b>🇬🇧 <a href="README.md">English Version</a></b> (maßgeblich)</p>

> **Hinweis:** Die englische Version dieser Seite ist die maßgebliche Referenz. Diese deutsche Übersetzung kann veraltet sein. Im Zweifelsfall gilt die [englische Version](README.md).

**ellmos** (XLLM-OS) ist eine Familie textbasierter Betriebssysteme, die Large Language Models befähigen, autonom zu arbeiten, zu lernen und sich selbst zu organisieren.

## Einstieg

| Du möchtest... | Starte mit |
|---|---|
| Ein vollständiges persönliches LLM-Betriebssystem mit GUI, Memory, Tools und Agenten nutzen | **[BACH](https://github.com/ellmos-ai/bach)** |
| Leichtgewichtige lokale Memory-, Task- und Connector-Infrastruktur in ein Agentenprojekt einbauen | **[Rinnsal](https://github.com/ellmos-ai/rinnsal)** |
| Mit einem minimalen, durchsuchbaren LLM-nativen OS-Kern experimentieren | **[gardener](https://github.com/ellmos-ai/gardener)** |
| Claude Desktop oder andere MCP-Clients mit lokalen Datei-, Code-, n8n- oder Profilwerkzeugen erweitern | **[MCP-Server](#mcp-server)** |
| Agenten-Skills, Shared Memory, Routing oder Schwarmmuster im eigenen Stack wiederverwenden | **[Steckbare Module](#steckbare-module)** und **[skills](https://github.com/ellmos-ai/skills)** |

Für maschinenlesbaren Ökosystem-Kontext siehe **[llms.txt](https://github.com/ellmos-ai/.github/blob/master/llms.txt)**.

## Öffentliches Repository-Verzeichnis

Dieses Verzeichnis ist vollständig für die öffentlichen `ellmos-ai`-Repositories. Archivierte Repositories sind ausdrücklich markiert.

| Bereich | Repositories |
|---|---|
| Organisationsprofil | **[.github](https://github.com/ellmos-ai/.github)** - Org-Profil, Community-Health-Dateien und `llms.txt` |
| LLM-Betriebssysteme | **[bach](https://github.com/ellmos-ai/bach)**, **[rinnsal](https://github.com/ellmos-ai/rinnsal)**, **[gardener](https://github.com/ellmos-ai/gardener)**, **[ellmos](https://github.com/ellmos-ai/ellmos)** |
| MCP-Server | **[ellmos-codecommander-mcp](https://github.com/ellmos-ai/ellmos-codecommander-mcp)**, **[ellmos-filecommander-mcp](https://github.com/ellmos-ai/ellmos-filecommander-mcp)**, **[ellmos-clatcher-mcp](https://github.com/ellmos-ai/ellmos-clatcher-mcp)**, **[n8n-manager-mcp](https://github.com/ellmos-ai/n8n-manager-mcp)**, **[ellmos-controlcenter-mcp](https://github.com/ellmos-ai/ellmos-controlcenter-mcp)**, **[ellmos-homebase-mcp](https://github.com/ellmos-ai/ellmos-homebase-mcp)**, **[ellmos-servercommander-mcp](https://github.com/ellmos-ai/ellmos-servercommander-mcp)** |
| Agenten-Module und Orchestrierung | **[usmc](https://github.com/ellmos-ai/usmc)**, **[clutch](https://github.com/ellmos-ai/clutch)**, **[MarbleRun](https://github.com/ellmos-ai/MarbleRun)**, **[swarm-ai](https://github.com/ellmos-ai/swarm-ai)**, **[n8n-workflow-manager](https://github.com/ellmos-ai/n8n-workflow-manager)**, **[ellmos-stack](https://github.com/ellmos-ai/ellmos-stack)**, **[skills](https://github.com/ellmos-ai/skills)** |
| Evaluation und Wartung | **[ellmos-tests](https://github.com/ellmos-ai/ellmos-tests)** |
| Legacy-Archiv | **[recludos-legacy](https://github.com/ellmos-ai/recludos-legacy)** - archivierter Vorgänger von BACH |

## Die ellmos-Familie

Drei Betriebssysteme — verschiedene Philosophien, selbes Ziel:

<table>
<tr>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-bach.jpg" width="200"><br>
<b><a href="https://github.com/ellmos-ai/bach">BACH</a></b><br>
<i>Der Strom der alles vereint</i><br>
Volles LLM-OS: 113+ Handler, 1870+ Skills, Agenten, GUI
</td>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-rinnsal.jpg" width="200"><br>
<b><a href="https://github.com/ellmos-ai/rinnsal">Rinnsal</a></b><br>
<i>Das Rinnsal</i><br>
Leichtgewichtige LLM-Infrastruktur: Memory, Tasks, Connectors, Chains. Keine Abhängigkeiten.
</td>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-gardener.jpg" width="200"><br>
<b><a href="https://github.com/ellmos-ai/gardener">gardener</a></b><br>
<i>Der Zen-Garten</i><br>
LLM-natives OS: 1 Tabelle, 4 Funktionen, FTS5-Suche. Alles ist durchsuchbar.
</td>
</tr>
</table>

## Architektur: 3 OS-Schichten + steckbare Module

Das ellmos-Ökosystem besteht aus **drei OS-Schichten** und **steckbaren Modulen**, die in jedes OS integriert — oder eigenständig genutzt werden können.

### Betriebssysteme

| | **BACH** | **Rinnsal** | **gardener** |
|---|---|---|---|
| **Philosophie** | Maximalistisch: alles integriert | Leichtgewichtig: keine Abhängigkeiten | Minimalistisch: 1 Tabelle, 4 Funktionen |
| **Datenbank** | SQLite (145+ Tabellen) | SQLite (strukturiert) | SQLite (1 Tabelle `everything` + FTS5) |
| **Memory** | 5-Typen kognitives Modell | Facts/Notes/Lessons/Sessions | Vereinheitlicht (memo/lesson/recall + Decay) |
| **Tasks** | Volles GTD (Priorität, Deadline, Tags) | Priorität + Status + Agent-Zuweisung | type='task' in everything |
| **Tools** | 550+ spezialisierte Tools | CLI-Befehle | 6 Bridge+Skin-Tools (erweiterbar) |
| **Skills/Agenten** | 1870+ Skills, 5 Boss-Agenten, 28 Experten | Keine | Keine (das LLM ist der Agent) |
| **Connectors** | Telegram, E-Mail, WhatsApp | Telegram, Discord, Home Assistant | Geplant (v0.2+) |
| **GUI** | PySide6 Desktop + Web | Nur CLI | Nur CLI |
| **Selbsterweiterung** | `bach skills create` | Nein | Nein |
| **Codebasis** | ~50.000+ Zeilen | ~2.000 Zeilen | ~1.600 Zeilen |
| **Ideal für** | Power-User, All-in-one | Entwickler die leichte Infra wollen | Minimalisten, LLM-native Experimente |

### Steckbare Module

Diese Module können in jedes OS integriert oder eigenständig genutzt werden:

| Modul | Zweck | Kernfeature |
|---|---|---|
| **[USMC](https://github.com/ellmos-ai/usmc)** | Agentenübergreifendes Shared Memory | Konfidenzbasierte Konfliktlösung, Änderungstracking |
| **[clutch](https://github.com/ellmos-ai/clutch)** | Anbieter-neutrales Modell-Routing | Auto-Learning welches Modell zu welcher Aufgabe passt, Budget-Zonen |
| **[MarbleRun](https://github.com/ellmos-ai/MarbleRun)** | Chain-Orchestrierung | Autonome Multi-Runden-Agenten-Schleifen mit Kontext-Übergabe |
| **[swarm-ai](https://github.com/ellmos-ai/swarm-ai)** | Parallele LLM-Koordination | 5 Muster: Epstein, Hierarchie, Stigmergie, Konsens, Spezialist |

### Wie alles zusammenpasst

```
┌─────────────────────────────────────────────────┐
│              Wähle deine OS-Schicht              │
│                                                 │
│   BACH (voll)   Rinnsal (leicht)  gardener (min) │
│   ┌─────────┐   ┌────────────┐   ┌──────────┐  │
│   │ 1870+   │   │ Keine Deps │   │ 1 Tabelle │  │
│   │ Skills  │   │ Connectors │   │ 4 Funkt.  │  │
│   │ 5 Boss  │   │ Chains     │   │ FTS5      │  │
│   │ Agenten │   │ Events     │   │ = Suche   │  │
│   └────┬────┘   └─────┬──────┘   └─────┬────┘  │
│        └────────────┼─────────────────┘       │
│                       │                         │
│        ┌──────────────┼──────────────┐          │
│        │    Steckbare Module         │          │
│        │                             │          │
│        │  USMC     ── Shared Memory  │          │
│        │  clutch   ── Modell-Routing │          │
│        │  MarbleRun ── Agent-Chains  │          │
│        │  swarm-ai ── Parallele LLMs │          │
│        └─────────────────────────────┘          │
└─────────────────────────────────────────────────┘
```

Alle Projekte: **Python 3.10+** | **SQLite** | **MIT-Lizenz** | **Keine oder minimale Abhängigkeiten**

## Steckbare Skills

<table>
<tr>
<td align="center" width="100%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-skills.jpg" width="200"><br>
<b><a href="https://github.com/ellmos-ai/skills">skills</a></b><br>
<i>Steckbare Skill-Bibliothek</i><br>
Wiederverwendbare Agenten-Skills die sich in jedes ellmos-OS einfügen.<br>
Entwicklung, Forschung, Bildung, Infrastruktur — nimm was du brauchst.
</td>
</tr>
</table>

---

## MCP-Server

<table>
<tr>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-ellmos-codecommander.jpg" width="160"><br>
<b><a href="https://github.com/ellmos-ai/ellmos-codecommander-mcp">CodeCommander</a></b><br>
Code-Analyse & Refactoring<br>
<code>npm i -g ellmos-codecommander-mcp</code>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-ellmos-filecommander.jpg" width="160"><br>
<b><a href="https://github.com/ellmos-ai/ellmos-filecommander-mcp">FileCommander</a></b><br>
Dateiverwaltung & Batch-Operationen<br>
<code>npm i -g ellmos-filecommander-mcp</code>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-clatcher.jpg" width="160"><br>
<b><a href="https://github.com/ellmos-ai/ellmos-clatcher-mcp">Clatcher</a></b><br>
Hilfswerkzeuge: Dateireparatur, Formatkonvertierung, Duplikaterkennung, Batch-Operationen<br>
<code>npm i -g ellmos-clatcher-mcp</code>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-n8n-manager-mcp.jpg" width="160"><br>
<b><a href="https://github.com/ellmos-ai/n8n-manager-mcp">n8n Manager</a></b><br>
n8n Workflow-Automatisierung<br>
<code>npm i -g n8n-manager-mcp</code>
</td>
</tr>
<tr>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-ellmos-controlcenter.jpg" width="160"><br>
<b><a href="https://github.com/ellmos-ai/ellmos-controlcenter-mcp">ControlCenter</a></b><br>
MCP-Profil-Dashboard, Fähigkeits-Bundles & Rechte-Audits<br>
<code>npm i -g ellmos-controlcenter-mcp</code>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-ellmos-homebase.jpg" width="293"><br>
<b><a href="https://github.com/ellmos-ai/ellmos-homebase-mcp">Homebase</a></b><br>
Lokales LLM-Memory, Wissen, State & Orchestrierung<br>
<code>npm i -g ellmos-homebase-mcp</code>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-ellmos-servercommander.jpg" width="160"><br>
<b><a href="https://github.com/ellmos-ai/ellmos-servercommander-mcp">ServerCommander</a></b><br>
Server-Health-Checks, Log-Analyse, Deploy-Dry-runs & Mail-Status<br>
<code>npm i -g ellmos-servercommander-mcp</code>
</td>
<td width="25%"></td>
</tr>
</table>

## Module & Mehr

| Projekt | Beschreibung |
|---|---|
| **[USMC](https://github.com/ellmos-ai/usmc)** | Agentenübergreifendes Shared Memory mit konfidenzbasierter Konfliktlösung |
| **[clutch](https://github.com/ellmos-ai/clutch)** | Anbieter-neutrales Modell-Routing mit Auto-Learning und Budget-Zonen |
| **[MarbleRun](https://github.com/ellmos-ai/MarbleRun)** | Autonome Multi-Runden-Agenten-Chains für Claude Code |
| **[swarm-ai](https://github.com/ellmos-ai/swarm-ai)** | 5 parallele LLM-Koordinationsmuster (Stigmergie, Konsens, ...) |
| **[n8n Workflow Manager](https://github.com/ellmos-ai/n8n-workflow-manager)** | Eigenständige GUI für n8n-Workflow-Erstellung |
| **[ellmos-stack](https://github.com/ellmos-ai/ellmos-stack)** | Selbst gehosteter KI-Stack (Docker, Ollama, n8n) |
| **[skills](https://github.com/ellmos-ai/skills)** | Steckbare Skill-Bibliothek (Entwicklung, Forschung, Bildung, Infrastruktur) |

## Legacy

<table>
<tr>
<td align="center" width="100%">
<img src="https://raw.githubusercontent.com/ellmos-ai/.github/master/profile/logo-recludos.jpg" width="180"><br>
<b><a href="https://github.com/ellmos-ai/recludos-legacy">recludOS</a></b><br>
<i>Archivierter Vorgänger von BACH</i><br>
Historische Referenz
</td>
</tr>
</table>

---

**[Vollständige Dokumentation](https://github.com/ellmos-ai/ellmos)** | **Lizenz:** MIT
