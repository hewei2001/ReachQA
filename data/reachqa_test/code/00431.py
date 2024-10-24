import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Extended years from 2010 to 2030
years = np.arange(2010, 2031)

# Constructing hypothetical green space growth data
green_space_growth = np.array([4.5, 5.0, 5.5, 5.7, 6.2, 6.5, 7.1, 7.8, 8.6, 9.5, 10.0, 10.5, 11.2, 12.0, 13.0, 13.5, 14.0, 15.0, 15.5, 16.0, 16.5])

# Additional metric: Biodiversity index
biodiversity_index = np.array([1.0, 1.1, 1.3, 1.2, 1.4, 1.6, 1.8, 2.0, 2.1, 2.4, 2.6, 2.7, 2.9, 3.1, 3.3, 3.5, 3.7, 3.9, 4.1, 4.3, 4.5])

# Predictive model to extend data beyond 2023
years_train = years[:len(green_space_growth)].reshape(-1, 1)
model = LinearRegression()
model.fit(years_train, green_space_growth)
predicted_growth = model.predict(years.reshape(-1, 1))

# Initiatives
initiatives = {
    2016: "Garden Renaissance Project",
    2020: "Urban Greening Initiative",
    2023: "Eco-Park Expansion",
    2027: "New Green Ordinance",
}

# Initialize figure with subplots
fig, axs = plt.subplots(2, 1, figsize=(14, 12), constrained_layout=True)

# Main plot - Green Space Growth
bar_width = 0.35
opacity = 0.7

axs[0].bar(years - bar_width/2, green_space_growth, bar_width, alpha=opacity, color='forestgreen', label='Actual Growth')
axs[0].bar(years + bar_width/2, predicted_growth, bar_width, alpha=opacity, color='darkorange', label='Predicted Growth')

# Annotate special initiatives
for year, event in initiatives.items():
    index = np.where(years == year)[0][0]
    axs[0].annotate(event, (years[index], green_space_growth[index] + 0.5), 
                    textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, 
                    arrowprops=dict(facecolor='black', arrowstyle="->"))

# Titles and labels for main plot
axs[0].set_title('Urban Green Space Growth and Biodiversity:\nA Comprehensive Analysis (2010-2030)', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=14)
axs[0].set_ylabel('Green Space Growth (sq km)', fontsize=14)
axs[0].legend(loc='upper left')
axs[0].set_ylim(0, 18)  # Adjusted y-axis limit
axs[0].grid(True, linestyle='--', alpha=0.6)

# Additional Biodiversity Index subplot
axs[1].plot(years, biodiversity_index, marker='s', linestyle='-', color='mediumblue', linewidth=2, label='Biodiversity Index')
axs[1].set_xlabel('Year', fontsize=14)
axs[1].set_ylabel('Biodiversity Index', fontsize=14)
axs[1].set_title('Biodiversity Index Trend in Urban Areas', fontsize=14, fontweight='bold')
axs[1].legend(loc='upper left')
axs[1].set_ylim(0, 5)  # Adjusted y-axis limit
axs[1].grid(True, linestyle='--', alpha=0.6)

# Adjust layout and show the plot
plt.xticks(years, rotation=45)
plt.show()