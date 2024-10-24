import matplotlib.pyplot as plt
import numpy as np

# Define the years and corresponding FLOPS (in teraflops) and model parameters (in billions)
years = np.arange(1980, 2021, 5)
computational_power = [0.001, 0.01, 0.1, 1, 10, 100, 1000, 5000, 10000]
model_complexity = [0.001, 0.01, 0.05, 0.2, 1, 10, 50, 200, 400]

# Annotations for significant milestones
milestones = {
    1985: "First\nNeural Networks",
    1995: "Rise of\nSVMs",
    2005: "Deep\nLearning Boom",
    2012: "AlexNet\nBreakthrough",
    2020: "Large-scale\nLanguage Models"
}

# Create the line chart
plt.figure(figsize=(14, 8))
plt.plot(years, computational_power, label='Computational Power (TeraFLOPS)', color='navy', marker='o', linestyle='-', linewidth=2)
plt.plot(years, model_complexity, label='Model Complexity (Billions of Parameters)', color='orangered', marker='o', linestyle='-', linewidth=2)

# Adding annotations for significant milestones
for year, event in milestones.items():
    comp_power = computational_power[(year - 1980) // 5]
    plt.annotate(event,
                 xy=(year, comp_power),
                 xytext=(year, comp_power * 3),
                 arrowprops=dict(facecolor='black', arrowstyle='->', lw=0.8),
                 fontsize=9,
                 ha='center',
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightblue'))

# Customize the plot
plt.title("Evolution of Computational Power and Machine Learning\nModel Complexity from 1980 to 2020", fontsize=16, fontweight='bold', ha='center')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Scale (Logarithmic)", fontsize=12)
plt.yscale('log')  # Use a logarithmic scale for clarity
plt.xticks(years, rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)

# Adding a legend
plt.legend(loc='upper left', fontsize=10, frameon=False)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()