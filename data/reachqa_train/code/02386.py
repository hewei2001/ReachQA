import matplotlib.pyplot as plt
import numpy as np

# Years from 2013 to 2023
years = np.arange(2013, 2024)

# Artificial data for ice shelf melting rates (in cubic kilometers per year)
ross_melting = np.array([100, 105, 110, 112, 115, 118, 120, 125, 130, 135, 140])
filchner_ronne_melting = np.array([80, 82, 85, 88, 90, 92, 95, 98, 100, 105, 110])
larsen_melting = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

# Create the line chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting melting rates for each ice shelf
ax.plot(years, ross_melting, label='Ross Ice Shelf', marker='o', linestyle='-', color='deepskyblue', linewidth=2)
ax.plot(years, filchner_ronne_melting, label='Filchner-Ronne Ice Shelf', marker='^', linestyle='-', color='mediumseagreen', linewidth=2)
ax.plot(years, larsen_melting, label='Larsen Ice Shelf', marker='s', linestyle='-', color='coral', linewidth=2)

# Setting title and labels
ax.set_title("Decade of Change:\nAntarctic Ice Shelf Melting Rates (2013-2023)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Melting Rate (Cubic Kilometers per Year)", fontsize=12)

# Adding a legend to distinguish each ice shelf
ax.legend(loc='upper left', fontsize=10, title="Ice Shelf", frameon=True)

# Adding grid lines for better readability
ax.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)

# Highlighting a significant increase in melting rate around 2020 for Larsen Ice Shelf
ax.annotate('Significant Increase', xy=(2020, 90), xytext=(2017, 95),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=10, fontweight='bold', color='darkred')

# Highlighting the year 2023 as the end of the observed period with a vertical line
ax.axvline(x=2023, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
ax.text(2023.1, 60, '2023 End of Decade', rotation=90, verticalalignment='center', fontsize=10, color='gray')

# Adjust layout to fit elements and avoid overlap
plt.tight_layout()

# Display the plot
plt.show()