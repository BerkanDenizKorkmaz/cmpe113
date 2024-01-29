#300201084

import os
"""
 My code does not check whether there is a line or not in the blank file 
 if you call "remove" or "modify" for invalid line(blank) there will be a
 "There is no such file." error not any specific error.
"""
def Create(query, file_names):
    file_name = query[2]
    attributes_list = query[4].split(",")
    attributes_str = "id," + query[4]
    if "id" in attributes_list:
        print("You cannot create a file with attribute 'id'.")
    else:
        if file_name in file_names:
            file = open(file_name, "w")
            file.write(attributes_str + "\n")
            print("There was already such a file. It is removed and then created again.")
            file.close()
        else:
            file = open(file_name, "w")
            file.write(attributes_str + "\n")
            print("Corresponding file was successfully created.")
            file.close()

def Delete(query, file_names):
    file_name = query[2]
    if file_name in file_names:
        os.remove(file_name)
        print("Corresponding file was successfully deleted.")
    else:
        print("There is no such file.")

def Display(file_names):

    print("Number of files: " + str(len(file_names)))
    for index in range(len(file_names)):
        if len(file_names) > 0:
            file = open(file_names[index], "r")
            attributes = file.readline()
            attributes = attributes.rstrip("\n")
            file.close()
            print( str(index+1) + ") " + file_names[index]+": " + attributes)
        else:
            break
def AddLine(query, file_names):
    new_id = 1
    ids = []
    file_name= query[3]
    if file_name not in file_names:
        print("There is no such file.")
    else:
        file = open(file_name, "r")
        attributes = file.readline()
        attributes = attributes.lstrip("id,")
        attributes = attributes.rstrip("\n")
        attributes = attributes.split(",")
        file.close()
        if len(attributes) == len(query[1].split(",")):
            file = open(file_name, "r")
            line = file.readline()
            while line != "":
                line = line.rstrip("\n")
                line.split(",")
                line = file.readline()
                if line != "":
                    ids.append(line[0])
            file.close()

            ids.sort()

            for id in ids:
                if new_id == int(id):
                    new_id +=1
                else:
                    break
            file = open(file_name,"a")
            file.write(str(new_id) + "," + query[1] + "\n" )
            file.close()
            print("New line was successfully added to students with id = " + str(new_id) + ".")

        else:
            print("Numbers of attributes do not match.")

def RemoveLines(query, file_names):
    file_name = query[3]
    if file_name not in file_names:
        print("There is no such file.")

    else:
        file = open(file_name,"r")
        line = file.readline()
        line = line.rstrip("\n")
        attributes = line.split(",")
        file.close()

        file = open(file_name, "r")
        lines = file.readlines()
        line_counter_initial = len(lines)
        file.close()

        if query[5] not in attributes:
            print("Your query contains an unknown attribute.")

        else:
            lines = []
            file = open(file_name, "r")
            lines = file.readlines()
            file.close()

            if query[6] == "==":
                file = open(file_name,"w")
                file.write(",".join(attributes) + "\n")
                for number, line in enumerate(lines):
                    if query[5] != query[7]:
                        file.write(line)
                file.close()
                file = open(file_name,"r")
                lines = file.readlines()
                line_counter_final = len(lines)
                file.close()
            else:
                file = open(file_name, "w")
                file.write(",".join(attributes) + "\n")
                for number, line in enumerate(lines):
                    if query[5] == query[7]:
                        file.write(line)
                file.close()
                file = open(file_name, "r")
                lines = file.readlines()
                line_counter_final = len(lines)
                file.close()

            removed_lines = line_counter_initial - line_counter_final
            print(str(removed_lines)+" lines were successfully removed.")

def ModifyLines(query,file_names):
    file_name = query[3]
    att_index = 0

    if file_name not in file_names:
        print("There is no such file.")

    else:
        file = open(file_name, "r")
        line = file.readline()
        line = line.rstrip("\n")
        attributes = line.split(",")
        file.close()


        if query[1] not in attributes:
            print("Your query contains an unknown attribute.")

        elif query[1] == "id":
            print("Id values cannot be changed.")

        else:
            modified_data = []
            modify_count = 0
            for modified_att in attributes:
                if modified_att == query[1]:
                    break
                else:
                    att_index += 1

            if query[8] == "==":
                file = open(file_name,"r")
                data = file.readlines()
                file.close()

                for element in data:
                    identifiers_list = element.split(",")
                    if identifiers_list[att_index] == query[9]:
                        identifiers_list[att_index] = query[5]
                        identifiers_str = ",".join(identifiers_list)
                        modified_data.append(identifiers_str)
                        modify_count += 1
                    else:
                        modified_data.append(element)

                file = open(file_name,"w")
                for line in modified_data:
                    file.write(line)
                file.close()

                print(str(modify_count) + " lines were successfully modified.")

            else:
                file = open(file_name, "r")
                data = file.readlines()
                file.close()

                for element in data:
                    identifiers_list = element.split(",")
                    if identifiers_list[att_index] != query[9]:
                        identifiers_list[att_index] = query[5]
                        identifiers_str = ",".join(identifiers_list)
                        modified_data.append(identifiers_str)
                        modify_count += 1
                    else:
                        modified_data.append(element)

                file = open(file_name, "w")
                for line in modified_data:
                    file.write(line)
                file.close()

                print(str(modify_count) + " lines were successfully modified.")

def FetchLines(query,file_names): #Rearange the longest line depneding on the wanted attrinutes and decrease the kength depending on the lnogest line
    file_name = query[3]

    if file_name not in file_names:
        print("There is no such file.")

    else:
        isAttributes_Okey = True
        wanted_atts =query[1].split(",")

        file = open(file_name, "r")
        attributes = file.readline()
        attributes = attributes.rstrip("\n")
        attributes = attributes.split(",")
        file.close()


        for wanted_att in wanted_atts:
            if not wanted_att in attributes:
                isAttributes_Okey = False
                break

        if not isAttributes_Okey:
            print("Your query contains an unknown attribute.")

        else:
            file = open(file_name,"r")
            lines = file.readlines()
            num_lines = len(lines) - 1
            file.close()


            modify_att = query[5]
            modify_index = 0
            indices = []
            for wanted_att in wanted_atts:
                index = 0
                for attribute in attributes:
                    if attribute == wanted_att:
                        break
                    else:
                        index += 1

                    if attribute == modify_att:
                        break
                    else:
                        modify_index += 1

                indices.append(index) # Found the wanted attributes' indices

            modify_count = 0
            output = []
            file = open(file_name, "r")
            att_line = file.readline() # File's attributes
            att_line_list = att_line.split(",")
            line = file.readline()
            while line != "":
                line = line.rstrip("\n")
                line_list = line.split(",")

                if query[6] == "==":
                    if line_list[modify_index] == query[7]:
                        line_str = ",".join(line_list)
                        output.append(line_str) # Found the fetched lines not in wanted format
                        modify_count += 1

                else:
                    if line_list[modify_index] != query[7]:
                        line_str = ",".join(line_list)
                        output.append(line_str) # Found the fetched lines not in wanted format
                        modify_count += 1

                line = file.readline()
            file.close()

            lengths = [] # List that contains the required longest words' length to assign columns
            for index in range(len(att_line_list)):
                longest = len(att_line_list[index])
                for element in output:
                    element = element.split(",")
                    if len(element[index]) > longest:
                        longest = len(element[index])
                lengths.append(longest)

            print("Number of lines in file students: " + str(num_lines))
            print("Number of lines that hold the condition: " + str(modify_count))

            acc = 0
            for a in lengths:
                acc += a
            longest_line = acc + len(lengths)*2 + (len(lengths)-1) +2

            print(longest_line * "-")
            line = "|"
            for index in indices:
                line = line + " " + "{:<{}}".format(attributes[index], lengths[index]) + " |"
            print(line)
            print(longest_line * "-")

            output_line_alligned = []
            for element in output:
                line = "|"
                element = element.split(",")
                for index in indices:
                    line = line + " " + "{:<{}}".format(element[index], lengths[index]) + " |"
                output_line_alligned.append(line)
            for _ in output_line_alligned:
                print(_)
            if len(output) != 0:
                print(longest_line * "-")

def isOperator(query_element):
    if query_element == "==" or query_element == "!=":
        return True
    else:
        return False

def isIdentifier(query_element):
    chars = ["_", ".", "@"]
    for char in chars:
        query_element = query_element.replace(char, "")
    if query_element.isalnum():
        return True
    else:
        return False

def isIdentifiers(query_element):
    query_element_list = query_element.split(",")
    for element in query_element_list:
        if not isIdentifier(element):
            return False
    return True

file_names= os.listdir()
for file in os.listdir():
    if file.endswith(".py"):
        file_names.remove(file)

query = input("What is your query?\n")
while query != "X":
    query = query.split(" ")
    query_len = len(query)

    if query_len == 5:
        if query[0] == "create" and query[1] == "file" and isIdentifier(query[2]) and query[3] == "with" and isIdentifiers(query[4]):
            Create(query,file_names)
        else:
            print("Invalid query.")

    elif query_len == 3:
        if query[0] == "delete" and query[1] == "file" and isIdentifier(query[2]):
            Delete(query,file_names)
        else:
            print("Invalid query.")

    elif query_len == 2:
        if query[0] == "display" and query[1] == "files":
            Display(file_names)
        else:
            print("Invalid query.")


    elif query_len == 4:
        if query[0] == "add" and isIdentifiers(query[1]) and query[2] == "into" and isIdentifier(query[3]):
            AddLine(query, file_names)
        else:
            print("Invalid query.")


    elif query_len == 8:
        if query[0] == "remove" and query[1] == "lines" and query[2] == "from" and isIdentifier(query[3]) and query[4] == "where" and isIdentifier(query[5]) and isOperator(query[6]) and isIdentifier(query[7]):
            RemoveLines(query,file_names)

        elif query[0] == "fetch" and isIdentifiers(query[1]) and query[2] == "from" and isIdentifier(query[3]) and query[4] == "where" and isIdentifier(query[5]) and isOperator(query[6]) and isIdentifier(query[7]):
            FetchLines(query,file_names)

        else:
            print("Invalid query.")


    elif query_len == 10:
        if query[0] == "modify" and isIdentifier(query[1]) and query[2] == "in" and isIdentifier(query[3]) and query[4] == "as" and isIdentifier(query[5]) and query[6] == "where" and isIdentifier(query[7]) and isOperator(query[8]) and isIdentifier(query[9]):
            ModifyLines(query,file_names)
        else:
            print("Invalid query.")


    else:
        print("Invalid query.")

    query = input("What is your query?\n")