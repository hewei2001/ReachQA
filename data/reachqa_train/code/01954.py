import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from sklearn.linear_model import LinearRegression

# Data for the scatter plot
cities = ['New York', 'San Francisco', 'Berlin', 'Tokyo', 'Sydney']
adoption_rate = np.array([150, 200, 120, 180, 140])  # in thousands
user_satisfaction = np.array([7.8, 8.2, 7.5, 8.0, 7.7])

# Setting up the plot
plt.figure(figsize=(14, 8))
scatter = plt.scatter(adoption_rate, user_satisfaction, 
                      s=adoption_rate*10,  # Marker size corresponds to adoption rate
                      c=user_satisfaction,  # Color corresponds to satisfaction level
                      cmap='viridis', 
                      alpha=0.8, 
                      edgecolors='k', 
                      linewidth=0.8)

# Add regression line (trend line)
X = adoption_rate.reshape(-1, 1)
model = LinearRegression().fit(X, user_satisfaction)
trendline = model.predict(X)
plt.plot(adoption_rate, trendline, color='gray', linestyle='--', linewidth=1, label='Trend Line')

# Adding annotations for each city with additional information
for i, city in enumerate(cities):
    plt.annotate(f"{city}\nAdoption: {adoption_rate[i]}k\nSatisfaction: {user_satisfaction[i]}", 
                 (adoption_rate[i], user_satisfaction[i]), 
                 textcoords="offset points", 
                 xytext=(10, -10), 
                 ha='left', 
                 fontsize=9, 
                 bbox=dict(facecolor='lightblue', alpha=0.6, boxstyle='round,pad=0.3'))

# Adding color bar to represent satisfaction levels
cbar = plt.colorbar(scatter)
cbar.set_label('User Satisfaction Level', fontsize=10)

# Adding labels and title
plt.xlabel('Electric Scooter Adoption Rate (in thousands)', fontsize=12)
plt.ylabel('User Satisfaction Level (scale 1-10)', fontsize=12)
plt.title('Urban Mobility Evolution:\nAdoption Rates vs. Satisfaction Levels Across Cities', 
          fontsize=14, weight='bold', pad=20)

# Add a grid for improved readability
plt.grid(True, linestyle='--', alpha=0.5)

# Modify axes to use MaxNLocator to ensure integer tick marks
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=False))

# Add legend
plt.legend(loc='upper left', fontsize=10)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()