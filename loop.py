# while True:
#     n = float(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(int(n)):

#     print("meow")

# MAKING THE COMPLETE WORKING CODE OUT OF THE ABOVE CODE 

def main():
    number = get_number() #calling the function
    meow(number)


def get_number():
    #writing code to accept positive integer only
    #this is allso for test purpose
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")
main()


this is the code to perform the test only.
after staging and before commiting the file i have made this changes which is want to reflect in this commit