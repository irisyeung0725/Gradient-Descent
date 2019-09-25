import numpy as np # support for large, multi-dimensional arrays and matrices
import numpy.linalg as la  # Linear algebra
import matplotlib.pyplot as plt # Useful plotting tool for data visualization
from mpl_toolkits.mplot3d import axes3d # Plot the 3d graph
import matplotlib

def f(x):
    '''
    Define the objective function
    '''
    return x[0]**2 + x[0]*x[1] + 3*x[1]**2 # python starts from 0

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
# termination tolerance
tol = 1e-6
# maximum number of allowed iterations
maxiter = 1000;
# minimum allowed perturbation
dxmin = 1e-6 
dx = float('Inf') # set dx as an infinit number
gnorm = float('Inf') # set gnorm as an infinit number
count = 0
while  (gnorm >= tol and (count <= maxiter and dx >= dxmin)) :
#     Calculate the gradient
    x = guesses[-1] # Always get the newest element from the array
    g = -df(x)# best improving direction
    # set fixed step size
    t_opt = 0.1 # step size = 1
    
    # take step and caculate the next dot
    next_guess = x + t_opt * g
    guesses.append(next_guess)
    gnorm = la.norm(-g)

    print("The current point is :", x)
    print("g =", g)

    # update termination metrics
    dx = la.norm(next_guess - x)
    count += 1 # increase iteration
    # Plot it
    plt.figure(3)
    plt.axis("equal")
    plt.contour(xmesh, ymesh, fmesh, 15)
    it_array = np.array(guesses)
    plt.plot(it_array.T[0], it_array.T[1], "x-") # plot current point
    # set title, x and y label
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.title("f(x) = x1^2 + x1*x2 + 3*x2^2")
    
print("Numbers of iterations :", count - 1)

plt.show(True)



