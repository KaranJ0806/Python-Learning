# recursion : the function will call itself

# def calc_factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * calc_factorial(num - 1)
# print(calc_factorial(3))



# Dictionary 

# Key              Value 
#laptop ->  an electronic device 
# curly bracket in used for dictionary to indicate the dictionary

# dict = {'name': 'karan', 'college': 'adypu', 'marks': '50'}

# print(dict)
# print(dict['name']) # karan will be printed 




#Create a clock program 

# HH:MM:SS
# 00:00:01
# 13:20:23
# 24 hours system

# import time

# hh = 24
# mm = 60
# ss = 60 
# for seconds in range (ss):
#     print ('seconds:', seconds)
#     time.sleep(1)

import time

hh = 24
mm = 60
ss = 60
while True:
    for hours in range(hh):
        for minutes in range(mm):
            for seconds in range(ss):
                display_hour = hours % 12 or 12
                period = "AM" if hours < 12 else "PM"
                print(f"{display_hour:02d}:{minutes:02d}:{seconds:02d} {period}")
                time.sleep(1)


# import time

# while True:
# 	print(time.strftime("%I:%M:%S %p"), end="\r", flush=True)
# 	time.sleep(1)

