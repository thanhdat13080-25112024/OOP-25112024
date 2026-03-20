#       The volume of a sephere with radius r is 4/3pir^3.What is the volume of a sephere with radius 5?
import math
r = 5
volume = 4 / 3 * math.pi * math.pow(r, 3)
print(f"The volume of a sephere with radius 5 is {round(volume, 3)}")


#       Suppost the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping cost $3
#       for the first copy and 75 cent for each additional copy. What is the total wholesale cost for 60 copies?

book = 24.95 * (1 - 0.4)
ship = 59 * 0.75 + 3
price = 60 * book + ship
print(f"The price for 60 books is ${round(price, 3)}")

#       If i leave my house at 6:52 am and run 1 mile at an easy pace(8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at 
#       easy pace again, what time do I get home for breakfast?