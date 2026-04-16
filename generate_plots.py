"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt

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

# Create plot_histogram(sensor_a, sensor_b, timestamps, ax) and 
# plot_boxplot(sensor_a, sensor_b, timestamps, ax) that draws
# the histogram and box plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_histogram(sensor_a, sensor_b, timestamps, ax):
    """Draw overlaid temperature histograms for two sensors on an Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Array of 200 temperature readings for Sensor A in degrees Celsius.
    sensor_b : numpy.ndarray
        Array of 200 temperature readings for Sensor B in degrees Celsius.
    timestamps : numpy.ndarray
        Array of 200 timestamps uniformly spaced from 0 to 10 seconds.
        This parameter is accepted for API consistency but is not used.
    ax : matplotlib.axes.Axes
        Matplotlib Axes object to draw the histogram on.

    Returns
    -------
    None
        The function modifies the provided Axes in place.
    """
    mean_a = np.mean(sensor_a)
    mean_b = np.mean(sensor_b)

    ax.hist(sensor_a, bins=30, alpha=0.5, color="tab:blue", label="Sensor A")
    ax.hist(sensor_b, bins=30, alpha=0.5, color="tab:orange", label="Sensor B")
    ax.axvline(mean_a, color="tab:blue", linestyle="--", linewidth=2,
               label=f"Sensor A mean ({mean_a:.2f}°C)")
    ax.axvline(mean_b, color="tab:orange", linestyle="--", linewidth=2,
               label=f"Sensor B mean ({mean_b:.2f}°C)")
    ax.set_title("Temperature Distribution for Sensor A and Sensor B")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Count")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.3)


def plot_boxplot(sensor_a, sensor_b, timestamps, ax):
    """Draw a side-by-side box plot comparing two sensor temperature arrays.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Array of 200 temperature readings for Sensor A in degrees Celsius.
    sensor_b : numpy.ndarray
        Array of 200 temperature readings for Sensor B in degrees Celsius.
    timestamps : numpy.ndarray
        Array of 200 timestamps uniformly spaced from 0 to 10 seconds.
        This parameter is accepted for API consistency but is not used.
    ax : matplotlib.axes.Axes
        Matplotlib Axes object to draw the box plot on.

    Returns
    -------
    None
        The function modifies the provided Axes in place.
    """
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.boxplot(
        [sensor_a, sensor_b],
        tick_labels=["Sensor A", "Sensor B"],
        patch_artist=True,
        boxprops=dict(facecolor="lightgrey", color="black"),
        medianprops=dict(color="black"),
        whiskerprops=dict(color="black"),
        capprops=dict(color="black"),
        flierprops=dict(marker="o", markerfacecolor="red", markersize=5, alpha=0.6),
    )
    ax.axhline(overall_mean, color="tab:green", linestyle="--", linewidth=2,
               label=f"Overall mean ({overall_mean:.2f}°C)")
    ax.set_title("Sensor Temperature Box Plot")
    ax.set_xlabel("Sensor")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.3)

# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.

def main():
    """Generate plots for synthetic sensor data and save the figure.

    Returns
    -------
    None
        This function saves the generated figure to disk as
        ``sensor_analysis.png``.
    """
    sensor_a, sensor_b, timestamps = generate_data(seed=6411)

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(18, 12))
    axes = axes.flatten()

    plot_scatter(sensor_a, sensor_b, timestamps, axes[0])
    plot_histogram(sensor_a, sensor_b, timestamps, axes[1])
    plot_boxplot(sensor_a, sensor_b, timestamps, axes[2])

    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    stats_text = (
        f"Sensor A mean: {sensor_a.mean():.2f} °C\n"
        f"Sensor B mean: {sensor_b.mean():.2f} °C\n"
        f"Overall mean: {overall_mean:.2f} °C\n"
        f"Sensor A std: {sensor_a.std(ddof=1):.2f} °C\n"
        f"Sensor B std: {sensor_b.std(ddof=1):.2f} °C"
    )
    axes[3].text(
        0.02,
        0.98,
        stats_text,
        va="top",
        ha="left",
        fontsize=12,
        family="monospace",
    )
    axes[3].set_title("Summary Statistics")
    axes[3].set_axis_off()

    plt.tight_layout()
    fig.savefig("sensor_analysis.png", dpi=150, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
