#Completed Project Euler Problem 2
#Answer: 4613732
firstTerm = 1
secondTerm = 2
counter = 0
temp = 0

while temp < 4000000:
    
    if temp % 2 == 0:
        counter = counter + temp
    temp = firstTerm + secondTerm    
    
    if firstTerm % 2 == 0:
        counter = counter + firstTerm
    firstTerm = temp + secondTerm    
    
    if secondTerm % 2 == 0:
        counter = counter + secondTerm
    secondTerm = firstTerm + temp
    
    print (counter)
    
