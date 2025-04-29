from bs4 import BeautifulSoup
import csv

# Step 1: Open the local HTML file
with open('form.html', 'r', encoding='utf-8') as file:
    html_content = file.read()  # Read the content of the HTML file

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Find the table in the HTML file
table = soup.find('table')  # Locate the <table> tag

if table:
    # Step 4: Extract headers from the <thead> section
    headers = [header.text.strip() for header in table.find('thead').find_all('th')]

    # Step 5: Extract data rows from the <tbody> section
    rows = []
    for row in table.find('tbody').find_all('tr'):
        cells = [cell.text.strip() for cell in row.find_all('td')]
        rows.append(cells)

    # Step 6: Write data into a CSV file
    with open('form_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)  # Write headers as the first row
        writer.writerows(rows)    # Write all data rows

    print("Data successfully saved to 'form_data.csv'.")
else:
    print("No table found in the HTML file.")

