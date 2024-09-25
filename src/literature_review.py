
from .literature_fetcher import fetch_literature_from_url, save_literature_to_file

def generate_literature_review_with_urls():
    """
    Generate a literature review by fetching research papers from given URLs.
    """
    urls = [
        'https://pubmed.ncbi.nlm.nih.gov/1234567/',
        'https://pubmed.ncbi.nlm.nih.gov/7654321/'
    ]
    
    review = ""
    
    for url in urls:
        content = fetch_literature_from_url(url)
        review += content + "\n\n"
    
    save_literature_to_file(review)
