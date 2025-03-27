# Python code to illustrate 
# working of try()  

def divide(x, y): 
    try: 
        # Floor Division : Gives only Fractional 
        # Part as Answer 
        result = x // y 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 
    else:
        print("Yeah ! Your answer is :", result) 
    finally:  
        # this block is always executed   
        # regardless of exception generation.  
        print('This is always executed')   

# Look at parameters and note the working of Program 
divide(6, 2) # 3 // 2 da 1
divide(3, 0) # 3 // 0 genera un ZeroDivisionError


#Example 2 multiple except block 
"""Ejemplo con múltiples bloques de excepción"""

'''try:
    num = int(input("Enter a number: "))  # Try to convert user input to an integer
    result = 10 / num  # Try dividing 10 by the input number
except ValueError:  # Handles case when input is not a number
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:  # Handles division by zero
    print("You can't divide by zero!")
else:
    print(f"Result: {result}")  # Executes only if no exception occurs
finally:
    print("Execution complete.")  # Always executes'''







