import numpy as np # support for large, multi-dimensional arrays and matrices
import numpy.linalg as la  # Linear algebra
import matplotlib.pyplot as plt # Useful plotting tool for data visualization
from mpl_toolkits.mplot3d import axes3d # Plot the 3d graph
import matplotlib

def f(x):
    '''
    Define the objective function
    '''
    return x[0]**2 + x[0]*x[1] + 3*x[1]**2

def df(x):
    '''
    Define the gradient of the objective
    '''
    return np.array([2*x[0] + x[1], x[0] + 6*x[1]])

# Using axes3d to plot the 3d shape
fig = plt.figure(1)
ax = fig.gca(projection="3d")
xmesh, ymesh = np.mgrid[-5:5:50j,-5:5:50j]
fmesh = f(np.array([xmesh, ymesh]))
ax.plot_surface(xmesh, ymesh, fmesh)
plt.show(False)


# Plot the contour graph of the function
plt.figure(2)
plt.axis("equal")
plt.contour(xmesh, ymesh, fmesh, 15)

plt.show(False)


guesses = [np.array([3, 3])] # starting point
count = 0
while count <= 9:
#     Calculate the gradient
    x = guesses[-1] # Always get the newest element from the array
    g = -df(x) # best improving direction
    t_opt = 0.1 # step size = 0.1
    next_guess = x + t_opt * g
    guesses.append(next_guess)
    print("The current dot is :", x)
    print("g =", g)
#     Plot it
    plt.figure(3)
    plt.axis("equal")
    plt.contour(xmesh, ymesh, fmesh, 15)
    it_array = np.array(guesses)
    plt.plot(it_array.T[0], it_array.T[1], "x-") # plot current point
    count += 1 # increase iteration
   

plt.show(True)

print("Numbers of iterations :", count)

