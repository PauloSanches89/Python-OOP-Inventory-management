from tabulate import tabulate
import math

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        """Initialising the attributes of the "Shoe" class."""

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
       
    def get_cost(self):
        """
        Method to retrieve the cost of an object.
        Returns an int.
        """
        cost = int(self.cost)
        return cost


    def get_quantity(self):
        """
        Method retrieving current stock of a shoe.
        Returns an int.
        """

        quant = int(self.quantity) 
        return quant
        

    def __str__(self):
        """initialises the format to print this object as string"""

        return f"""
Country:      {self.country}
Code:         {self.code}
Product name: {self.product}
Cost:         {self.cost}
Quantity:     {self.quantity}
"""
       



#=============Shoe list===========
"""
The list will be used to store a list of objects of shoes.
"""
shoe_list = []
#==========Functions outside the class==============

def verify_product_code(text):
    """
    Takes the input when prompted for a product code and checks that is 
    is in correct format. Prints instructions on correct input and 
    loops until correct format entered. Returns 
    correctly formatted stock code.
    """
    # loops until acceptable input is entered.
    while True:
        try:
            product_code_input = input(text).upper()
            
            # Checks for length
            if len(product_code_input) == 8:
                code_check = False
                num_check = False
                # Checks first 3 chars are 'SKU' & last 5 are numbers
                if product_code_input[3:8].isdigit() == True:
                    num_check = True

                if "SKU" in product_code_input[0:3]:
                    code_check = True

                if code_check == True and num_check == True:
                    # Returns if valid
                    return product_code_input
                
                else:
                    raise ValueError("Correct format: SKU##### \
(Where # is an integer)")
                    
            else:
                raise ValueError("Correct format: SKU##### \
(Where # is an integer)")
            
        except ValueError as ve:
            print(ve)
        



def get_int(text): 
    """
    Asks for an int input and keeps asking until value is 
    entered as int. Returns the int value.
    """
    while True:
        try:
            # Keeps trying until input is a positive integer
            integer_input = int(input(text))

            if integer_input < 0:
                raise ValueError("Input cannot be negative.")
        
        except ValueError as ve:
            # This error message handles non numeric input
            if "invalid literal" in str(ve):
                
                print("Please enter an integer")

            else:
                # This error handles negative input
                print(str(ve))
            
        else:
            return integer_input
            

def read_shoes_data(): 
    """
    Populates shoe_list with current stock of shoes from database in
    inventory.txt
    """
    # Opening file to read data.
    file = None
    try:
        file = open("inventory.txt", "r")
        
    except FileNotFoundError as error:
        print(error)
        print("\n" + "Please make sure the file \"inventory.txt\"" + 
              " exists in the current directory.")
        exit()

    else:
    
        # Skipping first line to avoid headers
        next(file)

        # Copying data from file and creating list of objects
        for line in file:
            line = line.strip()
            line = line.split(",")
            shoe_data = Shoe(line[0], line[1], line[2], line[3], 
                             line[4])

            shoe_list.append(shoe_data)

    finally:
        # Closing the file if it was created.
        if file is not None:
            file.close()
    
    
def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list. It also writes appends 
    the inventory.txt file with the addition.
    '''
    # Get user input for Shoe object attributes, 
    # looping until valid Inputs are entered
    country = input("Enter country of manufacture: ").capitalize()
    code = verify_product_code("Enter 8 character product code: ")
    product = input("Enter Product name: ")
    cost = get_int("Enter cost of product: R")
    quantity = get_int("Enter quantity in stock: ")
    
    # Creating temporary shoe object 
    new_shoe = Shoe(country, code, product, cost, quantity)

    # Append shoe to inventory list in inventory.txt
    file = None
    try:
        file = open("inventory.txt", "a")

    except FileNotFoundError:
        print("Unable to open inventory.")

    else:
        # Writes into inventory.txt with comma separated values
        file.write("\n" + new_shoe.country + "," + 
                    new_shoe.code + "," + 
                    new_shoe.product + "," +
                    str(new_shoe.cost) + "," +
                    str(new_shoe.quantity))
        
    finally:
        if file is not None:
            file.close()
            print()

def view_all():
    '''
    This function populates a list of lists from shoe_list to be used 
    with the tabulate function. The output is in the form of a table.
    '''
    # Loop through shoe list, creating a new list to store data
    table_data = [[shoe.country, 
                  shoe.code, 
                  shoe.product, 
                  shoe.cost, 
                  shoe.quantity] for shoe in shoe_list]
    
    # Printing the data to a table using tabulate() 
    print()
    print(tabulate(table_data, headers=["Country", "Code", "Product", 
                                  "Cost", "Quantity"]))
    print()


def re_stock():
    """
    Finds the shoe that has the lowest stock and asks user 
    if more should be bought. If yes is input it prompts for a 
    positive integer and prints the new value. It also 
    changes the total in the inventory.txt file.
    """
    # Creating list to find minimum quantity index value
    quant_list = []
    # Populate a list of integers to find the index with the lowest
    # quantity value.
    for shoe in range(len(shoe_list)):
        quant_list.append(shoe_list[shoe].get_quantity())

    #finding the index for the lowest quantity shoe
    low_index = quant_list.index(min(quant_list))

    # Printing to screen data of shoe
    print(shoe_list[low_index])

    # Prompting user to buy more stock (y/n)
    buy_shoes = None
    
    # Check that user input is appropriate
    while buy_shoes != "y" and buy_shoes != 'n':
        buy_shoes = input("Would you like to restock? (y/n): ")
        # If user selects to re_stock adds input integer to total
        if buy_shoes == "y":
            how_many = get_int("Enter number to purchase: ")
            x = int(shoe_list[low_index].quantity)
            x = x + how_many
            shoe_list[low_index].quantity = str(x)
            
            # Prints to screen updated values
            print("Transaction succesful!")
            print(shoe_list[low_index])
        
        elif buy_shoes =="n":
            print("\nNo change was made to inventory.\n")



    # Opens file to write
    file = open("inventory.txt", "w")

    # Writes header
    file.write("Country,Code,Product,Cost,Quantity")
    
    # Updates inventory.txt
    for shoe in range(len(shoe_list)):
        file.write(f"""\n{shoe_list[shoe].country},\
{shoe_list[shoe].code},\
{shoe_list[shoe].product},\
{shoe_list[shoe].cost},\
{shoe_list[shoe].quantity}""")
    file.close()
    
    


def seach_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that 
     it will be printed.
    '''
    # Asks for user input: product code
    product_code = verify_product_code("Enter product code to \
view details: ")
    # Checks if product code exists
    for shoe in range(len(shoe_list)):
        if shoe_list[shoe].code == product_code:
            return shoe_list[shoe]
        

    print("That product is not in the database. \
Enter 'c' at the main menu to add a new shoe.")
    

def value_per_item():
    '''
    This function will calculate the total value for each item.
    It then prints the information in tabular format.
    '''
    # creating a list containing data for output
    table_data = [[shoe.code,\
                    shoe.product,\
                    shoe.get_quantity() * shoe.get_cost()] \
                    for shoe in shoe_list]

    # Prints table
    print(tabulate(table_data, headers=["Code","Product",\
"Total value (R)"]))
    print()
    

def highest_qty():
    '''
    Determines the product with the highest quantity and
    prints this shoe as being for sale.
    '''
    # creating an empty list to store quantities 
    quant_list = []
    
    # populating list with quantities
    for shoe in range(len(shoe_list)):
        quant_list.append(shoe_list[shoe].get_quantity())

    # Finding the index of the object with the highest quantity
    max_index = quant_list.index(max(quant_list))

    # Printing the Sale message
    print("\n" + "The " + shoe_list[max_index].product + 
          " is currently on SALE!\n")
    
    

#==========Main Menu=============
'''
A menu that executes each function above.
'''


while True:
    # Making sure that the list is empty, ready for next iteration 
    # of the main menu.
    shoe_list.clear()

    # Called every iteration so any changes made reflect in next choice
    read_shoes_data()
    
    # Menu selection
    menu = input("""Make a selection by entering the following:
                 
c  - Capture data for new shoes
va - View all shoes in stock
r  - Re-stock
s  - Search for a shoe using product code
v  - Shows the value of stock on hand for each shoe
h  - To see which shoe is currently on sale
q  - To quit

Selection: """).lower()
    
    
    # if statements to make selection and else to capture input errors
    if menu == "c":
        capture_shoes()

    elif menu == "va":
        view_all()

    elif menu == "r":
        re_stock()

    elif menu == "s":
        print(seach_shoe())

    elif menu == "v":
        value_per_item()
    
    elif menu == "h":
        highest_qty()
        

    elif menu == "q":
        exit()

    else:
        print("Invalid selection. Please try again." + "\n")