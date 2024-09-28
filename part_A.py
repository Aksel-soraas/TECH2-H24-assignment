"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
import numpy as np
from math import sqrt

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

    # Define variables to be used in the function

    sum_lst = 0                             # Sum of list
    num_lst_squared = []                    # Sequence squared to be used in order to calculate the mean of squares
    sum_lst_squared = 0                     # Sum of the list squared
    N = 0                                   # Will be used to define elements

    for i in x:                       # Summarizing sequence and counting elements
        sum_lst = sum_lst + i
        N += 1

    m = (1/N) * sum_lst                     #calculate the mean m

    #Square all elements in num_list and sum together

    for i in x:
        num_lst_squared.append(i**2)
    
    for i in num_lst_squared:
        sum_lst_squared = sum_lst_squared + i

    # Calculate the mean of suqres S
    S = (1/N) * sum_lst_squared

    O2 = S - m**2                           # Computing the variance O2

    O = sqrt(O2)                       # computing the standard deviation O 

    return O


def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

    # Define variables to be used in the function
    sum_lst = sum(x)
    num_lst_squared = []
    N = len(x)

    m = (1/N) * sum_lst                     #calculate the mean m

    #Square all elements in num_list and sum together
    for i in x:
        num_lst_squared.append(i**2)

    sum_lst_squared = sum(num_lst_squared)

    # Calculate the mean of suqres S
    S = (1/N) * sum_lst_squared

    O2 = S - m**2                           # Computing the variance O2

    O = sqrt(O2)                            # computing the standard deviation O 

    return O

def main():
    x = [1, 2, 3, 4, 5]
    
    looped = std_loops(x)

    builtin = std_builtin(x)

    std_function = np.std(x)
    
    print(f'Deviation by loops is {looped}, and by built in functions {builtin} and using the function from numpy {std_function}')
    return looped, builtin

if __name__ == "__main__":
    main()
