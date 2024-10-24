import matplotlib.pyplot as plt
import numpy as np

# Define years for the x-axis
years = np.arange(2015, 2026)

# Enrollment data for Technology, Business, and Arts (in thousands)
tech_enrollments = np.array([30, 35, 40, 50, 65, 80, 100, 125, 150, 175, 200])
business_enrollments = np.array([40, 42, 45, 48, 50, 55, 60, 65, 70, 75, 80])
arts_enrollments = np.array([15, 16, 18, 19, 21, 23, 25, 28, 30, 33, 35])

# Create the plot
plt.figure(figsize=(12, 6))

# Plot lines for each subject area
plt.plot(years, tech_enrollments, label="Technology", color='blue', linestyle='-', marker='o', linewidth=2)
plt.plot(years, business_enrollments, label="Business", color='green', linestyle='--', marker='s', linewidth=2)
plt.plot(years, arts_enrollments, label="Arts", color='red', linestyle='-.', marker='^', linewidth=2)

# Highlight 2020 as a significant year
plt.axvline(x=2020, color='grey', linestyle=':', linewidth=1)
plt.text(2020.5, 50, '2020: Acceleration Year', fontsize=9, color='grey')

# Set chart title and labels
plt.title("The Rise of Digital Learning:\nOnline Course Enrollments (2015-2025)", fontsize=16, pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Enrollments (in thousands)", fontsize=12)

# Add legend and grid
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)

# Configure x-axis tick marks
plt.xticks(np.arange(2015, 2026, 1))

# Annotate a significant increase point in Technology
plt.annotate('Rapid growth', xy=(2023, 175), xytext=(2021, 160),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()