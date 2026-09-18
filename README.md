# Phantoms AI - Week 2 Capstone Project

An integrated project combining Backend fundamentals, SQL databases, APIs, Webhooks, and Automation.

## Folder Structure
phantoms-ai-week2/
├── data/          # Contains the SQLite database (store.db)
├── src/           # Contains API, Webhook, and Pipeline logic
├── tests/         # Verification and test files
├── main.py        # Main execution entry point for automation
└── README.md      # Comprehensive project documentation

## Execution Steps
1. Install dependencies:
   `pip install requests`
2. Run the main automation pipeline:
   `python main.py`

## Engineering Decisions & Assumptions
- SQLite is used for local pipeline data storage inside the `data/` directory.
- A periodic automation cycle is implemented to fetch, store, and webhook data automatically.
