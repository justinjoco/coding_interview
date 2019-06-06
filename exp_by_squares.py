'''
exp_by_squares.py

Algorithm:

x^n = x*(x^2)^((n-1)/2) if n is odd
    = (x^2)^(n/2) if n is even

'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return self.myPow(1/x , -n)
        if n%2 == 0:
            return self.myPow(x*x, n/2)
        if n%2 == 1:
            return x*self.myPow(x*x, (n-1)/2)