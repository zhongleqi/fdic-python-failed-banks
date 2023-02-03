import requests
import csv
from datetime import datetime
url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/banklist.csv'
response = requests.get(url)

with open('banklist.csv','w') as local_file:
    local_file.write(response.text)

ca_banks = []
with open('banklist.csv','r') as source_file:
    dict_reader = csv.DictReader(source_file)
    for row in dict_reader:
        state = row['State\xa0']
        if state == 'CA':
            date_string = row['Closing Date\xa0']
            date_object = datetime.strptime(date_string, "%d-%b-%y")
            row['Closing Date\xa0'] = date_object.strftime("%Y-%m-%d")
            ca_banks.append(row)


with open ('failed_banks_ca.csv', 'w') as new_file:
    col_headers = ['Bank Name\xa0', 'City\xa0', 'State\xa0', 'Cert\xa0', 'Acquiring Institution\xa0', 'Closing Date\xa0', 'Fund']
    dict_writer = csv.DictWriter(new_file, fieldnames=col_headers)
    dict_writer.writeheader()
    dict_writer.writerows(ca_banks)

count_of_banks = len(ca_banks)
print(f"There are {count_of_banks} failed banks in CA")