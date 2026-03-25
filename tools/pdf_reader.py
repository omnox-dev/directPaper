from pypdf import PdfReader
import os

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    """
    if not os.path.exists(pdf_path):
        return ""
    
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def parse_research_paper(text):
    """
    Simple heuristic or LLM-based parsing (placeholder for LLM extraction).
    For now, return the full text or first 5000 chars to avoid token limits.
    """
    return text[:10000] 
