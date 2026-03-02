#!/usr/bin/env python3
"""Generate an updated CV PDF for Mousa Abdullah Alqarni."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


OUTPUT_FILE = "cv. Mousa Abdullah - updated.pdf"


def build_cv_pdf(output_path: str) -> None:
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
        title="Mousa Abdullah Alqarni CV",
        author="Mousa Abdullah Alqarni",
    )

    base_styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "CVTitle",
        parent=base_styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        alignment=1,  # centered
        textColor=colors.HexColor("#1f2937"),
        spaceAfter=6,
    )
    contact_style = ParagraphStyle(
        "Contact",
        parent=base_styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=13,
        alignment=1,  # centered
        textColor=colors.HexColor("#374151"),
        spaceAfter=8,
    )
    section_style = ParagraphStyle(
        "SectionHeader",
        parent=base_styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=14,
        textColor=colors.HexColor("#111827"),
        spaceBefore=8,
        spaceAfter=4,
    )
    subheader_style = ParagraphStyle(
        "SubHeader",
        parent=base_styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=13,
        textColor=colors.HexColor("#111827"),
        spaceBefore=3,
        spaceAfter=2,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=base_styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#1f2937"),
        spaceAfter=2,
    )
    bullet_style = ParagraphStyle(
        "Bullet",
        parent=body_style,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=1.5,
    )

    story = []

    def section(title: str) -> None:
        story.append(Paragraph(title, section_style))

    def subheader(text: str) -> None:
        story.append(Paragraph(text, subheader_style))

    def body(text: str) -> None:
        story.append(Paragraph(text, body_style))

    def bullets(items: list[str]) -> None:
        for item in items:
            story.append(Paragraph(f"- {item}", bullet_style))

    story.append(Paragraph("Mousa Abdullah Alqarni", title_style))
    story.append(
        Paragraph(
            (
                "Email: mosa.alqarni01@gmail.com | Phone: 0531096142<br/>"
                "LinkedIn: https://www.linkedin.com/in/mousa-al-qarni-0440a22b2/"
            ),
            contact_style,
        )
    )

    section("EDUCATION")
    subheader(
        "Computer Science College, King Khalid University | "
        "Bachelor of Science in Computer Engineering | 09/2020 - 06/2025"
    )
    body("Second Class Honors.")

    section("EXPERIENCE")
    subheader(
        "Software Engineering Bootcamp Trainee | Holberton School (USA) "
        "- in partnership with Tuwaiq Academy | Riyadh, Saudi Arabia "
        "(Cloud-Based Program) | Oct 2025 - Present"
    )
    body(
        "An intensive, full-time Software Engineering program focused on practical, "
        "project-based learning and real-world development practices."
    )
    body("<b>Program Highlights:</b>")
    bullets(
        [
            "Strong foundation in Linux and Shell scripting.",
            "Low-level programming with C.",
            "Backend development using Python.",
            "Database management with SQL.",
            "Web development using Flask Framework.",
            "Practical use of AI tools in software development.",
            "System design fundamentals and problem-solving methodologies.",
        ]
    )
    body("<b>Technical Environment:</b>")
    bullets(
        [
            (
                "Worked daily on a dedicated cloud-based Ubuntu Linux sandbox "
                "environment provided by Holberton School (Middle East infrastructure)."
            ),
            "Version control and collaboration using Git and GitHub.",
            "Developed multiple individual and team-based projects published on GitHub.",
        ]
    )
    body("<b>Collaboration and Leadership:</b>")
    bullets(
        [
            (
                "Actively collaborated on team projects following real-world "
                "development workflows."
            ),
            (
                "Conducted peer-led technical sessions to exchange knowledge on "
                "various programming and system topics."
            ),
            "Practiced agile-style teamwork and structured code reviews.",
        ]
    )
    story.append(Spacer(1, 2))
    subheader(
        "Intern at the City Administration - IT Department | Military City, "
        "Khamis Mushait, Saudi Arabia | 06/2023 - 08/2023"
    )
    body(
        "Received training across key IT areas, including networks, backend/frontend "
        "programming, and technical support."
    )
    bullets(
        [
            "Studied network architecture across military city departments.",
            "Handled authentication requests through DC server workflows.",
            "Learned core router and PC hardware components.",
            "Performed periodic cable maintenance and RAM replacement.",
            "Formatted PCs and configured printers.",
            "Contributed to development of employee attendance programs.",
        ]
    )

    section("SKILLS")
    subheader("Technical Skills")
    bullets(
        [
            "High-level programming: Java, Python, SQL.",
            "Low-level programming: Assembly, C.",
            "Web development: HTML, CSS, JavaScript, Flask.",
            "Operating systems and tools: Ubuntu Linux, Shell scripting, Git, GitHub.",
            "Networking and IoT: Node-RED, MQTT, I2C, SPI, UART.",
            "Embedded systems: Raspberry Pi, Arduino, Microcontrollers.",
        ]
    )
    subheader("Soft Skills")
    bullets(
        [
            "Adaptability",
            "Problem solving",
            "Teamwork",
            "Critical thinking",
            "Communication",
            "Time management",
        ]
    )

    section("COURSES")
    bullets(
        [
            "The Web Developer Bootcamp.",
            "Introduction to Artificial Intelligence Bootcamp.",
            "Node-RED Bootcamp.",
            (
                "Robotic Applications Bootcamp: Smart Tank Project "
                "(second place in the camp)."
            ),
            "Blockchain Bootcamp.",
            "Internet of Things and Digital Transformation Fundamentals - Cisco.",
        ]
    )

    section("LEADERSHIP AND COMMUNITY INVOLVEMENT")
    subheader("Active Member - Tuwaiq Tech Club | Tuwaiq Academy")
    bullets(
        [
            "Co-organized technical workshops with academy instructors.",
            "Participated in organizing internal programming competitions.",
            "Supported knowledge-sharing initiatives among students.",
            "Contributed to building a collaborative technical learning environment.",
        ]
    )

    section("LANGUAGES")
    body("Arabic - Native | English - Fluent")

    doc.build(story)


if __name__ == "__main__":
    build_cv_pdf(OUTPUT_FILE)
    print(f"Generated: {OUTPUT_FILE}")
