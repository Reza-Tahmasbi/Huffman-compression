for i in range(112, 501):
    filename = str(i) + ".txt"
    with open(filename, "w") as file:
        file.write("This is the content of file " + filename)