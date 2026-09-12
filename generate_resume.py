import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
import pypdf

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            super().showPage()
        super().save()

def generate_resume(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=28,
        bottomMargin=28
    )

    styles = getSampleStyleSheet()

    # Custom styles
    primary_color = colors.HexColor("#0f172a")  # Slate 900
    sec_color = colors.HexColor("#334155")      # Slate 700
    sub_color = colors.HexColor("#64748b")      # Slate 500
    accent_color = colors.HexColor("#0284c7")   # Sky 600

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=20,
        alignment=1, # Center
        textColor=primary_color
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        alignment=1, # Center
        textColor=sec_color
    )

    contact_style = ParagraphStyle(
        'DocContact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=10.5,
        alignment=1, # Center
        textColor=sub_color
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=primary_color,
        spaceBefore=0,
        spaceAfter=0
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=10.5,
        textColor=sec_color
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.0,
        leading=10.0,
        textColor=sec_color
    )

    tech_style = ParagraphStyle(
        'TechLine',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=9.8,
        textColor=colors.HexColor("#475569")
    )

    story = []

    # --- HEADER ---
    story.append(Paragraph("<b>ALLAN PAULRAJ V</b>", title_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Computer Science &amp; Engineering (AI &amp; ML) · Karunya Institute of Technology and Sciences", subtitle_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        "Coimbatore, India &nbsp;|&nbsp; +91 6374185190 &nbsp;|&nbsp; "
        '<a href="mailto:allanpaulraj2020@gmail.com" color="#0284c7"><u>allanpaulraj2020@gmail.com</u></a> &nbsp;|&nbsp; '
        '<a href="https://www.linkedin.com/in/allaneyyyy28" color="#0284c7"><u>LinkedIn</u></a> &nbsp;|&nbsp; '
        '<a href="https://github.com/allanborder" color="#0284c7"><u>GitHub</u></a> &nbsp;|&nbsp; '
        '<a href="https://allansspace.vercel.app" color="#0284c7"><u>Portfolio</u></a>',
        contact_style
    ))
    story.append(Spacer(1, 4))

    def make_section_header(title):
        return [
            Paragraph(f"<b>{title.upper()}</b>", section_heading),
            Spacer(1, 1.5),
            HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#cbd5e1"), spaceBefore=1, spaceAfter=3)
        ]

    # --- EDUCATION ---
    story.extend(make_section_header("Education"))
    edu_table = Table([
        [
            Paragraph("<b>Karunya Institute of Technology and Sciences</b> — B.Tech CSE (AI &amp; ML)", body_style),
            Paragraph('<para align="right"><b>2024 – 2028</b> | Coimbatore, India</para>', body_style)
        ],
        [
            Paragraph("CGPA: 7.0 &nbsp;|&nbsp; Latest SGPA: 7.54 &nbsp;|&nbsp; Specialised Courses: Artificial Intelligence &amp; Machine Learning", tech_style),
            Paragraph("", tech_style)
        ]
    ], colWidths=[380, 160])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(edu_table)
    story.append(Spacer(1, 4))

    # --- TECHNICAL SKILLS ---
    story.extend(make_section_header("Technical Skills"))
    skills_data = [
        [Paragraph("<b>Languages:</b>", body_style), Paragraph("Python, Java, JavaScript (ES6+), C, SQL", body_style)],
        [Paragraph("<b>Frontend:</b>", body_style), Paragraph("React, Vite, HTML5, CSS3, Tailwind CSS, Vanilla JS, Pure SVG Charts", body_style)],
        [Paragraph("<b>Backend &amp; DBs:</b>", body_style), Paragraph("FastAPI, Node.js, Express, SQLite, MongoDB, REST APIs, WebSockets", body_style)],
        [Paragraph("<b>AI / ML:</b>", body_style), Paragraph("TensorFlow, EfficientNetB0, Groq API (Llama 3.3 70B), Mistral LLM, Ollama, PyTorch", body_style)],
        [Paragraph("<b>Tools &amp; Platforms:</b>", body_style), Paragraph("Git, GitHub, Vercel, Docker, Chart.js, Pytest, Postman", body_style)],
    ]
    skills_table = Table(skills_data, colWidths=[90, 450])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.5),
        ('TOPPADDING', (0,0), (-1,-1), 0.5),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 4))

    # --- PROJECTS ---
    story.extend(make_section_header("Projects"))

    # Project 1: PatchWise
    p1_header = Table([
        [
            Paragraph('<b>PatchWise — AI-Powered Vulnerability Triage Platform</b> (<font color="#0284c7">Hackathon Finalist</font>)', body_style),
            Paragraph('<para align="right">2025</para>', body_style)
        ]
    ], colWidths=[460, 80])
    p1_header.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p1_header)
    story.append(Paragraph("• Built at Nexora/HackWithAMYPO 24-hr hackathon; combines CVSS, EPSS, CISA KEV, exposure, &amp; service criticality into an explainable 0–100 risk score.", bullet_style))
    story.append(Paragraph("• Implemented AI-driven plain-English remediation reports, deterministic multi-signal scoring pipeline, audit trail, and robust test suite.", bullet_style))
    story.append(Paragraph("<b>Tech:</b> Python, FastAPI, React, Tailwind CSS, LLM Integration, Pytest, CISA KEV API", tech_style))
    story.append(Spacer(1, 3))

    # Project 2: RJ
    p2_header = Table([
        [
            Paragraph('<b>RJ — Personal AI Voice Assistant &amp; System Daemon</b>', body_style),
            Paragraph('<para align="right">2025</para>', body_style)
        ]
    ], colWidths=[460, 80])
    p2_header.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p2_header)
    story.append(Paragraph("• Powered by Groq's Llama 3.3 70B with gesture-based wake detection (clap + snap) and continuous background listening daemon.", bullet_style))
    story.append(Paragraph("• Voice commands for hands-free app launching, screen captures, volume &amp; music control, clipboard reasoning, and persistent memory.", bullet_style))
    story.append(Paragraph("<b>Tech:</b> Python, Groq API (Llama 3.3 70B), SpeechRecognition, pyttsx3, WebSockets, PyAudio, SQLite", tech_style))
    story.append(Spacer(1, 3))

    # Project 3: NeuroAI
    p3_header = Table([
        [
            Paragraph('<b>NeuroAI — Brain MRI Tumor Classifier &amp; Diagnostic Report Generator</b>', body_style),
            Paragraph('<para align="right">2025</para>', body_style)
        ]
    ], colWidths=[460, 80])
    p3_header.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p3_header)
    story.append(Paragraph("• Classifies brain MRI scans into 4 categories (Glioma, Meningioma, Pituitary, No Tumor) using fine-tuned EfficientNetB0 (97%+ accuracy).", bullet_style))
    story.append(Paragraph("• Integrated Mistral 7B via local Ollama for structured diagnostic clinical reports; 100% on-device private inference without cloud dependencies.", bullet_style))
    story.append(Paragraph("<b>Tech:</b> TensorFlow, EfficientNetB0, FastAPI, React, Mistral LLM, Ollama, Python", tech_style))
    story.append(Spacer(1, 3))

    # Project 4: Body Blueprint Pro
    p4_header = Table([
        [
            Paragraph('<b>Body Blueprint Pro — AI-Powered Fitness &amp; Analytics Web App</b>', body_style),
            Paragraph('<para align="right">2025</para>', body_style)
        ]
    ], colWidths=[460, 80])
    p4_header.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p4_header)
    story.append(Paragraph("• Full-stack fitness application tracking 14+ body measurements, automated PR detection, and interactive SVG charts without external charting libraries.", bullet_style))
    story.append(Paragraph("• Features AI bodybuilding contest prep planner and workout/nutrition coach powered by Groq's Llama 3.3 70B.", bullet_style))
    story.append(Paragraph("<b>Tech:</b> React, Vite, Node.js, Groq API (Llama 3.3 70B), Tailwind CSS, Vercel, Pure SVG Charts", tech_style))
    story.append(Spacer(1, 4))

    # --- EXPERIENCE & INTERNSHIPS ---
    story.extend(make_section_header("Experience &amp; Internships"))

    # Internship 1: Lysa Solutions
    exp1 = Table([
        [
            Paragraph("<b>Lysa Solutions</b> — Full Stack Developer Intern", body_style),
            Paragraph('<para align="right">Jun – Aug 2026 | Coimbatore, India</para>', body_style)
        ]
    ], colWidths=[380, 160])
    exp1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(exp1)
    story.append(Paragraph("• Engineered backend APIs and responsive web interfaces during an on-site deployment, delivering features under active deadlines.", bullet_style))
    story.append(Spacer(1, 2))

    # Internship 2: Oasis Infobyte
    exp2 = Table([
        [
            Paragraph("<b>Oasis Infobyte</b> — Data Science Intern", body_style),
            Paragraph('<para align="right">Jun 2026</para>', body_style)
        ]
    ], colWidths=[380, 160])
    exp2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(exp2)
    story.append(Paragraph("• Built Python machine learning pipelines on industrial datasets, reinforcing practical model development, data preprocessing, and evaluation.", bullet_style))
    story.append(Spacer(1, 2))

    # Internship 3: Fuzionest
    exp3 = Table([
        [
            Paragraph("<b>Fuzionest Private Limited</b> — Software Developer Intern", body_style),
            Paragraph('<para align="right">Jun – Aug 2025</para>', body_style)
        ]
    ], colWidths=[380, 160])
    exp3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(exp3)
    story.append(Paragraph("• Analysed enterprise sales datasets, detected statistical anomalies, and prepared analytical insights presented directly to leadership.", bullet_style))
    story.append(Spacer(1, 4))

    # --- LEADERSHIP & ACHIEVEMENTS ---
    story.extend(make_section_header("Leadership &amp; Achievements"))
    ach_items = [
        "<b>GDG On Campus Karunya:</b> Media &amp; Content Production Lead — directing media production and developer brand assets (2025–Present).",
        "<b>National Runners-Up:</b> Mindkraft 26 IoT 'Switch &amp; Glitch' competition representing AIML department (2026).",
        "<b>Nexora Hackathon Finalist:</b> Built PatchWise vulnerability triage platform in 24h competitive sprint (2025)."
    ]
    for ach in ach_items:
        story.append(Paragraph(f"• {ach}", bullet_style))
    story.append(Spacer(1, 4))

    # --- CERTIFICATIONS ---
    story.extend(make_section_header("Certifications &amp; Courses"))
    certs = [
        "<b>CS205: Building with Artificial Intelligence</b> — Saylor Academy (Grade: 94.12 | 48 hrs | Jun 2025)",
        "<b>CS260: Introduction to Cryptography &amp; Network Security</b> — Saylor Academy (48 hrs | Jun 2025)",
        "<b>Introduction to Generative AI</b> — Google (LLMs, Prompt Engineering, Responsible AI)",
        "<b>AI Agents with MongoDB</b> — MongoDB (Building &amp; scaling intelligent AI agents)",
        "<b>DBMS — Master the Fundamentals &amp; Advanced Concepts</b> — Scaler Topics (SQL, ACID, Normalization, Indexing)"
    ]
    for cert in certs:
        story.append(Paragraph(f"• {cert}", bullet_style))

    doc.build(story)

    # Check page count
    reader = pypdf.PdfReader(output_path)
    print(f"Generated PDF with {len(reader.pages)} page(s).")
    return len(reader.pages)

if __name__ == '__main__':
    target = 'assets/documents/Allan_Resume_2026.pdf'
    generate_resume(target)
