import requests



def get_url_status(url):  # checks status for each url in list urls
    try:
        r = requests.get(url)
        temp_status = str(r.status_code)
    except Exception as e:
        temp_status = "Failed to connect"
    return temp_status