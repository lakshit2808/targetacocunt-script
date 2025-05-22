from Functions import csv_to_json, verify_data

if __name__ == "__main__":
    csv_file_path = "CyberMSI_TargetAccounts.csv"
    email = "fyg1207@gmail.com"
    # csv_to_json(csv_file_path, email)
    print(verify_data(email, csv_file_path))  # Remove "#" in the beginning to verify data
