# Importing the necessary libraries
import pandas as pd  # Pandas library for data manipulation
from matplotlib import pyplot as plt  # Matplotlib for data visualization

# Create a DataFrame with initial book data
df_books = pd.DataFrame({
    'Title': ['Python for Beginners', 'Advanced Machine Learning', 'Data Science Essentials', 'Mystery of the Lost City', 'Thrilling Adventures'],
    'Author': ['Jane Doe', 'John Smith', 'Emily Johnson', 'Chris Davis', 'Alex Brown'],
    'Publication Year': [2020, 2018, 2019, 2017, 2021],
    'Genre': ['Programming', 'Technology', 'Data Science', 'Mystery', 'Adventure'],
    'Sales': [1000, 350, 150, 3000, 1200]
})

# Additional book data
df_books_additional = pd.DataFrame({
    'Title': ['Learning Python', 'Deep Learning with Python', 'Data Analysis with Python', 'Python Machine Learning', 'Python for Data Science'],
    'Author': ['Mark Lutz', 'François Chollet', 'Wes McKinney', 'Sebastian Raschka', 'Jake VanderPlas'],
    'Publication Year': [2021, 2019, 2022, 2020, 2018],
    'Genre': ['Programming', 'Artificial Intelligence', 'Data Science', 'Machine Learning', 'Data Science'],
    'Sales': [800, 900, 700, 650, 750]
})

# Save initial DataFrame to CSV
df_books.to_csv('Book_store_data.csv', index=False)

# Append additional DataFrame to CSV without the header
df_books_additional.to_csv('Book_store_data.csv', mode='a', index=False, header=False)

# Read the CSV file into a new DataFrame
df = pd.read_csv('Book_store_data.csv')

# Add 'Price Before Tax' column
df['Price Before Tax'] = [9.97, 29.99, 37.99, 3.50, 9.99, 16.57, 38.99, 17.60, 22.39, 29.48]

# Calculate and add 'Tax' column
df['Tax'] = df['Price Before Tax'].apply(lambda price: round(price * 0.07, 2))

# Calculate and add 'Price After Tax' column
df['Price After Tax'] = round(df['Price Before Tax'] + df['Tax'], 2)

# Calculate and add 'Revenue' column
df['Revenue'] = df['Price Before Tax'] * df['Sales']

# Calculate and add 'Profit After Tax' column
df['Profit After Tax'] = round(df['Revenue'] - (df['Sales'] * df['Tax']), 2)

# Rename columns for clarity
df.columns = ['Book Title', 'Author Name', 'Year Published', 
              'Genre Category', 'Units Sold', 'Price Before Tax (USD)', 
              'Sales Tax (USD)', 'Price After Tax (USD)', 'Total Revenue (USD)', 
              'Net Profit After Tax (USD)']

# Save the updated DataFrame back to CSV
df.to_csv('Book_store_data.csv', index=False)

# Print the updated DataFrame
print(df)

# Calculate and print total net profit
total_net_profit = df['Net Profit After Tax (USD)'].sum()
print(f'Your total net profit is: ${total_net_profit}')

# Group by Genre Category and sum Units Sold
df_genre_units_sold = df.groupby('Genre Category')['Units Sold'].sum().reset_index()
print(df_genre_units_sold)

# Group by Genre Category and sum Total Revenue
df_book_title_total_revenue = df.groupby('Genre Category')['Total Revenue (USD)'].sum().reset_index()
print(df_book_title_total_revenue)

# Plot Total Units Sold by Genre Category
plt.bar(df_genre_units_sold['Genre Category'], df_genre_units_sold['Units Sold'], color='orange')
plt.title('Total Genre Units Sold')
plt.xlabel('Genre')
plt.ylabel('Units Sold')
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.show()

# Plot Total Revenue by Genre Category
plt.figure(figsize=(10, 6))
plt.bar(df_book_title_total_revenue['Genre Category'], df_book_title_total_revenue['Total Revenue (USD)'], color='skyblue')
plt.title('Total Revenue by Genre Category')
plt.xlabel('Genre Category')
plt.ylabel('Total Revenue (USD)')
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.tight_layout()  # Adjust layout
plt.show()
