# main.py

import csv
print("hello")
# Data to write
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'Mumbai'],
    ['Bob', 25, 'Delhi'],
    ['Charlie', 35, 'Bangalore']
]

# CSV file path
filename = 'output.csv'

# Write to CSV
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{filename}' created successfully.")
