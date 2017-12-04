# Exercise 23 from http://www.practicepython.org
# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a
#  list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
with open('primes.txt', 'r') as f:
    primes = [int(line.strip()) for line in f]

print(primes)

with open('happy.txt', 'r') as f:
    happy_numbers = [int(line.strip()) for line in f]

print(happy_numbers)

overlapping = [element for element in happy_numbers if element in primes]
print(overlapping)





