import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Litville Book Fair Attendance (in thousands)
attendance = [5, 8, 12, 15, 20, 23, 28, 30, 35, 40, 45]  # in thousands

# Number of New Book Releases
new_book_releases = [10, 15, 20, 22, 30, 35, 40, 42, 50, 55, 60]

# Set up the scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(attendance, new_book_releases, c=years, cmap='plasma', s=100, alpha=0.8, edgecolor='k')

# Add title and labels with a creative layout
plt.title("Ink & Inspiration: Rise of Literary Engagement\nin Litville (2010-2020)", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("Annual Book Fair Attendance (thousands)", fontsize=12)
plt.ylabel("Number of New Book Releases", fontsize=12)

# Add colorbar
cbar = plt.colorbar(scatter, pad=0.02)
cbar.set_label('Year', fontsize=12)

# Annotate each point with the corresponding year
for i, txt in enumerate(years):
    plt.annotate(txt, (attendance[i], new_book_releases[i]), textcoords="offset points", xytext=(0, 5), ha='center')

# Improve grid visualization
plt.grid(True, linestyle='--', alpha=0.7)

# Automatic adjustment to prevent overlap
plt.tight_layout()

# Display the scatter chart
plt.show()