def Countlines(filename):
    f = open(filename,"r")
    lines = f.readlines()
    total_lines = len(lines)
    return(total_lines)

Userfile = input("Enter the path of your file")
print("Your file contains",Countlines(Userfile),"lines")
