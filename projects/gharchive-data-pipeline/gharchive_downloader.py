import requests
from datetime import datetime, timedelta

def download_gharchive_data():
    hour = (datetime.now() - timedelta(hours=3)).strftime('%Y-%m-%d-%H')

    url = f"https://data.gharchive.org/{hour}.json.gz"
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Downloaded {local_filename}")
    return local_filename
