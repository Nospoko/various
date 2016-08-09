import numpy as np
from mayavi import mlab

def main():
    """ Mejn """
    # One figure is enough for one run?
    # This does not seem like a fine design
    fig = mlab.figure(fgcolor = (1, 1, 1),
                      bgcolor = (0.0, 0.0, 0.0))

    t = np.linspace(0, 10, 1001)
    x = np.cos(t)
    y = np.sin(3*t)
    z = np.cos(2*t)

    color = np.sin(y)**2

    yo = mlab.plot3d(x, y, z, color,
                     colormap = 'Blues',
                     tube_radius=0.04)

    savepath = 'imgs/dupa.png'
    resolution = (500, 500)
    mlab.savefig(savepath, resolution)

if __name__ == '__main__':
    main()
