
import csv

def remove_duplicates(file_path):
    original_list = []
    duplicate_list = []
    seen_ids = set()

    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                transaction_id = row["transaction_id"]

                if transaction_id not in seen_ids:
                    original_list.append(row)
                    seen_ids.add(transaction_id)
                else:
                    duplicate_list.append(row)

        print("Unique transactions:", len(original_list))
        print("Duplicate transactions:", len(duplicate_list))

        return original_list, duplicate_list

    except (FileNotFoundError, UnicodeDecodeError) as error:
        print(f"Error: {error}")
        return [], []

file_path = "C:/Users/marad/OneDrive/Desktop/transactions.csv"
unique_transactions, duplicate_transactions = remove_duplicates(file_path)
