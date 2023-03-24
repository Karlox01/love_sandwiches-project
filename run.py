import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sales_data():
    """
    Get sales figures input from the user
    """
    while True:
        print('Please enter sales data from the last market.')
        print('Data should be six numbers, seperated by commas.')
        print('Example: 10,20,30,40,50,60\n')

        data_str = input('Enter your data here:')

        sales_data = data_str.split(',')
        

        if validate_data(sales_data):
            print('data is valid!')
            break
    return sales_data # We will use this on the very first step 1 and on step 6

   

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there arent exactly 6 values
    """

    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required , you provided {len(values)}"
            )
    except ValueError as e:
        print(f'Invalid data: {e}, Please try again. \n')
        return False

    return True
    

""" 

OBSOLETE


Commenting out these 2 functions as they are obsolete // For training purposes.


def update_sales_worksheet(data):
    
     Update sales worksheet, add new row with the list data provided.
    
    print('updating sales worksheet....\n')
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print('sales worksheet updated successfully. \n')



def update_surplus_worksheet(data):
    
     Update surplus worksheet, Compare the sales against stock. 
    
    print('updating surplus worksheet....\n')
    surplus_worksheet = SHEET.worksheet('surplus')
    surplus_worksheet.append_row(data)
    print('surplus worksheet updated successfully. \n')



    OBSOLETE
"""


def update_worksheet(data, worksheet): # 2 Data will be variable sales_data Which returns user input of 6 numbers Like wise worksheet will be asigned to sales page/ worksheet
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f'Updating {worksheet} worksheet...\n') # 3 Our function than prints updating "sales" worksheet
    worksheet_to_update = SHEET.worksheet(worksheet) # 4 We than pair a new variable to worksheet and the sales page of the worksheet
    worksheet_to_update.append_row(data) # 5 We than append that variable to go on to access that page on the sales work sheet and input the numbers user has input.
    print(f'{worksheet} worksheet updatedd successfully\n')




def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defines as the sales figure sub tracted from the stock:
    -Positive surplus indicates waste
    -Negative surplus indicates extra made when stock was sold out.
    """
    print('Calculating surplus data...\n')
    stock = SHEET.worksheet('stock').get_all_values()
    stock_row = stock[-1]

    surplus_data =[]
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data


def get_last_5_entry_sales():
    """
    Collects columns of data from sales worksheet, collecting the
    last 5 entries for each sandwich and returns the data
    as a list of lists.
    """
    sales = SHEET.worksheet('sales')
    # column = sales.col_values(3) # This will give us column for chicken spread note columns start counting at 1 here and not at 0
    # print(column)

    columns = []
    for ind in range(1, 7): # The google sheets columns start count at 1 hence why we had to set 1, 7
        column = sales.col_values(ind)
        columns.append(column[-5:]) # This will slice the list so that we only display last 5 inputs
    return columns



def main():
    """
    Run all program functions
    """

    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, 'sales') #  1 This is where the Function starts, Once called, We pass it our data for Sales row and we pass it the string value of sales,  
    new_surplus_data = calculate_surplus_data(sales_data) # 6 Once previous function is executed we than call the main function where we call a new variable that calls function calculate_surplus_data with sales_data data.  
    update_worksheet(new_surplus_data, 'surplus') # 7 than we call our update_worksheet function again, This time we pass it our new surplus data that holds data from calculate_surplus_data function , And this time we want to update 'surplus' page/worksheet
    
 
print('welcome to love sandwiches data automation')
# main()

sales_columns = get_last_5_entry_sales()