import time

import random

from os import system, name 

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
   
    else: 
        _ = system('clear')
clear()

fWrite = open("nums.txt", "w+")

fRead = open("nums.txt", "r")

randNums = []

avTime = []
avRunTime = []
runAverage = []
greatestTime = 0
leastTime = 100000

limit = 50 #number of numbers to sort
 
for i in range(1, limit + 1) :  
  randNums.append(i) #Generates numbers from 1 to limit

random.shuffle(randNums) #randomizes the numbers
tiOneOne = time.perf_counter()

input()

for i in range(0, limit - 1) : #main loop of sort
  for i in range(0, limit - 1) : #nested loop

    tiOne = time.perf_counter() #starts timer

    if randNums[i] > randNums[i + 1] : #compares current number to next
      numCheckOne = randNums[i]
      numCheckTwo = randNums[i+1]

      if numCheckOne > numCheckTwo :

        randNums[i] = numCheckTwo
        randNums[i+1] = numCheckOne 

      tiTwo = time.perf_counter() - tiOne

      print(randNums)
      clear() #constantly prints the numbers, without this, the script would be much more efficient in time saving, but doing this is not included in the averages, just the total time.
      print("\n")

      if tiTwo > greatestTime : #records longest time
        greatestTime = tiTwo

      if tiTwo < leastTime : #records shortest time
        leastTime = tiTwo

      avTime.append(tiTwo)

timetime = time.perf_counter() - tiOneOne

average = sum(avTime)/len(avTime)

#print all values

print("total time :", timetime)
print("average time :", average)
print("longest time :", greatestTime)
print("shortest time :", leastTime)

print(randNums)
