# by Kami Bigdely
# Replace magic numbers with named constanst

# First Section
COULOMB_CONST = 8.9875517923*1e9


def calculate_force(q1, q2, distance):
    return COULOMB_CONST * q1 * q2 / (distance**2)


q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance between two charges: "))

force = calculate_force(q1, q2, distance)
print("Electric Force between q1 and q2 is: ", force, "Newton")

# Second Section
EVEN_OR_ODD_CONST = 0
num = int(input('Enter an integer number: '))
if num % 2 == EVEN_OR_ODD_CONST:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")
