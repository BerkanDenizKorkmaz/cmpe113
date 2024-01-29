def prepareInfo(user_selection, file_name):
    """
        This function takes user_selection(int) and file_name(string) as inputs and
        returns two lists

        code(list): Contains all the codes of the selected category or product or portion
        (for portion it means price since there is no more selection needed)

        data(list): Contains the possible selectable categories or products or portions
    """
    code = []
    data = []
    file = open(file_name, "r")
    line = file.readline()
    while line != "":
        line = line.rstrip("\n")
        line = line.split(";")
        if stage == 0:
            data.append(line[1])
            code.append(line[0])
            if line[0] == str(user_selection):
                code.append(line[0])
        else:
            if line[0] == "#" + str(user_selection):
                data.append(line[1])
                code.append(line[2])
        line = file.readline()
    file.close()
    return code, data

def printMenu(data):
    """
        This function takes data(list) as input and writes each element of data(list) with increasing order beginning from 1
    """
    index = 1
    for a in range(len(data)):
        print(str(index)+ "." +data[a])
        index +=1

def getUserInput(list_code, data):
    """
        This function takes list_code(list) and data(list) as inputs and depending on the users choice returns
        the selected thing(string) and code of the thing(str) -For portion it becomes the price-
    """
    user_selection = input("\nPlease select an entity from " + files[stage].rstrip(".txt")+" ")
    str_code = list_code[int(user_selection)-1]
    title = data[int(user_selection)-1]
    return str_code, title

def recipeFormat(recipe):
    """
        This function takes recipe(list of lists) which contains list of each order and
        aligning the elements of the list column by column then prints.
    """
    for row in range(0,len(recipe)):
        print("{0:<25} {1:<35} {2:<20} {3:<4}".format(recipe[row][0], recipe[row][1], recipe[row][2], recipe[row][3]))

new_order = "n"
recipe = []
total = 0

print("""--------------------------------------------------
Welcome to the Store
--------------------------------------------------""")

while new_order == "n" or new_order == "N":
    files = ["categories.txt","products.txt","portions.txt"]
    stage = 0
    user_selection = ""
    order = []

    code, data = prepareInfo(user_selection, files[stage])
    printMenu(data)
    str_code, title = getUserInput(code, data)
    order.append(title)

    for stage in range(1,3):
        print("\n--------------------------------------------------")
        print(title)
        print("--------------------------------------------------")
        code, data = prepareInfo(str_code, files[stage])
        printMenu(data)
        str_code, title = getUserInput(code, data)
        order.append(title)
    order.append(str_code+"$")
    total += float(str_code)
    recipe.append(order)
    print("--------------------------------------------------")
    new_order = input("Would you like to complete the order (y/n)? ")
    print("--------------------------------------------------")

print("\nORDER RECIPE")
print("========================================================================================")
recipeFormat(recipe)
print("========================================================================================")
print("Total:   {:.2f}$".format(total))