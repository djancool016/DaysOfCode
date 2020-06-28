def inputMethod(source):
    file1 = open(source, "r")
    Lines = file1.readlines()
    file1.close()
    return Lines

