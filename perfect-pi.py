#!/usr/bin/env python3

# Look Ma! No math! (library)

# lucky complex numbers are built-in for python...
i = complex(0,1)

# n!=n*n-1*...*1
factorial = lambda n : n*factorial(n-1) if n >= 2 else 1

# exp(z)=e^z=sum(z^k/k!,k=0..infinity), or 100 is good enough for us,
exp = lambda z : sum([z**k/factorial(k) for k in range(100)])


# Use "The Most Beautiful Equation in Mathematics" to solve for pi
#
#   exp(i*pi)+1 = 0

f = lambda z : exp(i*z)+1
df = lambda z : i*exp(i*z)

# Start from a really bad estimate for pi
z = 4

for it in range(10):
    z=z-f(z)/df(z)
    
print(z)
