from signal_filter import signal_filter

import numpy as np

def test_signal_filter():
    events = np.load('data/events.npy')
    (mean_x, std_x), (mean_y, std_y) = signal_filter(events)
    assert np.abs(mean_x - 0.00) < 0.01
    assert np.abs(mean_y - 0.10) < 0.01
    assert np.abs(std_x - 0.70) < 0.02
    assert np.abs(std_y - 0.70) < 0.02
