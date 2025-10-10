#Understand
'''
print a message to the user, based on the number of hours slept.

'''

def sleep_assessment(hours):
    if hours > 10:
        print ("You're a sleep prodigy!")

    elif hours < 8:
        print ("Oof, go back to bed!")

    else:
        print ("You got a good night's rest!")

#test cases
sleep_assessment(10)
sleep_assessment(4)
sleep_assessment(12)
sleep_assessment(9)