import matplotlib.pyplot as plt
import numpy as np

# Define years for the x-axis
years = np.arange(2015, 2026)

# Enrollment data for Technology, Business, and Arts (in thousands)
tech_enrollments = np.array([30, 35, 40, 50, 65, 80, 100, 125, 150, 175, 200])
business_enrollments = np.array([40, 42, 45, 48, 50, 55, 60, 65, 70, 75, 80])
arts_enrollments = np.array([15, 16, 18, 19, 21, 23, 25, 28, 30, 33, 35])

# Graduation rates (as a percentage) for Technology, Business, and Arts
tech_graduation_rates = np.array([70, 72, 74, 78, 80, 82, 85, 87, 90, 92, 95])
business_graduation_rates = np.array([60, 61, 63, 65, 66, 68, 70, 72, 75, 77, 80])
arts_graduation_rates = np.array([50, 51, 53, 55, 56, 58, 60, 62, 65, 67, 70])

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Line plot for enrollments
ax1.plot(years, tech_enrollments, label="Technology", color='blue', linestyle='-', marker='o', linewidth=2)
ax1.plot(years, business_enrollments, label="Business", color='green', linestyle='--', marker='s', linewidth=2)
ax1.plot(years, arts_enrollments, label="Arts", color='red', linestyle='-.', marker='^', linewidth=2)

# Highlight 2020 as a significant year in line plot
ax1.axvline(x=2020, color='grey', linestyle=':', linewidth=1)
ax1.text(2020.5, 50, '2020: Acceleration Year', fontsize=9, color='grey')

# Set line plot title and labels
ax1.set_title("Online Course Enrollments (2015-2025)", fontsize=14, pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Enrollments (in thousands)", fontsize=12)

# Add legend and grid to line plot
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_xticks(np.arange(2015, 2026, 1))

# Annotate a significant increase point in Technology
ax1.annotate('Rapid growth', xy=(2023, 175), xytext=(2021, 160),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Bar chart for graduation rates
width = 0.25  # Width of bars

ax2.bar(years - width, tech_graduation_rates, width, label='Technology', color='blue', alpha=0.7)
ax2.bar(years, business_graduation_rates, width, label='Business', color='green', alpha=0.7)
ax2.bar(years + width, arts_graduation_rates, width, label='Arts', color='red', alpha=0.7)

# Set bar chart title and labels
ax2.set_title("Graduation Rates by Subject (2015-2025)", fontsize=14, pad=20)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Graduation Rate (%)", fontsize=12)

# Add legend and grid to bar chart
ax2.legend(loc='lower right', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.set_xticks(np.arange(2015, 2026, 1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()