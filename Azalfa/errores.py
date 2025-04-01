# 1. SyntaxError
try:
    print("Hello World" # Missing closing parenthesis
except SyntaxError as e:
    print(f"SyntaxError handling: {e}")
finally:
    print("\n---\n")

# 2. NameError
try:
    print(a)  # 'a' is not defined
except NameError as e:
    print(f"NameError handling: {e}")
finally:
    print("\n---\n")

# 3. TypeError
try:
    x = "hello" + 5  # Can't add a string and a number
except TypeError as e:
    print(f"TypeError handling: {e}")
finally:
    print("\n---\n")

# 4. ValueError
try:
    x = int("hello")  # Can't convert a non-numeric string to an integer
except ValueError as e:
    print(f"ValueError handling: {e}")
finally:
    print("\n---\n")

# 5. IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])  # Index out of range
except IndexError as e:
    print(f"IndexError handling: {e}")
finally:
    print("\n---\n")

# 6. KeyError
try:
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['c'])  # Key 'c' doesn't exist
except KeyError as e:
    print(f"KeyError handling: {e}")
finally:
    print("\n---\n")

# 7. AttributeError
try:
    x = 5
    x.append(10)  # 'int' object has no attribute 'append'
except AttributeError as e:
    print(f"AttributeError handling: {e}")
finally:
    print("\n---\n")

# 8. FileNotFoundError
try:
    with open("nonexisting_file.txt", "r") as file:
       content = file.read()  
       print(content)
except FileNotFoundError as e:
    print(f"FileNotFoundError handling: {e}")
finally:
    print("\n---\n")

# 9. ZeroDivisionError
try:
    x = 10 / 0  # Division by zero
    print(x)
except ZeroDivisionError as e:
    print(f"ZeroDivisionError handling: {e}")
finally:
    print("\n---\n")

# 10. OverflowError
try:
    import math
    x = math.exp(1000)  # Exceeds the maximum size
    print(x)
except OverflowError as e:
    print(f"OverflowError handling: {e}")
finally:
    print("\n---\n")

# 11. ImportError
try:
    import no  # Module not found
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
except StopIteration:
    print(f"No more items!")
finally:
    print("\n---\n")

# 13. MemoryError
try:
    lst = [1] * (10*10)
    print(lst)  # Trying to create a huge list
except MemoryError as e:
    print(f"MemoryError handling: {e}")
finally:
    print("\n---\n")

# 14. NotImplementedError
try:
    def my_function():
        raise NotImplementedError("This functionality is not implemented yet")
    
    my_function()  # This will raise NotImplementedError
except NotImplementedError as e:
    print(f"NotImplementedError handling: {e}")
finally:
    print("\n---\n")