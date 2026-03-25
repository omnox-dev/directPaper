from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

def create_research_report(paper_analyses, topic, output_filename="research_report.pdf"):
    """
    Generate a simple PDF report using ReportLab.
    Each analysis is a dict with: title, summary, insights, etc.
    """
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    story.append(Paragraph(f"Research Report: {topic}", styles['Title']))
    story.append(Spacer(1, 12))
    
    for paper in paper_analyses:
        story.append(Paragraph(f"<b>Title:</b> {paper.get('title', 'Unknown')}", styles['Heading2']))
        story.append(Paragraph(f"<b>Authors:</b> {', '.join(paper.get('authors', []))}", styles['Normal']))
        story.append(Spacer(1, 6))
        
        # TL;DR
        story.append(Paragraph("<b>TL;DR Summary:</b>", styles['Heading3']))
        story.append(Paragraph(paper.get('tldr', 'No TLDR provided.'), styles['Normal']))
        story.append(Spacer(1, 6))
        
        # Insights
        story.append(Paragraph("<b>Key Insights:</b>", styles['Heading3']))
        story.append(Paragraph(paper.get('insights', 'No insights provided.'), styles['Normal']))
        story.append(Spacer(1, 12))
        
    doc.build(story)
    return os.path.abspath(output_filename)
