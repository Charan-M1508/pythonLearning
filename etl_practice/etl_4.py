
import csv

def process_transactions(file_path):
    valid_list = []
    invalid_list = []
    valid_total = 0

    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    amount = float(row["amount"])

                    if amount > 0:
                        valid_list.append(row)
                        valid_total += amount
                    else:
                        invalid_list.append(row)

                except (KeyError, TypeError, ValueError):
                    invalid_list.append(row)

        print("Valid transactions:", len(valid_list))
        print("Invalid transactions:", len(invalid_list))
        print("Valid total amount:", valid_total)

        return valid_list, invalid_list

    except FileNotFoundError:
        print("Error: CSV file not found.")
    except UnicodeDecodeError:
        print("Error: Unable to decode the file.")

    return [], []

file_path = "C:/Users/marad/OneDrive/Desktop/transactions.csv"
valid, invalid = process_transactions(file_path)
