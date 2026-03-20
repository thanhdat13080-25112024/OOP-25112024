#1.How many seconds are there in 42 minutes 42 seconds?
min = 42
sec = 42
total_sec = min * 60 + sec
print("There are", total_sec, "seconds in 42 minutes 42 seconds.")

#2. How many miles are there in 10 kilometers? (Hint: 1 mile is 1.61 kilometers)
km = 10
miles = km / 1.61
print("There are", round(miles, 2), "miles in 10 kilometers.")

#3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?
total_time_sec = min * 60 + sec
pace_sec_per_mile = total_time_sec / miles
pace_min_per_mile = pace_sec_per_mile // 60
pace_sec_per_mile = pace_sec_per_mile % 60
print("Your average pace is", pace_min_per_mile, "minutes and", round(pace_sec_per_mile, 2), "seconds per mile.")

total_time_hours = total_time_sec / 3600
average_speed = miles / total_time_hours
print("Your average speed is", round(average_speed, 2), "miles per hour.")