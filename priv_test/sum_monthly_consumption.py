import csv

# Function to sum the numbers in the second column
def sum_second_column(csv_filename):
    total = 0
    with open(csv_filename, mode='r') as file:
        csv_reader = csv.reader(file)
        # Skip header if it exists (uncomment if there's a header)
        # next(csv_reader)
        
        for row in csv_reader:
            try:
                # Assuming the second column contains numeric values
                total += float(row[1])  # row[1] refers to the second column
            except ValueError:
                # Skip rows where the second column isn't a valid number
                print(f"Skipping invalid value in row: {row}")
                continue
    return total

# Example usage
csv_filename = 'priv_test/monthly_consumption.csv'  # Replace with the path to your CSV file
result = sum_second_column(csv_filename)
print(f"The sum of the numbers in the second column is: {result}")