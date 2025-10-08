# Documentation

This folder contains helpful docs for the Slackbot Content Pipeline.

Project layout

- `app.py` - Flask app and Slack endpoints
- `slack_commands.py` - Command handlers for slash commands
- `utils/` - Reusable utilities: keyword processing, outline and idea generation, PDF report generation
- `supabase.sql` - Database schema for keywords, clusters, reports
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker image for the app

Getting started

1. Copy `.env.example` to `.env` and fill in secrets.
2. Create a virtual environment and install dependencies:

   python -m venv .venv; .venv\Scripts\Activate; pip install -r requirements.txt

3. Run locally:

   python app.py

Notes

- The utils are lightweight stubs to get you started. Replace OpenAI and web search stubs with your preferred integrations.
- Add unit tests and CI as next steps.
