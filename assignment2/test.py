def prepareInfo(user_selection, file_name):

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
    index = 1
    for a in range(len(data)):
        print(str(index)+ "." +data[a])
        index +=1

def getUserInput(list_code, data):
    user_selection = input("Please select an entity from " + files[stage].rstrip(".txt"))
    str_code = list_code[int(user_selection)-1]
    title = data[int(user_selection)-1]
    return str_code, title

new_order = "n"
recipe = ""
while new_order == "n" or new_order == "N":
    files = ["categories.txt","products.txt","portions.txt"]
    stage = 0
    user_selection = ""

    print("""--------------------------------------------------
Welcome to the Store
--------------------------------------------------""")
    code, data = prepareInfo(user_selection, files[stage])
    printMenu(data)
    str_code, title = getUserInput(code, data)
    recipe += title

    for stage in range(1,3):
        print("--------------------------------------------------")
        print(title)
        print("--------------------------------------------------")
        code, data = prepareInfo(str_code, files[stage])
        printMenu(data)
        str_code, title = getUserInput(code, data)
        recipe += title
    recipe += title
    recipe += str_code
    new_order = input("Would you like to complete the order (y/n)?")
print(recipe)

