"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np


def generate_data(seed):
    """Generate synthetic temperature sensor data.

    Parameters
    ----------
    seed : int
        Seed value for NumPy's random number generator.

    Returns
    -------
    sensor_a : numpy.ndarray
        Array of 200 simulated temperature readings for Sensor A with mean
        25 °C and standard deviation 3 °C.
    sensor_b : numpy.ndarray
        Array of 200 simulated temperature readings for Sensor B with mean
        27 °C and standard deviation 4.5 °C.
    timestamps : numpy.ndarray
        Array of 200 timestamps uniformly spaced from 0 to 10 seconds.
    """
    rng = np.random.default_rng(seed)
    timestamps = np.linspace(0.0, 10.0, 200)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200)
    return sensor_a, sensor_b, timestamps

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

