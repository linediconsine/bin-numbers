import csv,sys
#
# https://www.mastercard.us/en-us/business/issuers/get-support/simplified-bin-account-range-table.html
# https://www.mastercard.us/content/dam/mccom/global/bintable/Simplified_BIN_Account_Range_Table_Reference_Guide.pdf
#

number = int(str(sys.argv[1]).ljust(10, '0')[0:10])
filename = './MC-SBART/latest.csv'

with open(filename, 'r') as f:
    reader = csv.DictReader(f)
    print(f"-- checking {number}")
    for row in reader:
        if int(row['ACCOUNT_RANGE_FROM']) <= number <= int(row['ACCOUNT_RANGE_TO']):
            print(f"Card id from {row['COMPANY_NAME']}")
            print(row)