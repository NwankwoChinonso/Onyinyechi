import requests

url = "http://127.0.0.1:8000/api/users/register/"  # Replace with your actual URL if different

data = {
    "username": "NwankwoChinonso",
    "email": "directednwankwo@gmail.com.com",
    "password": "NwankwoFrank@1"
}

response = requests.post(url, json=data)

# Print the status code to check the response status
print("Status Code:", response.status_code)

# Print the raw response text to see if there is any data returned
print("Response Text:", response.text)

# Attempt to parse JSON only if the response is valid
if response.status_code == 200:
    print("Response JSON:", response.json())  # Prints the response body as JSON
else:
    print("Error: The response did not contain valid JSON or was unsuccessful.")

"""

url2 = "http://127.0.0.1:8000/api/users/login/"
data = {
    "username": "adrian",
    "password": "strongpassword"
}

response = requests.post(url2, json=data)
print(response.status_code)
print(response.json())  # Expected to return a token

url3 = "http://127.0.0.1:8000/api/users/logout/"
headers = {
    "Authorization": "Token YOUR_AUTH_TOKEN"  # Replace YOUR_AUTH_TOKEN with the actual token
}

response = requests.post(url3, headers=headers)
print(response.status_code)
print(response.json())  # Expected to return a logout success message


url4 = "http://127.0.0.1:8000/api/users/profile/"
headers = {
    "Authorization": "Token YOUR_AUTH_TOKEN"  # Replace with the actual token you received from login
}

response = requests.get(url4, headers=headers)
print(response.status_code)
print(response.json())  # Expected to return the user profile

"""