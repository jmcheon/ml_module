import numpy as np
import matplotlib.pyplot as plt
import sys, os

path = os.path.join(os.path.dirname(__file__), '..', 'ex07')
sys.path.insert(1, path)
from vec_loss import loss_

def plot_with_loss(x, y, theta):
	"""
	Plot the data and prediction line from three non-empty numpy.ndarray.

	Args:
	x: has to be an numpy.ndarray, a vector of dimension m * 1.
	y: has to be an numpy.ndarray, a vector of dimension m * 1.
	theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.

	Returns:
	Nothing.

	Raises:
	This function should not raise any Exception.
	"""
	for v in [x, y, theta]:
		if not isinstance(v, np.ndarray):
			print(f"Invalid input: argument {v} of ndarray type required")	
			return

	if x.ndim == 1:
		x = x.reshape(x.size, 1)
	elif not (x.ndim == 2 and x.shape[1] == 1):
		print(f"Invalid input: wrong shape of {x}", x.shape)
		return

	if y.ndim == 1:
		y = y.reshape(y.size, 1)
	elif not (y.ndim == 2 and y.shape[1] == 1):
		print(f"Invalid input: wrong shape of {y}", y.shape)
		return
	
	if x.shape != y.shape:
		print("Invalid input: shapes of x, y should be indentical")
		return

	if theta.ndim == 1 and theta.size == 2:
		pass
	elif not (theta.ndim == 2 and theta.shape == (2, 1)):
		print("Invalid input: wrong shape of theta ", theta.shape)
		return

	X = np.hstack((np.ones((x.shape[0], 1)), x))
	y_hat = X.dot(theta)
	cost = loss_(y, y_hat.reshape(y_hat.size, 1)) * 2

	plt.scatter(x, y, color='blue', label='data points')
	plt.plot(x, y_hat, color='orange', label='prediction line')
	for xi, yi, y_hat_i in zip(x, y, y_hat):
		plt.plot([xi, xi], [yi, y_hat_i], '--', color='red')
	plt.legend()
	plt.title(f"Cost : {cost:.6f}")
	plt.show()


def ex1():
	x = np.arange(1,6)
	y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])

	# Example 1:
	theta1= np.array([18,-1])
	plot_with_loss(x, y, theta1)
	
	# Example 2:
	theta2 = np.array([14, 0])
	plot_with_loss(x, y, theta2)
	
	# Example 3:
	theta3 = np.array([12, 0.8])
	plot_with_loss(x, y, theta3)

def ex2():
	x = np.arange(1,6)
	y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
	#x = x.reshape(x.size, 1)
	#y = y.reshape(y.size, 1)
	#print("x:", x, x.shape)
	#print("y:", y, y.shape)

	#X = np.hstack((x, y))
	#print("X:", X, X.shape)

	# Example 1:
	theta1 = np.array([[4.5],[-0.2]])
	plot_with_loss(x, y, theta1)

	# Example 2:
	theta2 = np.array([[-1.5],[2]])
	plot_with_loss(x, y, theta2)

	# Example 3:
	theta3 = np.array([[3],[0.3]])
	plot_with_loss(x, y, theta3)

if __name__ == "__main__":
	ex1()
