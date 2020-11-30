from time import sleep
import sys

#def to run function print_slowly to print slooooowwwwwwwlllllyyy - args (text, number)
def print_slowly(text, time):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        sleep(time)


#run function
print_slowly('Hello World, ', 0.2)

#sleep a moment
sleep(0.2)

#print the babe and wait
print("BaBE")

#sleep for a moment
sleep(2)

#reticente
print_slowly('...', 0.2)

#print babe... just slowly and demands to change line
print_slowly("baaaaabe \n", 0.4)

#print with some delay Press enter...
print_slowly("Press Enter to continue...", 0.1)

#whait for enter
input()