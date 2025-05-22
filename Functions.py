
import csv
import requests

def post_to_api(data):
    url = "https://app.forceequals.ai/api/target-accounts"
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        print(f"API Response Status: {response.status_code}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {str(e)}")
        return None

def verify_data(email, csv_file_path):
    url = f"https://app.forceequals.ai/api/target-accounts?email={email}"
    try:
        data = []
        response = requests.get(url)
        response.raise_for_status()
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        if len(response.json()) == len(data):
            print("All data successfully sent to API")
        else:
            print("Some data failed to send to API")
            print(len(response.json()) - len(data))
            
        return len(response.json())
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {str(e)}")

def csv_to_json(csv_file_path, email):
    # Read CSV file
    data = []
    try:
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        print("CSV data read successfully")
        # Send data to API
        for row in data:
            row['email'] = email
            api_response = post_to_api(row)
            if api_response:
                print("Data successfully sent to API")
            else:
                print("Failed to send data to API")
                print(row)


    except FileNotFoundError:
        print("Error: Input file not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")