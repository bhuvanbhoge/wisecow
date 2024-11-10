import requests

url = "https://red-sea-094bb1510.5.azurestaticapps.net/"  # Replace with your application URL(Currently i have pasted my personal portfolio)

def check_app_status():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Application is UP and running.")
        else:
            print(f"Application is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error checking application: {e}")

check_app_status()

