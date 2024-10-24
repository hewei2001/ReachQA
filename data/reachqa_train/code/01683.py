import matplotlib.pyplot as plt
import numpy as np

# Define years from 2010 to 2030
years = np.arange(2010, 2031)

# Popularity percentages for each programming language, using non-linear data patterns
popularity_python = np.clip(15 + 5 * np.log(years - 2009), 0, 60)
popularity_java = np.clip(35 - 2 * np.sqrt(years - 2009), 0, 35)
popularity_javascript = np.clip(10 + 3 * np.sqrt(years - 2005), 0, 45)
popularity_cpp = np.clip(20 - 0.5 * (years - 2010), 0, 20)
popularity_ruby = np.clip(15 - 0.75 * (years - 2010), 0, 15)
popularity_swift = np.clip(2.5 * (np.tanh(years - 2013) + 1), 0, 15)
popularity_go = np.clip(0.2 * (years - 2010) ** 1.5, 0, 30)
popularity_kotlin = np.clip(2 * np.log(years - 2014) + 1, 0, 15)

# Create the plot
fig, axs = plt.subplots(2, 1, figsize=(14, 12))
ax1, ax2 = axs

# Plot each programming language with unique markers and colors
ax1.plot(years, popularity_python, marker='o', linestyle='-', color='#3778bf', linewidth=2, label='Python')
ax1.plot(years, popularity_java, marker='s', linestyle='--', color='#f0833a', linewidth=2, label='Java')
ax1.plot(years, popularity_javascript, marker='^', linestyle='-.', color='#77b55a', linewidth=2, label='JavaScript')
ax1.plot(years, popularity_cpp, marker='d', linestyle=':', color='#b09ecc', linewidth=2, label='C++')
ax1.plot(years, popularity_ruby, marker='*', linestyle='-', color='#e63946', linewidth=2, label='Ruby')
ax1.plot(years, popularity_swift, marker='x', linestyle='-', color='#16a085', linewidth=2, label='Swift')
ax1.plot(years, popularity_go, marker='p', linestyle='--', color='#f39c12', linewidth=2, label='Go')
ax1.plot(years, popularity_kotlin, marker='h', linestyle=':', color='#9b59b6', linewidth=2, label='Kotlin')

# Title and labels for the first plot
ax1.set_title('Trends in Programming Language Popularity\nAmong Software Developers (2010-2030)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Popularity (%)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_xticks(years[::2])  # Show ticks every 2 years
ax1.legend(title='Languages', loc='upper left', fontsize=10)

# Secondary plot: sum of popularity
popularity_sum = popularity_python + popularity_java + popularity_javascript + popularity_cpp + popularity_ruby + popularity_swift + popularity_go + popularity_kotlin
ax2.plot(years, popularity_sum, marker='o', linestyle='-', color='#2c3e50', linewidth=2, label='Total Popularity')

# Title and labels for the second plot
ax2.set_title('Total Popularity of Programming Languages Over Time', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Total Popularity (%)', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.set_xticks(years[::2])
ax2.legend(loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()