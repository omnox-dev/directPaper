# 📄 Agentic Research Assistant: Multi-Agent Synthesis Engine

> **"Transforming Information Overload into Published Insights"**

A high-impact, **multi-agent research ecosystem** that automates the entire academic lifecycle—from ArXiv discovery to professional LaTeX manuscript generation. Built with **LangGraph** and powered by **Gemini 2.5 Flash**, it mimics a faculty-level research team to produce 5+ page manuscripts in minutes.

---

## 💎 The Multi-Agent Architecture
This is not a simple chatbot. It is a **distributed system of specialized agents** working in high-fidelity coordination:

1.  **🕵️ The Search Scout (ArXiv Node)**: Performs deep searches on ArXiv, handling meta-data and link extraction.
2.  **⚖️ The Curator (Selection Node)**: Uses semantic reasoning to filter the top 6 papers for depth and relevance.
3.  **🔬 The Specialized Analyst (Extraction Node)**: A dedicated reader that extracts algorithms, math equations, and metrics from raw PDFs.
4.  **🖋️ The Lead Writer (Synthesis Node)**: Performs "Synthetic Reasoning"—connecting the dots across various papers to propose new frameworks.
5.  **🏛️ The Publisher (LaTeX Generator)**: A professional typesetting expert that creates clean, error-free LaTeX source and PDF assets.

---

## ✨ Key Features
- **🚀 Gemini 2.5 Flash Optimized**: Leverages high-speed reasoning and deep context windows for academic rigor.
- **📚 Smart Paper Selection**: AI-powered curation ensures you analyze the best work, not just the first 10 results.
- **⚙️ Tectonic Compilation**: Automatically generates journal-quality PDFs with zero local LaTeX setup required.
- **🛠️ Robust Escape-Handling**: Proprietary LaTeX cleaning logic ensures `_`, `&`, and `%` never crash your build.
- **⚖️ Rate-Limit Resilience**: Intelligent sequential pacing allows the system to run on **Gemini Free Tier (5 RPM)** without failure.

---

## 🚀 Quick Start

### 1. Prerequisites
- **Python 3.10+** (v3.13 recommended)
- **Tectonic** (for automated PDF generation): `cargo install tectonic` or download from [tectonic-typesetting.org](https://tectonic-typesetting.org/)

### 2. Installation
```powershell
# Clone the repository
git clone https://github.com/omnox-dev/directPaper
cd directPaper

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### 4. Run the App
```powershell
streamlit run app.py
```

---

## 🛠️ Technology Stack
- **Orchestration**: LangGraph
- **Language Models**: Google Gemini 2.5 Flash
- **UI Framework**: Streamlit
- **Research API**: ArXiv API
- **Typesetting**: TeX/LaTeX (via Tectonic Engine)
- **Typographics**: Microtype (for optical margin alignment)

---

## 📜 Future Roadmap (2027)
- [ ] **Multi-Modal Parsing**: Reading charts, diagrams, and figures directly from PDFs.
- [ ] **BibTeX Database**: Automated citation cross-referencing with DOI lookup.
- [ ] **Peer-Review Mode**: A dedicated agent to critique its own draft for logical fallacies.

---
**Created for Competition by Om Dombe (Craftexa Technologies)**
