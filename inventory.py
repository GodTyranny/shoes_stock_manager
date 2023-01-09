#========Class Declaration========
class Class_Shoes():

    #Constructor that initialise and create all the main value of this object
    def __init__(self, local_string_country : str, local_string_code : str, local_string_product : str, local_float_cost : float, local_int_quantity : int):
        self.string_country = local_string_country
        self.string_code = local_string_code
        self.string_product = local_string_product
        self.int_cost = local_float_cost
        self.int_quantity = local_int_quantity

    #Return the cost of this object shoes
    def method_get_cost(self):
        return self.int_cost

    #Return the stock value for this product
    def method_stock_value(self):
        return self.int_cost * self.int_quantity

    #Return the quantity in stock of this object shoes
    def method_get_quantity(self):
        return self.int_quantity

    #Return all the info about this object shoes
    def __str__(self):
        local_list_string = []
        local_list_string2 = []
        local_string = ""

        #All the text will became same lenght to have more readability
        #Can be separated by a character or have different spacing character
        local_list_string = ["|Product", "|Country", "|Code", "|Price","|Quantity", "|Stock Cost"]
        local_list_string = method_textAlignmentCorrector(local_list_string, 8, " ", True, "|:")

        local_list_string2 = [self.string_product, self.string_country, self.string_code,
         str(self.int_cost) + " R/each", str(self.int_quantity), str(self.int_cost * self.int_quantity) + " R"]
        local_list_string2 = method_textAlignmentCorrector(local_list_string2, 6, " ", True, "|")


        #String building with colour and format
        #As all the string are same lenght, get a full line lenght and build a edge
        local_string = "⋎" * (len(local_list_string[0]) + len(local_list_string2[0]) - 2)
        local_string_text = f"{Class_TextMod.green}▲{local_string}▲\n"

        #Object shoes details
        for i in range(len(local_list_string)):
            local_string_text += f"{Class_TextMod.blue}{local_list_string[i]}{Class_TextMod.yellow}{local_list_string2[i]}\n"

        #Full line lenght edge
        local_string = local_string.replace("⋎","⋏")
        local_string_text += f"{Class_TextMod.green}▼{local_string}▼"

        return local_string_text

#Class contined printing colour and mode
class Class_TextMod():
    reset = "\033[0m"
    blue = "\033[94m"
    cyan = "\033[96m"
    darkcyan = "\033[36m"
    green = "\033[92m"
    yellow = "\033[93m"
    lightred = "\033[91m"
    pink = "\033[95m"
    bold = "\033[1m"
    underline = "\033[4m"

#========END Class Declaration========

#==========Variable declaration==========

#List of object from the class shoes
list_class_shoes : "list[Class_Shoes]" = []

#==========END Variable==========

#==========Function declaration==========

    #=====Program function=====
#Create object shoes for each shoes on file inventory
def method_read_shoes_data():

    #Empty the list of object to fulfil with new updated object
    list_class_shoes.clear()
    local_bool_corrupted = False

    #Check if file exist
    try:
        file_inventory = open("inventory.txt", "r", encoding="utf-8")
    except:
        #Error message
        print(f"{Class_TextMod.lightred}No file have been found")
        #Exit from this method
        return
    
    local_list_string = file_inventory.read().split("\n")
    local_list_string_categories = ""

    #Starting from 1 to avoid the label line
    #Separate each categories in the line and create a new shoes object with that data
    for i in range(1, len(local_list_string)):
        #To prevent error in the data conversion or categories amount due to manual alteration or wrong file loading
        try:
            local_list_string_categories = local_list_string[i].strip().split(",")
            list_class_shoes.append(Class_Shoes(local_list_string_categories[0],local_list_string_categories[1],
            local_list_string_categories[2],float(local_list_string_categories[3]),int(local_list_string_categories[4])))
        except:
            #If last line in file is empty (cause of \n), don't show any error
            if not (local_list_string[i] == local_list_string[-1] and local_list_string[-1].strip() == ""):
                #Error message
                print(f"{Class_TextMod.lightred}An error occur trying to load file line {i + 1}\nContent:\t{local_list_string[i].strip()}")
                print()

                #A corrupted info have been found
                local_bool_corrupted = True
                continue

    print(f"{Class_TextMod.cyan}Currently loaded {len(list_class_shoes)} shoes")
    print()
    file_inventory.close()

    if local_bool_corrupted:
        print(f"{Class_TextMod.lightred}Any corrupted data have been removed on the process")
        print()
        method_rebuild_file()

#Create a new shoes object and add to the file, if no file exist one will be created
def method_capture_shoes():

    local_string_input = ""
    local_string_builder = ""
    local_list_string_categories = ["Country","Code","Product","Cost","Quantity","Details are correct? y/n"]
    local_list_string : "list[str]"= []
    local_int_index = 0

    try:
        file_inventory = open("inventory.txt", "a+")
    except:
        #Error message
        print(f"{Class_TextMod.lightred}No file have been found, one have been created")
        print()
        #Create a new file
        file_inventory = open("inventory.txt", "w")
        file_inventory.write("Country,Code,Product,Cost,Quantity\n")

    print(f"{Class_TextMod.green}―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
    print(f"{Class_TextMod.cyan}Insert new shoes details, insert -1 to skip")

    #Get all the input to create a new shoes object
    while True:

        print(f"{Class_TextMod.cyan}{local_list_string_categories[local_int_index]}", end="")
        local_string_input = input(f"{Class_TextMod.pink}: ").strip().replace(","," ")

        if local_string_input == "-1":
            break
        elif local_int_index == 3: #Case Cost
            try:
                if not float(local_string_input) > 0:
                    #Error message
                    print(f"{Class_TextMod.lightred}Insert a positive number")
                    print()
                    continue                                        
            except:
                #Error message
                print(f"{Class_TextMod.lightred}Insert a positive number")
                print()
                continue
        elif local_int_index == 4: #Case quantity
            try:
                if not int(local_string_input) > 0:
                    #Error message
                    print(f"{Class_TextMod.lightred}Insert a positive number")
                    print()
                    continue                   
            except:
                #Error message
                print(f"{Class_TextMod.lightred}Insert a positive integer number")
                print()
                continue   
        elif local_int_index == 5:
            if local_string_input.lower() == "y":
                local_string_builder = local_string_builder.strip(",")

                local_list_string = local_string_builder.split(",")
                print(local_list_string)

                #Create the new shoes object
                list_class_shoes.append(Class_Shoes(local_list_string[0], local_list_string[1],
                 local_list_string[2], float(local_list_string[3]), int(local_list_string[4])))

                #Add the new object info as string to the file
                local_string_builder += "\n"
                file_inventory.write(local_string_builder)
                break
            else:
                #Error message
                print(f"{Class_TextMod.lightred}Please insert details again or insert -1 to skip")
                print()
                local_int_index = 0
                local_string_builder = ""
                continue              


        local_string_builder += local_string_input + ","
        local_int_index += 1

    print(f"{Class_TextMod.green}―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――") 
    file_inventory.close()

#Display all the shoes object
def method_view_all():

    if len(list_class_shoes) > 0:
        for obj_shoes in list_class_shoes:
            print(obj_shoes)
    else:
        #Error message
        print(f"{Class_TextMod.lightred}No shoes have been loaded or insert in the system")
        print()

#Check the product with lowest stock and ask user if they want to buy more
def method_re_stock():

   # print(f"All the shoes data have been loaded to check for restock{}")
    print()

    method_read_shoes_data()

    if len(list_class_shoes) > 0: 

        local_int_index = 0
        #This value is set to an impossible stock quantity as default
        #To can check value lower than this
        local_int_quantity = 10000000
        local_string_input = ""

        #Check for the lowest stock quantity and save its index in shoes list
        for i in range(len(list_class_shoes)):
            if local_int_quantity > list_class_shoes[i].int_quantity:
                local_int_quantity = list_class_shoes[i].int_quantity
                local_int_index = i

        print()
        print(f"{Class_TextMod.bold}{Class_TextMod.cyan}This shoes have the lowest stock!!!{Class_TextMod.reset}")
        print(list_class_shoes[local_int_index])
        print()

        #User choice to update stock
        print(f"{Class_TextMod.cyan} want to buy 20 new units? y/n")
        local_string_input = input(f"{Class_TextMod.pink}: ").strip()

        if local_string_input.lower() == "y":
            list_class_shoes[local_int_index].int_quantity += 20

            #Build the file with the new update and clean the data inside
            method_rebuild_file()

            print(f"{Class_TextMod.green}20 new shoes have been bought")
            print()


        else:
            #Error message
            print(f"{Class_TextMod.lightred}No stock have been bought")
            print()
    else:
        #Error message
        print(f"{Class_TextMod.lightred}No shoes have been loaded or insert in the system")
        print()

#Display the object shoes with a specific code
def method_search_shoes():

    if len(list_class_shoes) > 0:

        local_bool_printed = False
        print(f"{Class_TextMod.cyan}Insert shoes code")
        local_string_input = input(f"{Class_TextMod.pink}: ").strip()
        print()


        for obj_shoes in list_class_shoes:
            if obj_shoes.string_code == local_string_input:
                print(obj_shoes)
                local_bool_printed = True
        
        if not local_bool_printed:
            #Error message
            print(f"{Class_TextMod.lightred}No matching code found")

        print()
    else:
        #Error message
        print(f"{Class_TextMod.lightred}No shoes have been loaded or insert in the system")
        print()
    

#Display the value of stock for each product
def method_value_per_item():

    if len(list_class_shoes) > 0:
        local_list_string = []
        local_list_string2 = []

        for obj_shoes in list_class_shoes:
            local_list_string.append("|"+obj_shoes.string_product)
            local_list_string2.append(str(obj_shoes.method_stock_value()) + " R")

        
        #All the text will became same lenght to have more readability
        #Can be separated by a character or have different spacing character
        local_list_string = method_textAlignmentCorrector(local_list_string, 6, " ", True, "|:")
        local_list_string2 = method_textAlignmentCorrector(local_list_string2, 6, " ", True, "|")

        #String building with colour and format
        #As all the string are same lenght, get a full line lenght and build a edge
        local_string = "☵" * (len(local_list_string[0]) + len(local_list_string2[0]) - 2)

        #Top edge
        local_string_text = f"{Class_TextMod.green}║{local_string}║\n"

        for i in range(len(local_list_string)):
            #Object shoes details required
            local_string_text += f"{Class_TextMod.blue}{local_list_string[i]}{Class_TextMod.yellow}{local_list_string2[i]}\n"
            #Bottom edge
            local_string_text += f"{Class_TextMod.green}║{local_string}║\n"

        print(local_string_text)
    else:
        #Error message
        print(f"{Class_TextMod.lightred}No shoes have been loaded or insert in the system")
        print()


#Display the shoes object/product with highest quantity in stock
def method_highest_quantity():

    if len(list_class_shoes) > 0:
        local_int_index = 0
        local_int_quantity = 0
        for i in range(len(list_class_shoes)):
            if local_int_quantity < list_class_shoes[i].int_quantity:
                local_int_quantity = list_class_shoes[i].int_quantity
                local_int_index = i

        print()
        print(f"{Class_TextMod.bold}{Class_TextMod.cyan}This shoes is on sale now!!!{Class_TextMod.reset}")
        print(list_class_shoes[local_int_index])
        print()
    else:
        #Error message
        print(f"{Class_TextMod.lightred}No shoes have been loaded or insert in the system")
        print()

    #=====Program function END=====

    #=====Utility function=====
#Return the list of string insert spaced by chosen amount with chosen character to be clear for reading, you can insert even ending character
def method_textAlignmentCorrector(local_list_string : "list[str]", local_int_increaser : int = 5, local_string_spacing : str = " ",
 local_bool_ending : bool = False, local_string_ending : str = ":") -> "list[str]":

    #Create a copy of the list sended as reference to prevent the change of the original list
    #That may be not desired in every case
    local_list_string = local_list_string[:]
    local_int_lenght = 0

    #Look for the longest string and its index inside the list
    for i in range(len(local_list_string)):
        if local_int_lenght < len(local_list_string[i]):
            local_int_lenght = len(local_list_string[i])

    #Building the spacing based on the preference
    for i in range(len(local_list_string)):
        if local_bool_ending:
            local_list_string[i] += (local_string_spacing * (local_int_lenght - len(local_list_string[i]) + local_int_increaser - 1)) + local_string_ending
        else:
            local_list_string[i] += local_string_spacing * (local_int_lenght - len(local_list_string[i]) + local_int_increaser)            
    return local_list_string

#Build back the file from the data inside the list of object, all the non loaded content will be removed
#So only the non properly written data will be removed
def method_rebuild_file():

    local_string_fileBuilder = ""

    #File will be cleaned from incorrect object as will be insert only the one that have
    #been succesfully loaded
    file_inventory = open("inventory.txt", "w", encoding="utf-8")

    #ReCreate the header
    local_string_fileBuilder = "Country,Code,Product,Cost,Quantity\n"

    #Build back the whole file content with the new quantity updated
    for i in range(len(list_class_shoes)):
        local_string_fileBuilder += f"{list_class_shoes[i].string_country},"
        local_string_fileBuilder += f"{list_class_shoes[i].string_code},"
        local_string_fileBuilder += f"{list_class_shoes[i].string_product},"
        local_string_fileBuilder += f"{list_class_shoes[i].int_cost},"
        local_string_fileBuilder += f"{list_class_shoes[i].int_quantity}\n"

    file_inventory.write(local_string_fileBuilder)
    file_inventory.close()

    #=====Utility function END=====
#==========END Function==========

#=======START POINT=======

def method_main():
    local_string_fileCheck = ""
    local_string_menu = ""
    local_string_container = ""
    local_string_option = ""
    local_list_string_menu = ["|Select one of the following Options below",
    "|━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
    "|rd - Read shoes data",
    "|c  - Capture shoes",
    "|va - View all",
    "|rs - Re-Stock",
    "|s  - Search shoes",
    "|vi - Value per item",
    "|hq - Highest quantity",
    "|e  - Exit"]

    try:
        file_inventory = open("inventory.txt", "r+", encoding="utf-8")
    except:
        #Error message
        print(f"{Class_TextMod.lightred}No file have been found, one have been created")
        print()
        #Create a new file
        file_inventory = open("inventory.txt", "w+", encoding="utf-8")
        file_inventory.write("Country,Code,Product,Cost,Quantity\n")

    local_string_fileCheck = file_inventory.read()
    #Check if file have new line as last character and eventually add it
    if (len(local_string_fileCheck ) > 0) and (not local_string_fileCheck[-1] == "\n"):
        file_inventory.write("\n")
    file_inventory.close()

    #Create a string containing the menu to display
    local_list_string_menu = method_textAlignmentCorrector(local_list_string_menu, 3, " ", True, "|")

    #String building with colour and format
    #As all the string are same lenght, get a full line lenght and build a edge
    local_string_container = "┰" * (len(local_list_string_menu[0]) - 2)
    local_string_menu = f"{Class_TextMod.green}▲{local_string_container}▲\n"

    #Object shoes details
    for i in range(len(local_list_string_menu)):
        local_string_menu += f"{Class_TextMod.blue}{local_list_string_menu[i]}\n"

    #Full line lenght edge
    local_string_container = local_string_container.replace("┰","┻")
    local_string_menu += f"{Class_TextMod.green}▼{local_string_container}▼"

    method_read_shoes_data()
    print()

    print(f"{Class_TextMod.blue}{Class_TextMod.bold}Welcome back!{Class_TextMod.reset}")

    #Working loop
    while True:
        #Menu
        print(local_string_menu)

        #User menu choice
        local_string_option = input(f"{Class_TextMod.pink}: ").lower()
        print()

        if local_string_option == "rd":
            method_read_shoes_data()
        elif local_string_option == "c":
            method_capture_shoes()
        elif local_string_option == "va":
            method_view_all()
        elif local_string_option == "rs":
            method_re_stock()
        elif local_string_option == "s":
            method_search_shoes()
        elif local_string_option == "vi":
            method_value_per_item()
        elif local_string_option == "hq":
            method_highest_quantity()
        elif local_string_option == "e":
            exit()
        else:
            #Error message
            print(f"{Class_TextMod.lightred}No available option have been selected")
            print()   


#START CODE
method_main()