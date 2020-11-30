from time import sleep
import sys

# print("Hello World, ")
# time.sleep(1)
# print("babe")
# time.sleep(5)



def print_slowly(text):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.2)


print_slowly('Hello World, ')
sleep(0.2)
print("BaBE")
sleep(5)