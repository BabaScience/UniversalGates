def NAND(a, b):
    """
    Perform the NAND operation on two binary inputs.
    
    Parameters:
    - a (int): A binary input, either 0 or 1.
    - b (int): Another binary input, either 0 or 1.
    
    Returns:
    int: The result of the NAND operation.
    """
    # Use the NOT operation on the result of the AND operation.
    return not (a and b)