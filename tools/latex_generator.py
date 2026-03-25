import os
import subprocess

def compile_with_tectonic(tex_path):
    """
    Compile a LaTeX file into a PDF using tectonic.
    """
    try:
        subprocess.run(["tectonic", tex_path], check=True)
        return tex_path.replace(".tex", ".pdf")
    except Exception as e:
        print(f"Tectonic compilation failed: {e}")
        return None

def generate_latex_manuscript(final_manuscript_text, topic, output_filename="manuscript.tex"):
    """
    Generate a professional LaTeX research paper using the synthesized text.
    """
    paper_content = final_manuscript_text

    # IMPROVED ESCAPING:
    # We trust the LLM to provide LaTeX structure (\section, \cite, etc.)
    # We only escape characters that frequently cause crashes in raw text: &, %, #
    # We DO NOT escape _ here because it breaks commands like \cite{label_1}
    
    # 1. Protect already escaped characters
    paper_content = paper_content.replace(r'\&', 'PROTECTED_AMPERSAND')
    paper_content = paper_content.replace(r'\%', 'PROTECTED_PERCENT')
    paper_content = paper_content.replace(r'\#', 'PROTECTED_HASH')
    
    # 2. Escape any REMAINING raw characters that are NOT math or commands
    paper_content = paper_content.replace('&', r'\&')
    paper_content = paper_content.replace('%', r'\%')
    paper_content = paper_content.replace('#', r'\#')

    # 3. Restore protected characters
    paper_content = paper_content.replace('PROTECTED_AMPERSAND', r'\&')
    paper_content = paper_content.replace('PROTECTED_PERCENT', r'\%')
    paper_content = paper_content.replace('PROTECTED_HASH', r'\#')

    # 4. Handle Unicode characters like em-dashes and quotes
    paper_content = paper_content.replace('—', '---')
    paper_content = paper_content.replace('–', '--')
    paper_content = paper_content.replace('“', '``')   # Left double quote
    paper_content = paper_content.replace('”', "''")   # Right double quote
    paper_content = paper_content.replace('‘', '`')    # Left single quote
    paper_content = paper_content.replace('’', "'")    # Right single quote

    # 4. FIX MARKDOWN BOLD/ITALIC (Common LLM slip-ups)
    # Convert **bold** to \textbf{bold}
    import re
    paper_content = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', paper_content)
    # Convert *italic* to \textit{italic}
    paper_content = re.sub(r'\*(.*?)\*', r'\\textit{\1}', paper_content)

    # 5. FIX DOUBLE SLASHES (e.g., \\' or \\_)
    # Sometimes LLMs over-escape or the previous logic caused double slashes.
    # We normalize \\' to ' and \\" to " etc. if they look redundant.
    paper_content = paper_content.replace(r"\\'", "'")
    paper_content = paper_content.replace(r'\\"', '"')

    # 5. REMOVE DOCSTRINGS:
    # Sometimes LLMs wrap output in ```latex ... ```
    if "```latex" in paper_content:
        paper_content = paper_content.split("```latex")[-1].split("```")[0]
    elif "```" in paper_content:
        paper_content = paper_content.split("```")[-1].split("```")[0]

    latex_content = r"""\documentclass[12pt, a4paper]{article}

% --- Packages ---
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath, amssymb}
\usepackage{microtype}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{mdframed}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{tabularx}  % Added for better table handling

% --- Custom Image Placeholder Command ---
\newcommand{\imageplaceholder}[2]{
    \begin{figure}[htbp]
        \centering
        \framebox[0.8\textwidth]{\vbox to 3cm{\vfill \centering #1 \vfill}}
        \caption{#2}
    \end{figure}
}

% --- Page Setup ---
\geometry{margin=1in}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,      
    urlcolor=cyan,
    pdftitle={Research Paper Manuscript},
}

% --- Custom Box for Placeholders ---
\newmdenv[
    linecolor=black,
    linewidth=1pt,
    backgroundcolor=gray!10,
    innerrightmargin=10pt,
    innertopmargin=20pt,
    innerbottommargin=20pt,
    font=\small\itshape
]{placeholderbox}

% --- Title Information ---
\title{\textbf{Bridging the Cognitive Gap: """ + topic + r"""}}
\author{Om Dombe \\ \small Craftexa Technologies}
\date{\today}

\begin{document}

\maketitle

""" + paper_content + r"""

\end{document}
"""
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    # Optional: Automatically Compile with Tectonic
    pdf_path = compile_with_tectonic(output_filename)
    
    return os.path.abspath(output_filename), (os.path.abspath(pdf_path) if pdf_path else None)
