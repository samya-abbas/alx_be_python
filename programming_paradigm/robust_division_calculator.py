def safe_divide(numerator, denominator):
  
    try:
        num_float = float(numerator)
        den_float = float(denominator)

        result = num_float / den_float
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
