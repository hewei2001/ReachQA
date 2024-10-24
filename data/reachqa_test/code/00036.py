import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

# Original data for innovation scores and engagement rates
innovation_scores = np.array([10, 25, 40, 55, 70, 85])
engagement_rates = np.array([20, 30, 55, 65, 80, 95])

# New data for additional subplot: Monthly Active Users (MAU) and Subscription Costs
service_names = ["SoundWave", "BeatFlow", "TuneStream", "Harmony", "ChordMax", "RhythmHub"]
mau = np.array([1.5, 2.3, 3.0, 3.8, 4.5, 5.2])  # in millions
subscription_costs = np.array([9.99, 12.99, 14.99, 9.99, 19.99, 14.99])  # in dollars

# Creating a smooth line using cubic spline interpolation for the original data
tck = interpolate.splrep(innovation_scores, engagement_rates, s=0)
innovation_fine = np.linspace(min(innovation_scores), max(innovation_scores), 300)
engagement_fine = interpolate.splev(innovation_fine, tck, der=0)

# Set up the figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 6), gridspec_kw={'width_ratios': [1.5, 1]})

# First subplot: Engagement vs Innovation (Scatter + Spline)
axes[0].scatter(innovation_scores, engagement_rates, color='purple', label='Streaming Services',
                s=100, alpha=0.8, edgecolors='black')
axes[0].plot(innovation_fine, engagement_fine, color='darkred', linestyle='-', linewidth=2.5,
             label='Trend Line (Cubic Spline)')
axes[0].set_title("The Evolution of Music Streaming:\nEngagement vs. Innovation", fontsize=14, fontweight='bold')
axes[0].set_xlabel("Innovation Score", fontsize=12)
axes[0].set_ylabel("Engagement Rate", fontsize=12)
axes[0].legend(frameon=False, fontsize=10)
axes[0].grid(True, linestyle='--', alpha=0.7)
for i, txt in enumerate(service_names):
    axes[0].annotate(txt, (innovation_scores[i], engagement_rates[i]), textcoords="offset points", 
                     xytext=(0,10), ha='center')

# Second subplot: MAU vs Subscription Cost (Bar Plot)
bar_colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#CCCCFF', '#FFB366']
axes[1].bar(service_names, mau, color=bar_colors, alpha=0.7, label='MAU (millions)')
axes[1].set_ylabel("Monthly Active Users (millions)", fontsize=12)
axes[1].twinx().plot(service_names, subscription_costs, color='orange', marker='o', 
                     label='Subscription Costs ($)')
axes[1].set_title("Service Costs and Reach", fontsize=14, fontweight='bold')
axes[1].set_ylim(0, 7)
axes[1].legend(loc='upper left', fontsize=10)
axes[1].grid(False)

# Adjust layout to prevent overlap
fig.tight_layout()

# Show plot
plt.show()