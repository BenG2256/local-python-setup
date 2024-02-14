# def pos_num(n):
    
#     if n == 0:
#         return
    
#     else:
#         print(n)
#         pos_num(n-1)
        
# pos_num(7)

# def natural_numbers(x):
    
#     if x <= 0:
#         return
    
#     else:
#         print(x)
#         natural_numbers(x - 1)
        
# natural_numbers(9)

# def nth_fibbonacci(n):
#   if n<= 0:
#     print("Incorrect input")
#   # First Fibonacci number is 0
#   elif n == 1:
#     return 0
#   # Second Fibonacci number is 1
#   elif n == 2:
#     return 1
#   else:
#     return nth_fibbonacci(n-1)+nth_fibbonacci(n-2)
# print("2nd fib number:")
# print(nth_fibbonacci(2))
# print("4th fib number:")
# print(nth_fibbonacci(4))
# print("8th fib number:")
# print(nth_fibbonacci(8))


# def power(a, b):
#     if b < 1:
#         print("nope")
#     elif b == 1:
#         return a
#     else: 
#         return a * power(a, b-1)
    
# print(power(2,4))

# def is_palindrome(str):
#   if len(str) == 1 or len(str) == 0:
#     return True
#   else:
#     return (str[0] == str[-1]) and is_palindrome(str[1:-1])

# print("is 'apple' a palindrome?")
# print(is_palindrome('apple'))
# print("is 'tacocat' a palindrome?")
# print(is_palindrome('tacocat'))
    