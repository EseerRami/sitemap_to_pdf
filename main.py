import requests
from bs4 import BeautifulSoup
import pdfkit
import os

# Define the directory where you want to save the PDFs
output_dir = 'C:/Users/avion/Desktop/Sitemap_To_PDF'

# Download the sitemap
sitemap_url = 'https://customgpt-streamlit.s3.amazonaws.com/customgpt-streamlit/eb2abeaa-0fd0-45bc-913e-d7976f1ae9a8.xml'
response = requests.get(sitemap_url)
sitemap = BeautifulSoup(response.content, 'xml')

# Find all the URLs in the sitemap
urls = [loc.text for loc in sitemap.find_all('loc')]

# Download each URL and save it as a PDF
for url in urls:
    try:
        # Remove "https://" from the filename and replace remaining slashes with underscores
        filename = url.replace("https://", "").replace("/", "_") + ".pdf"
        output_path = os.path.join(output_dir, filename)
        pdfkit.from_url(url, output_path)
        print(f'Successfully saved {url} as a PDF')
    except Exception as e:
        print(f'Failed to save {url} as a PDF: {e}')
