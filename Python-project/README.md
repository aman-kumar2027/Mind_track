I# MindTrack-CLI

> An offline, beginner-friendly command-line app for journaling, mood tracking and stress self-checks. Your data never leaves your computer.

**VITyarthi - Build Your Own Project**

| | |
|---|---|
| **Author** | _Aman Kumar_ |
| **Registration No.** | _26BCE10427_ |
| **Course** | _CSE CORE and CSE1021_ |
| **Language** | Python 3 (developed with 3.13), standard library only |

---

## Table of Contents

1. [Quick Navigation](#quick-navigation)
2. [Overview](#overview)
3. [Features](#features)
4. [Technologies / Tools Used](#technologies--tools-used)
5. [Project Structure](#project-structure)
6. [Install and Run](#install-and-run)
7. [How to Use](#how-to-use)
8. [Data Files and Formats](#data-files-and-formats)
9. [Screenshots](#screenshots)
10. [Instructions for Testing](#instructions-for-testing)
11. [Design Documentation](#design-documentation)
12. [Known Limitations](#known-limitations)
13. [Future Enhancements](#future-enhancements)
14. [Troubleshooting](#troubleshooting)

---

## Quick Navigation

Looking for something specific? Start here.

| I want to... | Go to |
|---|---|
| Run the app | [`mindtrack.py`](mindtrack.py) and [Install and Run](#install-and-run) |
| Read the problem statement, scope and target users | [`statement.md`](statement.md) |
| Read the full project report | [`docs/MindTrack-CLI_Section6_Project_Report.pdf`](docs/MindTrack-CLI_Section6_Project_Report.pdf) (Word version: [`.docx`](docs/MindTrack-CLI_Section6_Project_Report.docx)) |
| See requirements, UML and storage design | [`docs/MindTrack-CLI_Section4_Design_and_Documentation.pdf`](docs/MindTrack-CLI_Section4_Design_and_Documentation.pdf) (Word version: [`.docx`](docs/MindTrack-CLI_Section4_Design_and_Documentation.docx)) |
| Look at the diagrams | [`docs/diagrams/`](docs/diagrams/) |
| See how the app looks | [`docs/screenshots/`](docs/screenshots/) or [Screenshots](#screenshots) |
| See my saved journal / mood data | [`journal.txt`](journal.txt), [`mood.csv`](mood.csv) |
| Test the project | [Instructions for Testing](#instructions-for-testing) |

---

## Overview

MindTrack is a simple Python project that helps people keep track of their emotional well-being from the terminal. Users can write journal entries, log their mood for the day, receive positive affirmations and take a short stress-level quiz.

All information is stored locally in `.txt` and `.csv` files, so the app is light, private and easy to launch: there is nothing to install beyond Python itself.

**Who is it for?**

- Students who feel stressed by academic and personal-life problems.
- People with privacy concerns who want to keep their thoughts stored locally.

For the full problem statement and scope, see [`statement.md`](statement.md).

> **Note:** MindTrack-CLI is a self-reflection aid. The stress questionnaire is a simple, non-clinical check and is **not** a medical diagnosis.

---

## Features

- **Journal:** write dated journal entries and read them back.
- **Mood log:** record how you feel each day (happy / sad / anxious / neutral / angry) and view your history.
- **Positive affirmations:** get a random encouraging message whenever you want one.
- **Stress questionnaire:** five quick questions that give a Low / Moderate / High result with advice.
- **Fully offline:** no internet, no accounts, no third-party packages.
- **Local storage:** data lives in plain `.txt` and `.csv` files that you can open in any editor or spreadsheet.
- **Simple CLI:** a numbered menu that works right in the terminal.

---

## Technologies / Tools Used

| Tool | Purpose |
|---|---|
| Python 3 (developed with 3.13) | Programming language |
| `.txt` file | Journal storage |
| `.csv` file and the `csv` module | Mood storage |
| `datetime` module | Date stamps |
| `random` module | Picking affirmations |
| Git and GitHub | Version control and submission |

---

## Project Structure

```text
MindTrack-CLI/
│
├── README.md                 <- You are here: overview, setup, testing, navigation
├── statement.md              <- Problem statement, scope, target users, high-level features
│
├── mindtrack.py              <- The application (menu + all features)
├── journal.txt               <- Journal data (created automatically on first entry)
├── mood.csv                  <- Mood data (created automatically on first mood log)
│
└── docs/                     <- Everything that documents the project
    ├── MindTrack-CLI_Section6_Project_Report.pdf      <- Full project report
    ├── MindTrack-CLI_Section6_Project_Report.docx     <- Same report, editable
    ├── MindTrack-CLI_Section4_Design_and_Documentation.pdf
    ├── MindTrack-CLI_Section4_Design_and_Documentation.docx
    │
    ├── diagrams/             <- Design diagrams (PNG)
    │   ├── 01-architecture.png
    │   ├── 02-workflow.png
    │   ├── 03-use-case.png
    │   ├── 04-component.png
    │   ├── 05-sequence-journal.png
    │   ├── 06-sequence-mood.png
    │   ├── 07-sequence-stress.png
    │   └── 08-er-diagram.png
    │
    └── screenshots/          <- Terminal screenshots used in this README and the report
        ├── 01-main-menu.png
        ├── 02-journal.png
        ├── 03-mood.png
        ├── 04-affirmation-and-stress.png
        └── 05-error-handling.png
```

### What each file does

| Path | Type | Description |
|---|---|---|
| [`mindtrack.py`](mindtrack.py) | Source code | Complete app: file-path constants, feature functions and the main menu loop |
| [`journal.txt`](journal.txt) | Data | One line per entry: `YYYY-MM-DD - text` |
| [`mood.csv`](mood.csv) | Data | One row per mood log: `date,mood` (no header row) |
| [`statement.md`](statement.md) | Documentation | Problem statement, scope, target users, features |
| [`docs/`](docs/) | Documentation | Project report, design document, diagrams and screenshots |

### Inside `mindtrack.py`

| Menu option | Function | Reads / writes |
|---|---|---|
| 1. Write Journal Entry | `write_journal()` | appends to `journal.txt` |
| 2. View Journal Entries | `view_journal()` | reads `journal.txt` |
| 3. Log Mood | `log_mood()` | appends to `mood.csv` |
| 4. View Mood Entries | `view_mood_entries()` | reads `mood.csv` |
| 5. Get Positive Affirmation | `give_affirmation()` | none (built-in list) |
| 6. Take Stress Questionnaire | `stress_test()` | none (result is shown, not stored) |
| 7. Exit | `main()` | none |

---

## Install and Run

**Requirements:** Python 3.8 or newer (developed with 3.13). No other packages are needed.

1. **Get the project**

   ```bash
   git clone <your-repository-url>
   cd MindTrack-CLI
   ```

   Or download the repository as a ZIP from GitHub, extract it and open the folder.

2. **Check that Python is installed**

   ```bash
   python --version
   ```

   On macOS/Linux you may need `python3 --version`. Install Python from <https://www.python.org/downloads/> if it is missing.

3. **Run the program from inside the project folder**

   ```bash
   python mindtrack.py
   ```

   (macOS/Linux: `python3 mindtrack.py`)

4. **Follow the on-screen instructions.** Type a number from 1 to 7 and press Enter.

> **Tip:** always start the program from the project folder. `journal.txt` and `mood.csv` are created in the folder you run it from, so running it elsewhere creates separate, empty data files.

---

## How to Use

```text
===== MindTrack CLI =====

1. Write Journal Entry
2. View Journal Entries
3. Log Mood
4. View Mood Entries
5. Get Positive Affirmation
6. Take Stress Questionnaire
7. Exit
```

- **Journal (1, 2):** type your thoughts and press Enter; the entry is saved with today's date. Choose 2 to read everything you have written.
- **Mood (3, 4):** type one of `happy`, `sad`, `anxious`, `neutral` or `angry`. Choose 4 to see your history.
- **Affirmation (5):** shows one random encouraging message.
- **Stress questionnaire (6):** answer five statements from **1 (Never)** to **5 (Always)**. The total (5 to 25) is classified as:

  | Total score | Result |
  |---|---|
  | 5 - 10 | Low stress |
  | 11 - 18 | Moderate stress |
  | 19 - 25 | High stress |

- **Exit (7):** quits the program. Your data stays in the files for next time.

---

## Data Files and Formats

Both files are plain text, so you can back them up, open them in Notepad, VS Code or Excel, or delete them to start fresh.

**`journal.txt`** - one entry per line

```text
2025-11-23 - feeling happy today
```

**`mood.csv`** - one row per log, no header

```text
2025-11-23,happy
```

Privacy note: the files are **not encrypted**. They stay on your device, but anyone with access to your computer can read them. Keep your device secure, and do not commit personal entries to a public GitHub repository (see the tip under [Known Limitations](#known-limitations)).

---


## Instructions for Testing

MindTrack-CLI is tested manually. For a clean test, run from an empty folder that contains only `mindtrack.py` (delete or move `journal.txt` and `mood.csv` first).

| # | Test | Steps | Expected output |
|---|---|---|---|
| 1 | Write a journal entry | Menu 1, type any text | "Entry saved!" and a new line `YYYY-MM-DD - text` in `journal.txt` |
| 2 | View journal entries | Menu 2 | All saved entries are displayed |
| 3 | Log a mood | Menu 3, type `anxious` | "Mood saved!" and a new row `date,anxious` in `mood.csv` |
| 4 | Mood is stored in lower case | Menu 3, type `HAPPY` | Stored as `happy` |
| 5 | View mood log | Menu 4 | Each row shown as `date → mood` |
| 6 | Affirmation | Menu 5 | One affirmation is displayed |
| 7 | Stress: low | Menu 6, answer `2 3 2 2 1` (total 10) | "Low Stress" |
| 8 | Stress: moderate | Menu 6, answer `3 3 3 3 3` (total 15) | "Moderate Stress" |
| 9 | Stress: high | Menu 6, answer `4 4 4 4 3` (total 19) | "High Stress" |
| 10 | Invalid menu option | Enter `9` | "Invalid option. Try again." and the menu appears again |
| 11 | Missing data files | Delete both data files, then menu 2 and 4 | "No entries found yet." / "No mood entries found." |
| 12 | Exit | Menu 7 | Goodbye message and the program ends |

**Quick smoke test (macOS/Linux).** This sends a scripted sequence of choices: write an entry, view journal, exit. It appends one line to `journal.txt`.

```bash
printf '1\nHello MindTrack\n2\n7\n' | python3 mindtrack.py
```

The full test results (10 of 13 test cases passing, with the 3 exceptions explained) are in section 11 of the [project report](docs/MindTrack-CLI_Section6_Project_Report.pdf).

---

## Design Documentation

| Document | Contents |
|---|---|
| [Project report (PDF)](docs/MindTrack-CLI_Section6_Project_Report.pdf) | Introduction, requirements, architecture, diagrams, design decisions, implementation, results, testing, challenges, learnings, future work, references |
| [Design and documentation (PDF)](docs/MindTrack-CLI_Section4_Design_and_Documentation.pdf) | Problem statement, objectives, functional and non-functional requirements, architecture, workflow, UML, storage design |

| Diagram | File |
|---|---|
| System architecture | [`docs/diagrams/01-architecture.png`](docs/diagrams/01-architecture.png) |
| Workflow | [`docs/diagrams/02-workflow.png`](docs/diagrams/02-workflow.png) |
| Use case | [`docs/diagrams/03-use-case.png`](docs/diagrams/03-use-case.png) |
| Component | [`docs/diagrams/04-component.png`](docs/diagrams/04-component.png) |
| Sequence: journal | [`docs/diagrams/05-sequence-journal.png`](docs/diagrams/05-sequence-journal.png) |
| Sequence: mood | [`docs/diagrams/06-sequence-mood.png`](docs/diagrams/06-sequence-mood.png) |
| Sequence: stress questionnaire | [`docs/diagrams/07-sequence-stress.png`](docs/diagrams/07-sequence-stress.png) |
| ER diagram | [`docs/diagrams/08-er-diagram.png`](docs/diagrams/08-er-diagram.png) |

---

## Known Limitations

- A non-numeric answer in the stress questionnaire (for example `abc`) stops the program with a `ValueError`.
- A blank or malformed row in `mood.csv` stops the mood view with an `IndexError`.
- Mood words outside the suggested five (for example `excited`) are accepted and stored.
- Data files are plain text and not encrypted.
- The stress questionnaire result is not saved, so there is no history of scores.

> **Tip for GitHub:** `journal.txt` and `mood.csv` hold personal entries. Before publishing a repository, replace them with sample data or add them to a `.gitignore` file.

---

## Future Enhancements

- Input validation loops for quiz answers and moods, and skipping bad CSV rows.
- Splitting the code into modules (journal, mood, affirmations, stress, storage) with a `tests/` folder and automated unit tests.
- Mood summaries and trends (counts per mood, weekly view, streaks).
- Search, edit and delete for journal entries.
- Saving dated stress-test results.
- Optional password protection or encryption of the data files.
- Error logging to a local log file.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `python` is not recognised | Install Python, or try `python3` (macOS/Linux) or `py` (Windows) |
| My entries seem to be missing | You probably ran the program from a different folder. Run it from the project folder so it finds `journal.txt` and `mood.csv` |
| The program closes with a `ValueError` | Enter only numbers from 1 to 5 in the stress questionnaire |
| Emoji or symbols look broken | Use a terminal that supports UTF-8 (Windows Terminal, VS Code terminal, macOS Terminal) |

---

_Made for the VITyarthi Build Your Own Project. MindTrack-CLI supports self-reflection only and is not a substitute for professional help. If you are struggling, please talk to someone you trust or a qualified professional._
