import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url, output_folder):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for img_tag in img_tags:
        img_url = img_tag.get('src')
        if img_url:
            img_url = urljoin(url, img_url)
            img_name = img_url.split('/')[-1]
            img_path = os.path.join(output_folder, img_name)
            with open(img_path, 'wb') as img_file:
                img_file.write(requests.get(img_url).content)

# Example usage:
website_url = "https://kshetradarshan.com//tirumala//srivari-seva-voluntary-seva//"
output_folder = r"C:\Users\user\OneDrive\Documents\Desktop\jup"

download_images(website_url, output_folder)
