import matplotlib.pyplot as plt
import numpy as np

# Define industries and data
industries = ['Manufacturing', 'Healthcare', 'Retail', 'Finance', 
              'Transportation', 'Agriculture', 'Education', 'Construction']
job_displacement = np.array([1500, 500, 800, 400, 700, 300, 200, 600])  # Job displacement in thousands
job_creation = np.array([600, 700, 300, 800, 250, 400, 150, 500])        # Job creation in thousands

# New data for the bar chart: Job growth rates in percentage
job_growth_rates = np.array([5, 6, 3, 7, 4, 2, 3, 5])  # Growth rates in percentage

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# Scatter Plot
ax1 = axs[0]
scatter = ax1.scatter(job_displacement, job_creation, 
                       s=100, color='darkblue', alpha=0.7, edgecolor='black')

for i, industry in enumerate(industries):
    ax1.annotate(industry, 
                  (job_displacement[i], job_creation[i]), 
                  fontsize=10, ha='right', va='bottom', 
                  bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='lightgrey'))

ax1.set_title('AI & Robotics: Future Job Market Dynamics\nDisplacement vs Creation (2020-2030)', 
              fontsize=16, fontweight='bold')
ax1.set_xlabel('Predicted Job Displacement (in thousands)', fontsize=12)
ax1.set_ylabel('Predicted Job Creation (in thousands)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.axhline(0, color='grey', lw=1)
ax1.axvline(0, color='grey', lw=1)
ax1.set_xlim(0, 2000)
ax1.set_ylim(0, 1000)
plt.scatter([], [], color='darkblue', label='Industry Points', alpha=0.7)
ax1.legend(loc='upper left')

# Bar Chart
ax2 = axs[1]
ax2.bar(industries, job_growth_rates, color='skyblue', alpha=0.8)
ax2.set_title('Relative Impact on Job Growth Rate by Industry', fontsize=16, fontweight='bold')
ax2.set_xlabel('Industries', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.set_ylim(0, 10)
ax2.grid(axis='y', linestyle='--', alpha=0.6)

# Annotations for bars
for i, rate in enumerate(job_growth_rates):
    ax2.annotate(f'{rate}%', 
                  (i, rate), 
                  ha='center', va='bottom', 
                  fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()