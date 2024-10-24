import matplotlib.pyplot as plt
import numpy as np

# Data for autonomous vehicle technology advancements over the years
years = np.arange(2010, 2021)
perception_systems = [1, 2, 2, 4, 5, 6, 8, 10, 13, 15, 18]
decision_ai = [1, 2, 3, 4, 5, 7, 9, 11, 14, 16, 20]
connectivity = [0, 0, 1, 2, 3, 4, 5, 6, 7, 9, 11]
safety_protocols = [1, 1, 2, 3, 4, 4, 5, 6, 7, 9, 10]

plt.figure(figsize=(14, 8))

# Line styles and colors
plt.plot(years, perception_systems, marker='o', label='Perception Systems', color='#1f77b4', linewidth=2, linestyle='-')
plt.plot(years, decision_ai, marker='s', label='AI Improvements', color='#ff7f0e', linewidth=2, linestyle='--')
plt.plot(years, connectivity, marker='^', label='Connectivity', color='#2ca02c', linewidth=2, linestyle='-.')
plt.plot(years, safety_protocols, marker='d', label='Safety Protocols', color='#d62728', linewidth=2, linestyle=':')

# Annotate key breakthroughs with shadow effect
plt.annotate('AI Navigation Breakthrough', xy=(2015, 7), xytext=(2012, 12),
             arrowprops=dict(facecolor='gray', arrowstyle='->', linestyle='--', linewidth=1.5), 
             fontsize=10, color='black', bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5', alpha=0.8))
plt.annotate('Connected Highway', xy=(2017, 5), xytext=(2014, 8),
             arrowprops=dict(facecolor='gray', arrowstyle='->', linestyle='--', linewidth=1.5), 
             fontsize=10, color='black', bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5', alpha=0.8))
plt.annotate('Enhanced Perception Accuracy', xy=(2018, 13), xytext=(2015, 15),
             arrowprops=dict(facecolor='gray', arrowstyle='->', linestyle='--', linewidth=1.5), 
             fontsize=10, color='black', bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5', alpha=0.8))

# Label each data point with its value
for i, year in enumerate(years):
    plt.text(year, perception_systems[i] + 0.5, f'{perception_systems[i]}', ha='center', va='bottom', fontsize=8)
    plt.text(year, decision_ai[i] + 0.5, f'{decision_ai[i]}', ha='center', va='bottom', fontsize=8)
    plt.text(year, connectivity[i] + 0.5, f'{connectivity[i]}', ha='center', va='bottom', fontsize=8)
    plt.text(year, safety_protocols[i] + 0.5, f'{safety_protocols[i]}', ha='center', va='bottom', fontsize=8)

# Enhanced titles and labels
plt.title('The Journey of Autonomous Vehicles:\nA Decade of Innovation (2010-2020)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Technological Advancements', fontsize=14)

# Enhanced legend
plt.legend(loc='upper left', fontsize=11, shadow=True, fancybox=True)

# Enable enhanced grid
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)

# Add area shading to visualize trends
plt.fill_between(years, perception_systems, color='#1f77b4', alpha=0.1)
plt.fill_between(years, decision_ai, color='#ff7f0e', alpha=0.1)
plt.fill_between(years, connectivity, color='#2ca02c', alpha=0.1)
plt.fill_between(years, safety_protocols, color='#d62728', alpha=0.1)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the optimized chart
plt.show()