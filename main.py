
import csv

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

    except FileNotFoundError:
        print("Error: Input file not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    csv_file_path = "CyberMSI_TargetAccounts.csv"
    email = "test@example.com"
    csv_to_json(csv_file_path, email)
