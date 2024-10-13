def safe_divide(numerator, denominator):
    """Performs division while handling errors like division by zero and non-numeric inputs."""
    try:
        # Convert input to float
        num = float(numerator)
        denom = float(denominator)
        
        # Attempt division
        result = num / denom
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
