#Ex3.3
#1. Write a function that draws a grid like the following:
for i in range(2):
    print("+  --  --  --  --  +" + "  --  --  --  --  +" + "\n")
    for j in range(4):
        print("|                  |" + "                  |" + "\n")
print("+  --  --  --  --  +" + "  --  --  --  --  +")
#-------------------------------------------------------------------------------------------------------------------------------------
print("\n\n\n\n")

#2. Write a function that draws a similar grid with four rows and four columns
for i in range(4):
    print("+  --  --  --  --  +" + "  --  --  --  --  +" * 3 + "\n")
    for j in range(4):
        print("|                  |" + "                  |" * 3 + "\n")
print("+  --  --  --  --  +" + "  --  --  --  --  +" * 3)
#-------------------------------------------------------------------------------------------------------------------------------------
#PS: The program can print the number of rows and columns based on the parameters.

def Rec():
    r = int(input("Enter the row: "))
    c = int(input("Enter the collum: "))
    for i in range(r):
        print("+  --  --  --  --  +" + "  --  --  --  --  +" * (c - 1) + "\n")
        for j in range(4):
            print("|                  |" + "                  |" * (c - 1) + "\n")
    print("+  --  --  --  --  +" + "  --  --  --  --  +" * (c - 1))