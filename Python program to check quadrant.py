Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================================ RESTART: Shell ================================
>>> #take inputs for X and Y
X  = int(input('Enter value for X-axis :'))
Y = int(input('Enter value for Y-axis :'))
#check for 1st quadrant
if X > 0 and Y > 0:
    print('X and Y lie at First quadrant')
#check for 2nd quadrant
elif X < 0 and Y > 0:
    print('X and Y lie at Second quadrant')
#check for 3rd quadrant
elif X < 0 and Y < 0:
    print('X and Y lie at Third quadrant')
#check for fourth quadrant
elif X > 0 and Y < 0:
    print('X and Y lie at Fourth quadrant')
else: 
    print('X and Y lie at Origin')