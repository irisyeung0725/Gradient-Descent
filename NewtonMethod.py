import numpy as np # support for large, multi-dimensional arrays and matrices
from numpy.linalg import matrix_power # for handling matrices
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
count = 0
cont = True
while cont:

#   define the Hessian of the function
    H = np.array([[2, 1], [1, 6]])
    # calculate H^-1
    h = matrix_power(H, -1)     
    x = guesses[-1] # Always get the newest element from the array
    # deflect the gradient g
    g =  np.matmul(h, df(x)) # g = H^-1 * g
    # set fixed step size
    t_opt = 1 # step size = 1
    next_guess = x - t_opt * g
    guesses.append(next_guess)
    count += 1 # increase iteration    
#   Plot it
    plt.figure(3)
    plt.axis("equal")
    plt.contour(xmesh, ymesh, fmesh, 15)
    it_array = np.array(guesses)
    cdot = it_array[-1]
    plt.plot(it_array.T[0], it_array.T[1], "x-") # plot current point
    # set title, x and y label
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.title("f(x) = x1^2 + x1*x2 + 3*x2^2")
    # for loop stops when it reaches 0
    for element in guesses[-1]:
        if element == 0:
            print("Numbers of iterations:", count)
            cont = False
    print("The current dot is :", cdot)

            
    
    

plt.show(True)


