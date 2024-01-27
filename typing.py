from time import *
import random as r

def mistake(par_test, user_test):
        error = 0
        for i in range(len(par_test)):
                try:
                        if par_test[i] != user_test[i]:
                                error = error + 1
                except :
                               error = error + 1
        return error 
            
def speed_time(time_s,time_e,userinput):
        time_delay = time_e - time_s
        time_R = round(time_delay,2)
        speed = len(userinput)/time_R
        return round(speed)


test = ["A quick brown fox jumped over the lazy dog", 
        "The greatest glory in living lies not in never falling, but in rising every time we fall",
        "The future belongs to those who believe in the beauty of their dreams",
        "You must be the change you wish to see in the world"]
test1 = r.choice(test)      
print("\n----------------------------------\n*****Test your typing speed*****\n----------------------------------\n")
print(test1)
print()
print()

time_1 = time()
testinput=input("Start Typing : ")
time_2 = time()

print('Typing Speed = ', speed_time(time_1,time_2,testinput), " Words/sec")
print("Errors made: ",mistake(test1,testinput))
