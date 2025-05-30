import requests

OBJ_ID = 173
URL = f"https://www.pr.hamburg/ws/ws.get.status.php?obj={OBJ_ID}"

def fetch_free_spaces():
    resp = requests.get(URL, timeout=5)
    resp.raise_for_status()
    return int(resp.text.strip())

if __name__ == "__main__":
    total = 232
    free = fetch_free_spaces()
    used = total - free
    print(f"Aktuell freie Stellplätze: {free}")
    print(f"Aktuell belegte Stellplätze: {used}")
