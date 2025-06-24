# modules/report.py
from fpdf import FPDF
import datetime
import os

def generate_pdf(output_path="report.pdf", user="Unknown", score=0.0, verdict="Unknown", message_file=None):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    pdf.set_text_color(0, 0, 0)
    pdf.cell(200, 10, txt="PersonaFence Impersonation Detection Report", ln=True, align='C')

    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"🕵️ Checked User: {user}", ln=True)
    pdf.cell(200, 10, txt=f"📄 Source File: {message_file}", ln=True)
    pdf.cell(200, 10, txt=f"📊 Match Score: {score:.2f}%", ln=True)
    pdf.cell(200, 10, txt=f"🧠 Verdict: {verdict}", ln=True)
    pdf.cell(200, 10, txt=f"📅 Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    if message_file and os.path.exists(message_file):
        pdf.ln(10)
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(200, 10, txt="Suspicious Message Content:", ln=True)
        pdf.set_font("Arial", size=11)
        pdf.ln(5)
        with open(message_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip():
                    pdf.multi_cell(0, 10, txt=line.strip())

    pdf.output(output_path)
    print(f"[📄] PDF report generated: {output_path}")
