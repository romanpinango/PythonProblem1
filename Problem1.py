# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

print("Problem 1")

# We ask the user which will be the limit to evaluate
limit = input("Define limit to evaluate: ")

# The sum of multiples of 3 and 5
sum = 0

# Iterate over numbers below max value
for x in range(int(limit)):
    if (x % 3 == 0 or x % 5 == 0):
        sum += x

# Show the result
print("With max " + limit + " the sum is: " + str(sum))
