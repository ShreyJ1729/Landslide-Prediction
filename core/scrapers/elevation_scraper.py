import os
import argparse
import requests
import re

"""
Downloads all zip files from the viewfinder panoramas elevation dataset
"""

class ElevationScraper:
    def __init__(self):
        self.data_url = "http://viewfinderpanoramas.org/Coverage%20map%20viewfinderpanoramas_org3.htm"
        self.base_dir = "./data/elevation/"

    def download_data(self):
        req = requests.get(self.data_url)
        urls = re.findall(r"\"(https?://\S+)\"", str(req.text))
        urls = urls[4:]
        # urls = open(os.path.join(self.base_dir, "urls.txt"))
        # urls.write(str(urls))
        
        # now download all of it and save to proper dir
        print(urls)