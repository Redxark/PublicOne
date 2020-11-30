from time import sleep
import sys

#def to run function print_slowly to print slooooowwwwwwwlllllyyy
def print_slowly(text):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.2)

def print_xtra_slowly(text):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.4)

#run function
print_slowly('Hello World, ')

#sleep a moment
sleep(0.2)

#print the babe and wait
print("BaBE")

#sleep for a moment
sleep(2)

#reticente
print_slowly('...')


#print babe... just slowly and demands to change line
print_xtra_slowly("baaaaabe \n")


#whait for enter
input("Press Enter to continue...")