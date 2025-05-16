
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

def csv_to_json(csv_file_path, email):
    # Read CSV file
    data = []
    try:
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        print("CSV data read successfully")
        data[0]["email"] = email
        print(data[0])
        # Send data to API
        api_response = post_to_api(data[0])
        if api_response:
            print("Data successfully sent to API")

    except FileNotFoundError:
        print("Error: Input file not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    csv_file_path = "CyberMSI_TargetAccounts.csv"
    email = "test@example.com"
    csv_to_json(csv_file_path, email)
