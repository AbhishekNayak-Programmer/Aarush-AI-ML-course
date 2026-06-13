import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()
    data = response.json() 
    print(data)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")