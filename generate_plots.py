"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.
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

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Draw a sensor temperature scatter plot on an existing Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Array of 200 temperature readings for Sensor A in degrees Celsius.
    sensor_b : numpy.ndarray
        Array of 200 temperature readings for Sensor B in degrees Celsius.
    timestamps : numpy.ndarray
        Array of 200 timestamps uniformly spaced from 0 to 10 seconds.
    ax : matplotlib.axes.Axes
        Matplotlib Axes object to draw the scatter plot on.

    Returns
    -------
    None
        The function modifies the provided Axes in place.
    """
    ax.scatter(timestamps, sensor_a, color="tab:blue", alpha=0.7, label="Sensor A")
    ax.scatter(timestamps, sensor_b, color="tab:orange", alpha=0.7, label="Sensor B")
    ax.set_title("Simulated Temperature Readings vs Time")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.4)

