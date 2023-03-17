import json
import base64
import requests
import xml.etree.ElementTree as ET
import urllib.request

def get_url_data(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    return data

def save_encoded_image(b64_image: str, output_path: str):
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(b64_image))

rss_feeds = {
  "cnn": "http://rss.cnn.com/rss/cnn_topstories.rss",
  "foxnews": "https://moxie.foxnews.com/google-publisher/latest.xml",
  "yahoo": "https://www.yahoo.com/news/rss",
  "latimes": "https://www.latimes.com/local/rss2.0.xml"
}

sdapi_url = "http://127.0.0.1:7860/sdapi/v1/txt2img"

for site, url in rss_feeds.items():
    xmldata = get_url_data(url)   
    root = ET.fromstring(xmldata)
    first_item = next((item for item in root.iter('item')), None)
    title = first_item.find('title').text
    first_link = next((guid for guid in first_item.iter('guid')), None).text
    prompt = {'prompt': title}
   
   # response = requests.post(url=sdapi_url,json=prompt)
   # save_encoded_image(response.json()['images'][0], "./" + site + ".png")
    print(site)
    print(title)
    print(first_link)


