import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = np.arange(2010, 2020)

# Hypothetical data for the popularity of languages (on a scale from 0 to 100)
python_popularity = np.array([50, 55, 60, 65, 70, 78, 85, 90, 93, 97])
javascript_popularity = np.array([60, 63, 67, 70, 72, 75, 78, 80, 82, 85])
java_popularity = np.array([80, 78, 75, 72, 70, 68, 67, 66, 65, 64])

# Create the line plot
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(years, python_popularity, label='Python', color='tab:blue', marker='o', linewidth=2.5, linestyle='-')
ax.plot(years, javascript_popularity, label='JavaScript', color='tab:green', marker='^', linewidth=2.5, linestyle='--')
ax.plot(years, java_popularity, label='Java', color='tab:red', marker='s', linewidth=2.5, linestyle='-.')

# Set labels and title
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Popularity Index', fontsize=12)
ax.set_title('The Evolution of Programming Language Popularity\nin the Digital Age (2010-2019)', fontsize=14)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add a legend
ax.legend(loc='lower left', fontsize=10)

# Automatically adjust the subplot layout for better fit
plt.tight_layout()

# Show the plot
plt.show()