import matplotlib.pyplot as plt
import numpy as np

# Define years from 2015 to 2025
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])

# Popularity percentages for each programming language
popularity_python = [22, 24, 27, 30, 35, 40, 45, 50, 52, 53, 55]
popularity_java = [30, 29, 28, 28, 27, 26, 25, 24, 23, 22, 21]
popularity_javascript = [20, 22, 23, 24, 25, 27, 28, 29, 30, 32, 33]
popularity_cpp = [15, 14, 14, 13, 13, 12, 12, 12, 11, 11, 10]
popularity_ruby = [10, 9, 8, 7, 7, 6, 6, 5, 5, 4, 4]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each programming language with unique markers and colors
ax.plot(years, popularity_python, marker='o', linestyle='-', color='#3778bf', linewidth=2, label='Python')
ax.plot(years, popularity_java, marker='s', linestyle='--', color='#f0833a', linewidth=2, label='Java')
ax.plot(years, popularity_javascript, marker='^', linestyle='-.', color='#77b55a', linewidth=2, label='JavaScript')
ax.plot(years, popularity_cpp, marker='d', linestyle=':', color='#b09ecc', linewidth=2, label='C++')
ax.plot(years, popularity_ruby, marker='*', linestyle='-', color='#e63946', linewidth=2, label='Ruby')

# Annotate data points with their popularity percentages
for (year, pop) in zip(years, popularity_python):
    ax.annotate(f'{pop}%', xy=(year, pop), textcoords='offset points', xytext=(0, 5), ha='center')
for (year, pop) in zip(years, popularity_java):
    ax.annotate(f'{pop}%', xy=(year, pop), textcoords='offset points', xytext=(0, -15), ha='center')
for (year, pop) in zip(years, popularity_javascript):
    ax.annotate(f'{pop}%', xy=(year, pop), textcoords='offset points', xytext=(-20, -10), ha='center')
for (year, pop) in zip(years, popularity_cpp):
    ax.annotate(f'{pop}%', xy=(year, pop), textcoords='offset points', xytext=(10, 10), ha='center')
for (year, pop) in zip(years, popularity_ruby):
    ax.annotate(f'{pop}%', xy=(year, pop), textcoords='offset points', xytext=(0, 10), ha='center')

# Setting up the chart title and axis labels
ax.set_title('Trends in Programming Language Popularity\nAmong Software Developers (2015-2025)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Popularity (%)', fontsize=12)

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Set x-axis tick marks
ax.set_xticks(years)

# Display legend to identify each line
ax.legend(title='Programming Languages', loc='upper left', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()