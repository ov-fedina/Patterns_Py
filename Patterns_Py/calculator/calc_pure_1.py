print ('Welcome to Calculator!') # Output "Welcome to Calculator"!
q1 = int (input('Enter number 1: ')) # # Display the sum of two numbers entered by the user
q2 = int (input('Enter number 2: '))

v = int (input('What operation do you want to perform? \n 1 Addition \n 2 Subtraction \n 3 Division \n 4 Multiplication \n'))

if v == 1:
    r = q1 + q2
    p = 'Addition'
    t = p
if v == 2:
    r = q1 - q2
    l = 'Subtraction'
    t = l
if v == 3:
    r = float(q1 / q2)
    m = 'Division'
    t = m
if v == 4:
    r = q1 * q2
    n = 'Multiplication'
    t = n
print ('Result ',t,' = ',r)


