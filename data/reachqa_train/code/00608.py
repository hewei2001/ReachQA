import matplotlib.pyplot as plt
import numpy as np

# Define the months of the year for the x-axis
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

# Percentage popularity of each programming language over the months
python_popularity = np.array([35, 36, 37, 39, 38, 39, 40, 42, 43, 44, 45, 46])
javascript_popularity = np.array([30, 29, 29, 30, 32, 31, 32, 33, 35, 36, 35, 34])
java_popularity = np.array([15, 15, 16, 16, 17, 17, 17, 16, 15, 14, 14, 13])
csharp_popularity = np.array([10, 10, 10, 9, 8, 9, 10, 10, 11, 12, 13, 14])
rust_popularity = np.array([5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 9, 10])

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(
    months, 
    python_popularity, 
    javascript_popularity, 
    java_popularity, 
    csharp_popularity, 
    rust_popularity, 
    labels=['Python', 'JavaScript', 'Java', 'C#', 'Rust'],
    colors=['#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#e41a1c'],
    alpha=0.8
)

# Adding titles and labels
ax.set_title("Rising Tides:\nProgramming Language Popularity in 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Months", fontsize=14)
ax.set_ylabel("Popularity (%)", fontsize=14)

# Improve readability with gridlines
ax.grid(True, linestyle='--', alpha=0.6)

# Position the legend and adjust layout
ax.legend(loc='upper left', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

# Display the plot
plt.show()