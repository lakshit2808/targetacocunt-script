import csv
import requests
import streamlit as st

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
            st.success("All data successfully sent to API")
        else:
            st.error("Some data failed to send to API")
            st.write(len(response.json()) - len(data))
            
        return len(response.json())
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {str(e)}")
def csv_to_json(csv_file_path, email):
    # Read CSV file
    data = []
    try:
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        st.success("CSV data read successfully")
        
        # Get existing data from API
        existing_data = []
        try:
            response = requests.get(f"https://app.forceequals.ai/api/target-accounts?email={email}")
            response.raise_for_status()
            existing_data = response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to fetch existing data: {str(e)}")
            return

        # Send data to API, checking for duplicates
        for row in data:
            row['email'] = email
            # Check if record already exists
            is_duplicate = False
            for existing in existing_data:
                if existing.get('name') == row.get('name') and existing.get('email') == email:
                    is_duplicate = True
                    st.warning(f"Duplicate record found for {row.get('name')} - skipping")
                    break
            
            if not is_duplicate:
                api_response = post_to_api(row)
                if api_response:
                    st.success(f"Data successfully sent to API for {row.get('name')}")
                else:
                    st.error(f"Failed to send data to API for {row.get('name')}")
                    st.write(row)

    except FileNotFoundError:
        st.error("Error: Input file not found")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
