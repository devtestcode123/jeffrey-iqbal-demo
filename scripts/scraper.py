import urllib.request
from bs4 import BeautifulSoup
import os
import re

base_url = "http://jeffreyiqbal.com"
pages = {
    "Home": "/",
    "About": "/about/",
    "Packages": "/packages/",
    "Music": "/music/",
    "Video": "/video/",
    "Unity_Thru_Music": "/unity-thru-music/",
    "Contact": "/contact/"
}

output_dir = r"E:\SideProjects\JefferyIqbal"
os.makedirs(output_dir, exist_ok=True)

for name, path in pages.items():
    url = base_url + path
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.extract()
            
        # Get text
        text = soup.get_text(separator='\n', strip=True)
        
        # Clean up empty lines
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        clean_text = '\n'.join(lines)
        
        # Save to file
        file_path = os.path.join(output_dir, f"{name}.txt")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"--- URL: {url} ---\n\n")
            f.write(clean_text)
            
        print(f"Successfully extracted {name} to {name}.txt")
    except Exception as e:
        print(f"Failed to extract {name} from {url}: {e}")