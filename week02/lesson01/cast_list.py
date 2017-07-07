def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    file = open(filename)
    for line in file:
        cast_list.append(line.split(",")[0].strip())
    file.close()

    return cast_list


def create_cast_list2(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename) as file:
        for line in file:
            cast_list.append(line.split(",")[0].strip())
    file.close()

    return cast_list