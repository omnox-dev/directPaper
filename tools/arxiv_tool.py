import arxiv
import requests
import os

def search_arxiv(query, max_results=6):
    """
    Search ArXiv for papers matching the query with retry on rate-limiting.
    """
    import time
    
    # Use the newer arxiv.Client for better handling of retries and configuration
    client = arxiv.Client(
        page_size=max_results,
        delay_seconds=3,  # Added buffer between requests
        num_retries=3     # Automatically retry on common failures
    )
    
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    
    results = []
    try:
        # Client.results() manages the connection and pagination
        for result in client.results(search):
            results.append({
                "title": result.title,
                "authors": [author.name for author in result.authors],
                "summary": result.summary,
                "pdf_url": result.pdf_url,
                "published": result.published.strftime("%Y-%m-%d"),
                "entry_id": result.entry_id
            })
    except Exception as e:
        print(f"ArXiv search encountered an error: {e}")
        # If we hit 429, we already have retries, but if it still fails:
        if "429" in str(e):
            print("Rate limit reached. Please wait a minute before searching again.")
    
    return results

def download_pdf(url, filename, download_dir="downloads"):
    """
    Download a PDF from a URL.
    """
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    filepath = os.path.join(download_dir, filename)
    response = requests.get(url)
    with open(filepath, 'wb') as f:
        f.write(response.content)
    return filepath
