# slack_commands.py
# Minimal command handler for slash commands. Expand per your workflow.

from typing import Dict
from utils.idea_generator import generate_ideas
from utils.outline_generator import generate_outline
from utils.report_generator import create_pdf_report
import os


def handle_command(command: str, text: str, user_id: str) -> Dict:
    """Return a JSON-serializable payload to respond to Slack.

    This function keeps behavior simple:
      - /ideas <topic> -> returns a list of ideas
      - /outline <topic> -> returns an outline
      - /report <title>|<section1,section2,...> -> generates a PDF and returns path
    """
    if not command:
        return {"text": "No command provided."}

    cmd = command.lstrip("/")
    if cmd == "ideas":
        ideas = generate_ideas(text or "topic")
        return {"response_type": "ephemeral", "text": "\n".join(f"- {i}" for i in ideas)}

    if cmd == "outline":
        outline = generate_outline(text or "topic")
        out_text = f"*{outline['title']}*\n" + "\n".join(f"- {s}" for s in outline["sections"])
        return {"response_type": "ephemeral", "text": out_text}

    if cmd == "report":
        # text expected: title|section1,section2
        parts = (text or "").split("|", 1)
        title = parts[0] if parts else "Report"
        sections = parts[1].split(",") if len(parts) > 1 else ["Overview"]
        out_dir = os.getenv("REPORT_DIR", ".")
        safe_name = title.replace(" ", "_")[:60]
        out_path = os.path.join(out_dir, f"{safe_name}.pdf")
        create_pdf_report(title, sections, out_path)
        return {"response_type": "ephemeral", "text": f"Report created: {out_path}", "filepath": out_path}

    return {"response_type": "ephemeral", "text": f"Unknown command: {command}"}
