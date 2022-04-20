# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:49:31 2022

@author: Hernani
"""
# def multiply(number, multiplier):
    
#     """
#     :param number: The number to multiply
#     :type number: int
    
#     :param multiplier: The multiplier
#     :type multipliert: int
#     """
    
#     return number*multiplier

# # call function

# print(multiply(5,2))

from medium_multiply import Multiplication

# Instantiate a Multiplication object
multiplication = Multiplication(2)

# Call the multiply method
print(multiplication.multiply(5))

# build library -- python setup.py sdist bdist_wheel 
# test library-- twine check dist/* 
# upload to test pypi -- twine upload --repository-url https://test.pypi.org/legacy/ dist/*