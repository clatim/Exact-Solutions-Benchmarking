import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

intro = """
This problem is a one dimensional domain with an albedo boundary condition at both ends.
The albedo alpha is always the same at both ends.
It can be used to test the following:
    -Vacuum boundary condition (alpha = 0)
    -Reflective boundary condition (alpha = 1)
    -General albedo boundary (0 < alpha < 1)
    -Extrapolated boundary condition (alpha = 0.031758)
"""

print(intro)

length = 1.0 # length of the 1d domain
Q = 1.0 # Source strength
sigt = 1.0 # macroscopic total xsection
sigs = 0.3 # macroscopic scatter xsection
num_pts = 100 # number of points used in plotting

alpha = float(input('Please enter the alpha (albedo coefficient). See above for what alpha should be: '))

D = 1/(3*sigt) # Diffusion coefficient
S = Q/D
siga = sigt-sigs # macroscopic absorption xsection
L = np.sqrt(D/siga)

Z = (1-alpha)/(1+alpha)
kappaP = (1/L + Z/(2*D))
kappaM = (1/L - Z/(2*D))

pos_coeff = 1/ ( 1- kappaP/kappaM*np.exp(length/L) ) * S*L*L*Z/(2*D*kappaM) # coefficient infront of the exp(x/L) term
neg_coeff = pos_coeff * np.exp(length/L) # coefficient infront of the exp(-x/L) term

flux = lambda x : pos_coeff*np.exp(x/L) + neg_coeff*np.exp(-x/L) + S*L*L

xs = np.linspace(0.0,length,num_pts)
r = list(map(flux,xs))


plot = input('Would you like to see a plot of the solution? (y/n): ')
if plot == 'y':
    fig, axes = plt.subplots(1,1)
    plt.plot(xs,r,label='Albedo problem')
    plt.show()

# calclate the flux integral using quadrature
flux_integral = integrate.quad(flux,0,length)
print()
print("The flux integral for the albedo solution is:", flux_integral)
average_flux = flux_integral[0]/length
print("The average integral for the albedo solution is:", average_flux)
