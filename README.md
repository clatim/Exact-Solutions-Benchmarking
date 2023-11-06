These files contain python scripts that evaluate exact solutions of the 1D transport equation. 
There are files for zero flux, albedo, and side source, and most of them have some parameters in them that allow you to solve other cases (e.g run albedo and set alpha = 1 is a reflective boundary condition)

I wrote and ran these codes using Python3 (Python3.6 in particular), maybe they will work with Python2, I do not know.

To run them you will need to install the following things (at least, maybe more):
	- Python 3
	- SciPy for Python3
	- NumPy for Python3
	- matplotlib for Python3
Make sure you do not install the Python 2 versions.

Hopfully the files are self explanatory and hopefully they work. They did for me but that doesn't mean they are fool proof.
They are more likely to be right if coefficients are 1.0 etc. 

You can get them to plot out the solutions which you can use to eyeball your own calculations. They also output the integral of the flux over the entire domain
and the average flux (which I took as the integral of the flux over the entire domain divided by the size of the domain)

HOPE IT HELPS!
