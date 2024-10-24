import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2000 to 2020
years = np.arange(2000, 2021, 4)

# Hypothetical popularity index data for programming languages
python_popularity = [20, 35, 50, 65, 80, 95]
java_popularity = [80, 85, 75, 70, 60, 55]
javascript_popularity = [40, 50, 65, 80, 90, 95]
csharp_popularity = [30, 45, 60, 75, 70, 65]
ruby_popularity = [25, 35, 45, 60, 65, 60]

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the line chart for each language
ax.plot(years, python_popularity, marker='o', linestyle='-', color='#3776AB', linewidth=2, label='Python')
ax.plot(years, java_popularity, marker='s', linestyle='--', color='#B07219', linewidth=2, label='Java')
ax.plot(years, javascript_popularity, marker='^', linestyle='-.', color='#F0DB4F', linewidth=2, label='JavaScript')
ax.plot(years, csharp_popularity, marker='D', linestyle=':', color='#178600', linewidth=2, label='C#')
ax.plot(years, ruby_popularity, marker='*', linestyle='-', color='#701516', linewidth=2, label='Ruby')

# Titles and labels
ax.set_title('Programming Languages Popularity Trends\n(2000-2020)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Popularity Index', fontsize=14)
ax.set_xticks(years)

# Grid lines for readability
ax.grid(True, linestyle='--', which='both', color='gray', alpha=0.5)

# Add legend
ax.legend(title='Programming Languages', loc='upper left', fontsize=12)

# Highlight key observations with annotations
ax.annotate('Python Surges', xy=(2016, 80), xytext=(2008, 85),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='#3776AB')
ax.annotate('Ruby Peaks', xy=(2012, 60), xytext=(2010, 70),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='#701516')

# Adjust layout for visibility
plt.tight_layout()

# Show the plot
plt.show()