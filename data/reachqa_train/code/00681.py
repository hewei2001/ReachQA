import matplotlib.pyplot as plt
import numpy as np

# Define the years and communication modes
years = np.arange(1990, 2021)
modes = ['Postal Mail', 'Landline Phones', 'Emails', 'Mobile Phones', 'Social Media & IM']

# Create data representing the percentage use of each communication mode
postal_mail = np.array([30, 28, 25, 22, 18, 15, 12, 10, 9, 8, 7, 6, 5, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1])
landline_phones = np.array([45, 44, 43, 42, 41, 39, 35, 32, 30, 28, 26, 25, 23, 22, 20, 18, 16, 14, 12, 10, 8, 6, 5, 4, 4, 4, 3, 3, 2, 1, 1])
emails = np.array([5, 7, 10, 15, 20, 23, 25, 27, 29, 30, 30, 30, 29, 28, 27, 26, 25, 25, 24, 23, 22, 20, 19, 18, 17, 16, 15, 14, 13, 12, 10])
mobile_phones = np.array([2, 3, 5, 8, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 58, 60, 62, 63, 64, 65, 66, 67, 67, 68, 68, 69, 70, 71, 71, 72, 73])
social_media = 100 - (postal_mail + landline_phones + emails + mobile_phones)

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, postal_mail, landline_phones, emails, mobile_phones, social_media,
             labels=modes, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'], alpha=0.8)

# Add titles and labels
ax.set_title("Evolution of Communication Modes\nAcross the Digital Era (1990-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Percentage of Use (%)", fontsize=12)

# Customize the legend and grid
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Communication Modes', title_fontsize='13', fontsize=11)
ax.grid(linestyle='--', alpha=0.5)

# Set x-axis ticks to avoid label overlap
plt.xticks(years[::3], rotation=45)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()