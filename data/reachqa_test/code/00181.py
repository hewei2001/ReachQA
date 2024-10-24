import matplotlib.pyplot as plt
import numpy as np

# Define the years and model categories
years = np.arange(2013, 2024)
categories = ["Linear Models", "Decision Trees", "Neural Networks", "Ensemble Methods"]

# Create artificial data for each category
linear_models = [120, 115, 110, 100, 90, 80, 70, 60, 55, 50, 45]
decision_trees = [80, 85, 80, 75, 70, 70, 65, 60, 60, 55, 50]
neural_networks = [60, 75, 95, 110, 130, 150, 160, 170, 180, 190, 200]
ensemble_methods = [40, 45, 50, 60, 70, 80, 85, 90, 95, 100, 105]

# Create additional data for average citations
average_citations = [5.5, 6, 5.8, 6.5, 6.8, 7.0, 7.3, 7.6, 8.0, 8.5, 9.0]

# Prepare the data for stacking
data = np.array([linear_models, decision_trees, neural_networks, ensemble_methods])

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot stacked bars
ax.bar(years, linear_models, label="Linear Models", color='skyblue', alpha=0.8)
ax.bar(years, decision_trees, bottom=linear_models, label="Decision Trees", color='goldenrod', alpha=0.8)
ax.bar(years, neural_networks, bottom=np.array(linear_models) + np.array(decision_trees), label="Neural Networks", color='salmon', alpha=0.8)
ax.bar(years, ensemble_methods, bottom=np.array(linear_models) + np.array(decision_trees) + np.array(neural_networks), label="Ensemble Methods", color='lightgreen', alpha=0.8)

# Overlay line plot on secondary y-axis for average citations
ax2 = ax.twinx()
ax2.plot(years, average_citations, label="Average Citations per Paper", color='purple', linewidth=2, marker='o', linestyle='--')
ax2.set_ylabel("Average Citations per Paper", fontsize=12, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

# Set titles and labels
ax.set_title("Evolution of Machine Learning Model Architectures\nin Research Papers (2013-2023)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Research Papers", fontsize=12)

# Customize x-ticks
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=11, rotation=45)

# Add legends
ax.legend(title="Model Architectures", fontsize=10, title_fontsize=11, loc='upper left', bbox_to_anchor=(1.05, 1))
ax2.legend(loc='upper right')

# Enhance grid and style
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust layout to prevent overlapping and ensure clarity
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the chart
plt.show()