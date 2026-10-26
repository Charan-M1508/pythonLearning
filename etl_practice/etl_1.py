import csv

def calculate_daily_sales(file_path):
    daily_totals = {}

    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    date = row["date"]
                    amount = int(row["amount"])

                    if not date or row["amount"] == "":
                        continue

                    if date in daily_totals:
                        daily_totals[date] += amount
                    else:
                        daily_totals[date] = amount

                except (KeyError, TypeError, ValueError):
                    continue

        return daily_totals

    except FileNotFoundError:
        print("Error: CSV file not found.")
    except UnicodeDecodeError:
        print("Error: Unable to decode the file.")

    return {}

file_path = "C:/Users/marad/OneDrive/Desktop/transactions.csv"

result = calculate_daily_sales(file_path)
print(result)
    