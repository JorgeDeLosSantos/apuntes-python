import matplotlib.pyplot as plt
import numpy as np

base_dir = r"C:\Users\delos\Google Drive\Apuntes - Python\img\ch03\\"

def polar_01():
    theta = np.linspace(0, 2*np.pi, 1000)
    a,k,phi0 = 5,7,0
    r = a*np.cos(k*theta + phi0)
    plt.polar(theta, r, "r")
    plt.savefig(base_dir+"polar_01.pdf")
    plt.show()


if __name__ == "__main__":
    polar_01()
