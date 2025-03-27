# 1. SyntaxError
try:
    print("Hello World")  # Fixed missing closing parenthesis
except SyntaxError as e:
    print(f"SyntaxError handling: {e}")
finally:
    print("\n---\n")

# 2. NameError
try:
    a = 10  # Defined 'a' to fix the error
    print(a)  # Now 'a' is defined
except NameError as e:
    print(f"NameError handling: {e}")
finally:
    print("\n---\n")

# 3. TypeError
try:
    x = "hello" + str(5)  # Corrected by converting the number 5 to a string
except TypeError as e:
    print(f"TypeError handling: {e}")
finally:
    print("\n---\n")

# 4. ValueError
try:
    x = int("123")  # Corrected by passing a valid number as string
except ValueError as e:
    print(f"ValueError handling: {e}")
finally:
    print("\n---\n")

# 5. IndexError
try:
    lst = [1, 2, 3]
    print(lst[2])  # Changed index to 2 (valid index)
except IndexError as e:
    print(f"IndexError handling: {e}")
finally:
    print("\n---\n")

# 6. KeyError
try:
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['b'])  # Accessing an existing key ('b')
except KeyError as e:
    print(f"KeyError handling: {e}")
finally:
    print("\n---\n")

# 7. AttributeError
try:
    x = [1, 2, 3]
    x.append(4)  # Corrected to append to the list (not an int)
except AttributeError as e:
    print(f"AttributeError handling: {e}")
finally:
    print("\n---\n")

# 8. FileNotFoundError
try:
    with open("existing_file.txt", "w") as file:  # Using an existing file
        file.write("Hello, world!")
except FileNotFoundError as e:
    print(f"FileNotFoundError handling: {e}")
finally:
    print("\n---\n")

# 9. ZeroDivisionError
try:
    x = 10 / 2  # Fixed by dividing by a non-zero number
except ZeroDivisionError as e:
    print(f"ZeroDivisionError handling: {e}")
finally:
    print("\n---\n")

# 10. OverflowError
try:
    import math
    x = math.exp(100)  # Reduced value to avoid overflow
except OverflowError as e:
    print(f"OverflowError handling: {e}")
finally:
    print("\n---\n")

# 11. ImportError
try:
    import math  # Correctly importing an existing module
except ImportError as e:
    print(f"ImportError handling: {e}")
finally:
    print("\n---\n")

# 12. StopIteration
try:
    my_list = iter([1, 2, 3])
    print(next(my_list))
    print(next(my_list))
    print(next(my_list))
    print(next(my_list))  # Will raise StopIteration
except StopIteration as e:
    print(f"StopIteration handling: {e}")
finally:
    print("\n---\n")

# 13. MemoryError
try:
    lst = [1] * (10**7)  # Reduced the size of the list to avoid memory issues
except MemoryError as e:
    print(f"MemoryError handling: {e}")
finally:
    print("\n---\n")

# 14. NotImplementedError
try:
    def my_function():
        pass  # Functionality implemented
    my_function()  # This won't raise an error anymore
except NotImplementedError as e:
    print(f"NotImplementedError handling: {e}")
finally:
    print("\n---\n")
