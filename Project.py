# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:39:14 2025

@author: computershop.mn
"""
#Algorithm EuclideanGCD(a, b)
#    Input: Two positive integers a and b
#    Output: Greatest common divisor of a and b
#    If b = 0 then
#        Return a
#    Else
#        Return EuclideanGCD(b, a mod b)
#    End If
#End Algorithm

#create a class
class EuclideanAlgorithm:
    #create a function to devide the inputs
    def gcd(a: int, b: int) -> int:
        while b != 0:
            temp = b #have the input of b set temporary
            b = a % b #have a new value for b set as the devided remainder of a and b
            a = temp #change the value of a to the old b
        return a
#create a function for the main calculations
def main():
    #orint a sentence as a start
    print("Euclidean Algorithm!")
    try:
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))
        if a <= 0 or b <= 0:
            raise ValueError("Both numbers must be positive integers.")
       
        
        gcd = EuclideanAlgorithm.gcd(a, b)
        print(f"The GCD of {a} and {b} is: {gcd}")
    #print the sentence when given a letter instead of a number integer
    except ValueError:
        print("Invalid input! Please enter integers.")
#to make the "main" function run
if __name__ == "__main__":
    main()
