""" Docstring :
This programme is supposed to take user input until user presses enter and then sums it up and averages it.
pseudo :take user input if the input is " else take user input 
"""

count=0
theSum=0
while True:
    number = input("Enter number here: ")
    if number=='':
        break
    realNumber=int(number)
    theSum += realNumber
    count+= 1

print(theSum)
print((theSum/count))

