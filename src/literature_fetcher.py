
import requests
from bs4 import BeautifulSoup

def fetch_literature_from_url(url):
    """
    Fetch literature from a URL (e.g., PubMed).
    
    Args:
        url (str): URL of the literature page.
        
    Returns:
        str: Extracted text from the page.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()
    return content

def save_literature_to_file(content, filename='/workspaces/epidemic-research-ai/references/literature_input.txt'):
    """
    Save fetched literature to a file.
    
    Args:
        content (str): Fetched literature content.
        filename (str): File path to save content.
    """
    with open(filename, 'w') as f:
        f.write(content)
