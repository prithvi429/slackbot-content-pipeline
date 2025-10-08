from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime


def create_pdf_report(title: str, sections: list, out_path: str):
    """Create a simple PDF report with title and section headings."""
    c = canvas.Canvas(out_path, pagesize=letter)
    width, height = letter
    y = height - 72

    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, y, title)
    c.setFont("Helvetica", 10)
    c.drawString(72, y - 18, f"Generated: {datetime.utcnow().isoformat()}Z")

    y -= 48
    for sec in sections:
        if y < 96:
            c.showPage()
            y = height - 72
        c.setFont("Helvetica-Bold", 12)
        c.drawString(72, y, sec)
        y -= 18

    c.save()
    return out_path
