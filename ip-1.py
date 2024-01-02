import requests

def get_fresh_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        if response.status_code == 200:
            data = response.json()
            return data["ip"]
        else:
            return None
    except requests.exceptions.RequestException:
        return None

# Example usage
fresh_ip = get_fresh_ip()
if fresh_ip:
    print("Fresh IP address:", fresh_ip)
else:
    print("Failed to retrieve fresh IP address")
    