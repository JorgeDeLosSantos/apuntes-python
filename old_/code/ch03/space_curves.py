from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

base_dir = r"C:\Users\delos\Google Drive\Apuntes - Python\img\ch03\\"

def parametric_curve_01():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    t = np.linspace(0, 4*np.pi, 100)
    x = np.cos(t)
    y = np.sin(t)
    z = t

    ax.plot(x, y, z)
    plt.savefig(base_dir+"parametric_curve_01.pdf")
    plt.show()

def parametric_curve_02():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    t = np.linspace(0, 4*np.pi, 100)
    x = np.cos(t)
    y = np.sin(t)
    z = t

    ax.plot(x, y, z, color="r", linewidth=3)
    xticks = ax.get_xticks()
    yticks = ax.get_yticks()
    ax.set_xticks(xticks[::3])
    ax.set_yticks(yticks[::3])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.savefig(base_dir+"parametric_curve_02.pdf")
    plt.show()


if __name__ == "__main__":
    parametric_curve_02()
