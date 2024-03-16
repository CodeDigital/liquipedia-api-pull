import requests

LIQUIPEDIA_URL = ""



if __name__ == "__main__":
    import requests

    url = "https://liquipedia.net/counterstrike/api.php"

    querystring = {"action":"parse","format":"json","page":"PGL/2024/Copenhagen"}

    payload = ""
    headers = {
        "User-Agent": "EsportsAnalyticaCS2DW/0.1 (https://github.com/CodeDigital/esports-analytica-documentation;xavltrav@gmail.com)",
        "Accept-Encoding": "gzip"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)