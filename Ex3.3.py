def row_collum():
    n = int(input("Enter the row: "))
    row = " - - - - "
    collum = "+\n|\n|\n|\n|\n+"
    print(collum + row + (n-1)*row + collum)
row_collum()