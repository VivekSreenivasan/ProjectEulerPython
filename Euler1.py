#For Project Euler Problem 1
#Answer was correct with 233168
counter = 0
for c in range(1,1000):
   if c % 3 == 0:
       counter = counter + c
   elif c%5 == 0:
       counter = counter + c
print (counter)
