import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

intro = """
This problem is a one dimensional domain with a side source at both ends.
The strength of the source at each end is always the same.
This can also be used to test vacuum boundary conditions by setting MLeft = 0
"""

print(intro)

length = 1.0 # length of the 1d domain
Q = 1.0 # Source strength
sigt = 1.0 # macroscopic total xsection
sigs = 0.0 # macroscopic scatter xsection
num_pts = 100 # number of points used in plotting

MLeft = float(input('Please enter a strength for the side source. If you input zero it will be a vacuum problem: '))

D = 1/(3*sigt) # Diffusion coefficient
S = Q/D
siga = sigt-sigs # macroscopic absorption xsection
L = np.sqrt(D/siga)

alpha = S*L*L/(2*D) - 2*MLeft/D
beta = 1/L - 1/(2*D)
delta = 1/L + 1/(2*D)

pos_coeff = alpha/beta*1/( 1-delta/beta*np.exp(length/L) ) # coefficient infront of the exp(x/L) term
neg_coeff = pos_coeff * np.exp(length/L) # coefficient infront of the exp(-x/L)

flux = lambda x : pos_coeff*np.exp(x/L) + neg_coeff*np.exp(-x/L) + S*L*L

xs = np.linspace(0.0,length,num_pts)
r = list(map(flux,xs))

plot = input('Would you like to see a plot of the solution? (y/n): ')
if plot == 'y':
    fig, axes = plt.subplots(1,1)
    plt.plot(xs,r,label='Side Sources')
    plt.show()

# calclate the flux integral using quadrature
flux_integral = integrate.quad(flux,0,length)
print()
print("The flux integral for the sidesource solution is:", flux_integral)
average_flux = flux_integral[0]/length
print("The average integral for the sidesource solution is:", average_flux)
