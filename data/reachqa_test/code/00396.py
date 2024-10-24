import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data for Arabica and Robusta coffee beans' quality journey
stages = ['Germination', 'Maturation', 'Harvest', 'Sorting', 'Roasting']
arabica_quality = [45, 70, 85, 88, 92]  # Quality points for Arabica coffee
robusta_quality = [30, 55, 65, 68, 70]  # Quality points for Robusta coffee

# Simulated coffee production data at each stage (in tons)
arabica_production = [50, 70, 85, 120, 150]  # Production for Arabica
robusta_production = [30, 45, 60, 80, 95]   # Production for Robusta

# Create x-axis values, these will be the stages of the journey
x = np.arange(len(stages))

# Create spline interpolation for smooth fitting
xnew = np.linspace(x.min(), x.max(), 50)
spl_arabica = make_interp_spline(x, arabica_quality, k=3)
ynew_arabica = spl_arabica(xnew)

spl_robusta = make_interp_spline(x, robusta_quality, k=3)
ynew_robusta = spl_robusta(xnew)

# Create figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 6))

# Subplot 1 - Quality journey plot
# Scatter Arabica points and fit
ax1.scatter(x, arabica_quality, color='brown', label='Arabica', marker='o', s=100)
ax1.plot(xnew, ynew_arabica, color='brown', linestyle='-', linewidth=2, label='Arabica Fit')

# Scatter Robusta points and fit
ax1.scatter(x, robusta_quality, color='forestgreen', label='Robusta', marker='^', s=100)
ax1.plot(xnew, ynew_robusta, color='forestgreen', linestyle='-', linewidth=2, label='Robusta Fit')

# Title and labels
ax1.set_title('A Bean\'s Journey:\nQuality Through Coffee Cultivation and Processing', fontsize=18)
ax1.set_xlabel('Cultivation and Processing Stages', fontsize=14)
ax1.set_ylabel('Quality (0-100 scale)', fontsize=14)
ax1.set_xticks(x, stages, rotation=45)

# Grid for readability
ax1.grid(True, linestyle='--', alpha=0.7)

# Legend for differentiation
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Subplot 2 - Production contribution plot
# Bar width
width = 0.35

# Add bars for Arabica production
ax2.bar(x - width/2, arabica_production, width, label='Arabica', color='brown')

# Add bars for Robusta production
ax2.bar(x + width/2, robusta_production, width, label='Robusta', color='forestgreen')

# Title and labels
ax2.set_title('Coffee Production Contribution\nby Cultivation and Processing Stage', fontsize=18)
ax2.set_xlabel('Cultivation and Processing Stages', fontsize=14)
ax2.set_ylabel('Coffee Production (tons)', fontsize=14)
ax2.set_xticks(x, stages, rotation=45)

# Grid for readability
ax2.grid(True, linestyle='--', alpha=0.7)

# Legend for differentiation
ax2.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Adjusting layout
plt.tight_layout()

# Show the plot
plt.show()