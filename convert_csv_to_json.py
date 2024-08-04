import csv
import json

csv_file = 'csv.csv'  # Update with CSV file path
json_file = 'json.json'  # Output JSON file path


output_data = []
with open(csv_file, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row if exists
    for row in reader:
        disease = row[0]
        cases = int(row[1])
        percentage = float(row[2])

        item = {
            'disease': disease,
            'cases': cases,
            'percentage': percentage
        }

        output_data.append(item)

with open(json_file, mode='w') as file:
    json.dump(output_data, file, indent=4)

print(f'CSV file "{csv_file}" successfully converted to JSON file "{json_file}".')
