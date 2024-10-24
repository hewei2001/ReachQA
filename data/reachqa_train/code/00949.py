import matplotlib.pyplot as plt
import numpy as np

# Years from 1900 to 2000
years = np.arange(1900, 2010, 10)

# Influence units for communication technologies
telegrams = np.array([40, 35, 30, 20, 10, 5, 2, 1, 0, 0, 0])
telephones = np.array([5, 10, 20, 35, 50, 60, 70, 80, 85, 90, 95])
radio = np.array([0, 0, 5, 15, 25, 40, 50, 40, 30, 20, 10])
television = np.array([0, 0, 0, 0, 5, 15, 30, 45, 60, 70, 80])
internet = np.array([0, 0, 0, 0, 0, 0, 5, 15, 25, 40, 60])

# Stack data
data = np.array([telegrams, telephones, radio, television, internet])

# Plotting the stacked area chart
plt.figure(figsize=(14, 8))
plt.stackplot(years, data, labels=['Telegrams', 'Telephones', 'Radio', 'Television', 'Internet'], 
              colors=['#ff9999', '#66b2ff', '#99ff99', '#ffcc99', '#c2c2f0'], alpha=0.85)

# Titles and labels
plt.title('Evolution of Communication Modalities\nfrom 1900 to 2000', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Influence Units', fontsize=12)
plt.xlim(years[0], years[-1])
plt.ylim(0, 220)

# Customizing the grid
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend
plt.legend(loc='upper left', fontsize=10, title="Communication Technologies")

# Rotating x-axis labels for better readability
plt.xticks(years, rotation=45)

# Adding annotations to highlight significant shifts in communication trends
plt.annotate('Rise of Telephones', xy=(1950, 60), xytext=(1920, 130),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontweight='bold')
plt.annotate('Internet Era Begins', xy=(2000, 60), xytext=(1980, 100),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontweight='bold')

# Automatically adjust layout for better visualization
plt.tight_layout()

# Show the plot
plt.show()