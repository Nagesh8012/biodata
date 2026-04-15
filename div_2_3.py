###python program to check whether a number is divisible by both 2 and 3:
##num=int(input("Enter a number:"))
##if num%2==0 and num%3==0:
##    print("The number is divisible by both 2 and 3.")
##else:
##    print("The number is not divisible by both 2 and 3.")
###num %2==0 checks divisibility by 2
###num %3==0 checks divisibilit by 3
###The and opeartor ensures both conditions are true
    

#using functions
def check_divisibility(num):
    if num%2==0 and num%3==0:
        return "The number is divisible by both 2 and 3."
    else:
        return "The number is not divisible by both 2 and 3."

# Example usage
number=int(input("Enter a number:"))
print(check_divisibility(number))
