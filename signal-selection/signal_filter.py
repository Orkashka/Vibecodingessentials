import numpy as np
import matplotlib.pyplot as plt

def signal_filter(events):
    """ """
    pass


def plot_hist_1d(events):
    """ """
    pass


def plot_scatter_with_contour(events):
    """ """
    pass


if __name__ == '__main__':
    events = np.load('data/events.npy')
    plot_hist_1d(events)
    plot_scatter_with_contour(events)
    (mean_x, std_x), (mean_y, std_y) = signal_filter(events)
    print(f'x: mean {mean_x:.2f} std {std_x:.2f}')
    print(f'y: mean {mean_y:.2f} std {std_y:.2f}')
