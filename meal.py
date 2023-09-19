
import requests

# API URL
url = "https://www.themealdb.com/api.php"

# Sending a GET request to the API
response = requests.get(url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response text
    print(response.text)
else:
    print("Failed to retrieve data from the API. Status code:", response.status_code)
