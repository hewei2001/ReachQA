import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define coffee consumption (cups per day) expanded with more data points
coffee_consumption = np.arange(1, 11, 0.5)  # More data points

# Define productivity scores with non-linear trends and more workplace categories
tech_hub_productivity = 50 + 15 * np.log(coffee_consumption) + np.sin(coffee_consumption)
creative_studio_productivity = 45 + 10 * np.sqrt(coffee_consumption) + np.cos(coffee_consumption)
finance_firm_productivity = 60 + 5 * coffee_consumption - 0.5 * coffee_consumption**1.5

# Additional workplace categories with crafted productivity trends
healthcare_facility_productivity = 52 + 10 * np.log(coffee_consumption) - np.sin(coffee_consumption / 2)
research_lab_productivity = 58 + 8 * coffee_consumption**0.5 + np.sin(coffee_consumption)
educational_institution_productivity = 40 + 12 * coffee_consumption**0.3 + np.cos(coffee_consumption / 3)

# Function to create smooth curves using cubic spline interpolation
def smooth_curve(x, y):
    x_smooth = np.linspace(x.min(), x.max(), 300)
    spl = make_interp_spline(x, y, k=3)
    y_smooth = spl(x_smooth)
    return x_smooth, y_smooth

# Initialize the plot
plt.figure(figsize=(15, 9))

# Define plot settings for each workplace
workplaces = {
    'Tech Hub': ('blue', 'o', tech_hub_productivity),
    'Creative Studio': ('green', 's', creative_studio_productivity),
    'Finance Firm': ('red', '^', finance_firm_productivity),
    'Healthcare Facility': ('purple', 'd', healthcare_facility_productivity),
    'Research Lab': ('orange', 'x', research_lab_productivity),
    'Educational Institution': ('brown', '*', educational_institution_productivity),
}

# Create plots for each workplace
for workplace, (color, marker, productivity) in workplaces.items():
    x_smooth, y_smooth = smooth_curve(coffee_consumption, productivity)
    plt.scatter(coffee_consumption, productivity, label=workplace, color=color, marker=marker, s=50, alpha=0.7)
    plt.plot(x_smooth, y_smooth, color=color, linewidth=2)

# Configure titles and labels
plt.title('Trends in Coffee Consumption and Productivity Across Various Workplaces\nAnalyzed by Consumption Intensity', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Coffee Consumption (Cups per Day)', fontsize=12)
plt.ylabel('Productivity Score', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()