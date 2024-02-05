''' Augmented Assignment Operators:

Combine assignment and operation (e.g., x += 5 is equivalent to x = x + 5).
Augmented assignment operators provide a concise way to perform operations and assign the result back to the variable in a single step.
They are often used to update variables within loops, calculations, and data manipulations.
Choose the appropriate operator based on the desired operation and data types involved.
'''
#1. Arithmetic Operations:

#+=: Add and assign:

count = 0
count += 5  # Equivalent to count = count + 5
print(count)  # Output: 5

#-=: Subtract and assign:
balance = 100
balance -= 25  # Equivalent to balance = balance - 25
print(balance)  # Output: 75

#*=: Multiply and assign:
price = 15
price *= 2  # Equivalent to price = price * 2
print(price)  # Output: 30

#/=: Divide and assign:

total = 100
total /= 4  # Equivalent to total = total / 4
print(total)  # Output: 25.0

#//=: Floor divide and assign:

minutes = 67
hours = minutes // 60  # Equivalent to hours = minutes // 60
print(hours)  # Output: 1


#%=: Modulo and assign:

number = 17
remainder = number % 5  # Equivalent to remainder = number % 5
print(remainder)  # Output: 2

#**=: Raise to a power and assign:

base = 2
result = base ** 3  # Equivalent to result = base ** 3
print(result)  # Output: 8


#2. Bitwise Operations:

#&=: Bitwise AND and assign:

flags = 0b1110  # Binary 14
flags &= 0b0101  # Equivalent to flags = flags & 0b0101
print(flags)  # Output: 4 (binary 0100)

#|=: Bitwise OR and assign:

permissions = 0b1010  # Binary 10
permissions |= 0b0011  # Equivalent to permissions = permissions | 0b0011
print(permissions)  # Output: 13 (binary 1101)

#^=: Bitwise XOR and assign:

data = 0b1100  # Binary 12
data ^= 0b0111  # Equivalent to data = data ^ 0b0111
print(data)  # Output: 7 (binary 0111)

#<<=: Left shift and assign:

number = 8  # Binary 1000
number <<= 2  # Equivalent to number = number << 2
print(number)  # Output: 32 (binary 100000)

#>>=: Right shift and assign:

value = 64  # Binary 1000000
value >>= 3  # Equivalent to value = value >> 3
print(value)  # Output: 8 (binary 1000)

