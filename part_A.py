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

    num_lst = [1, 2, 3, 4, 5]               #Sequence to be deviated THIS SHOULD BE PUT IN MAIN FUNCTION
    sum_lst = 0                             # Sum of list
    num_lst_squared = []                    # Sequence squared to be used in order to calculate the mean of squares
    sum_lst_squared = 0                     # Sum of the list squared
    N = num_lst[-1]                         # Last number in list
    
    for i in num_lst:                       # Summarizing sequence
        sum_lst = sum_lst + num_lst[i-1]

    x = (1/N) * sum_lst                     #calculate the mean x

    #Square all elements in num_list and sum together

    for i in num_lst:
        num_lst_squared.append(num_lst[i-1]**2)
        sum_lst_squared = sum_lst_squared + num_lst_squared[i-1]

    # Calculate the mean of suqres S
    S = (1/N) * sum_lst_squared

    O2 = S - x**2                           # Computing the variance O2

    O = sqrt(O2)                            # computing the standard deviation O 

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
    num_lst = [1, 2, 3, 4, 5]
    sum_lst = sum(num_lst)
    num_lst_squared = []
    N = len(num_lst)

    x = (1/N) * sum_lst                     #calculate the mean x

        #Square all elements in num_list and sum together

    for i in num_lst:
        num_lst_squared.append(num_lst[i-1]**2)
        sum_lst_squared = sum(num_lst_squared)
        # Calculate the mean of suqres S
    S = (1/N) * sum_lst_squared

    O2 = S - x**2                           # Computing the variance O2

    O = sqrt(O2)                            # computing the standard deviation O 

def main():

# sum fuction print(sum_sequence.sum())