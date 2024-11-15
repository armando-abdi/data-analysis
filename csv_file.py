import csv  # Import the csv module

# Define the filename for the CSV file
filename = 'Book_store_data.csv'

# Open the file in write mode ('w') and ensure newlines are handled properly
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)  # Create a csv.writer object
