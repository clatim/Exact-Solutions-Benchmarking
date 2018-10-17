import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

intro = """
This problem is a one dimensional domain with a zero flux (homogenous Dirichlet) boundary condition at both ends.
"""

print(intro)

length = 1.0 # length of the 1d domain
Q = 1.0 # Source strength
sigt = 1.0 # total xsection
sigs = 0.0 # scattering xsection
num_pts = 100 # number of points to use in plotting


D = 1/(3*sigt) # diffusion coefficient
S = Q/D
siga = sigt-sigs # macroscopic absorption xsection
L = np.sqrt(D/siga)

neg_coeff=S*L*L*(np.exp(length/L)-1)/(np.exp(-length/L)-np.exp(length/L)) # The coefficient infront of the exp(-x/L) term
pos_coeff=-(S*L*L+neg_coeff) # The coefficient infront of the exp(x/L) term

flux = lambda x : pos_coeff*np.exp(x/L) + neg_coeff*np.exp(-x/L) + S*L*L

xs = np.linspace(0.0,length,num_pts)
r = list(map(flux,xs))

plot = input('Would you like to see a plot of the solution? (y/n): ')
if plot == 'y':
    fig, axes =  plt.subplots(1,1)
    plt.plot(xs, r, label='Zero Flux')
    plt.show()


#calculate integral of flux over the domain
flux_integral = integrate.quad(flux, 0, length)
print()
print("The flux integral for the zero flux solution is:", flux_integral)
average_flux = flux_integral[0]/length
print("The average integral for the zero flux solution is:", average_flux)
