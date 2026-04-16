# Sensor Plot Generator

A small Python script that generates synthetic temperature sensor data and creates scatter, histogram, and box plot visualizations.

## Installation

1. Activate the `ece105` conda environment:

```bash
conda activate ece105
```

2. Install the required packages using `conda` or `mamba`:

```bash
conda install numpy matplotlib
```

or

```bash
mamba install numpy matplotlib
```

## Usage

Run the script from the project directory:

```bash
python generate_plots.py
```

## Example output

The script produces a combined figure saved as `sensor_analysis.png` that contains:

- a scatter plot of Sensor A and Sensor B temperature readings over time
- an overlaid histogram comparing the temperature distributions for both sensors
- a side-by-side box plot showing the distribution and overall mean of both sensors

## AI tools used and disclosure

I used Copilot to generate code based on prompts that I then checked and ran to make sure it creates
an acceptable `sensor_analysis.png` with the three required graphs in both the python code and
Jupyter notebook.