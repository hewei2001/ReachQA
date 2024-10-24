import matplotlib.pyplot as plt
import numpy as np

# Define years for the x-axis
years = np.arange(2015, 2026)

# Original data for digital transformation adoption rates in various industries
healthcare_adoption = [10, 12, 15, 18, 25, 35, 50, 65, 75, 80, 85]
manufacturing_adoption = [20, 25, 30, 40, 50, 55, 60, 70, 75, 80, 82]
finance_adoption = [30, 40, 50, 60, 70, 75, 80, 85, 90, 92, 95]
retail_adoption = [15, 18, 22, 28, 35, 42, 50, 60, 70, 78, 80]
education_adoption = [5, 8, 10, 15, 25, 40, 55, 65, 70, 75, 80]

# New data: Average annual growth rate of adoption for each industry
industries = ['Healthcare', 'Manufacturing', 'Finance', 'Retail', 'Education']
growth_rates = [
    ((healthcare_adoption[-1] / healthcare_adoption[0]) ** (1 / (len(years) - 1)) - 1) * 100,
    ((manufacturing_adoption[-1] / manufacturing_adoption[0]) ** (1 / (len(years) - 1)) - 1) * 100,
    ((finance_adoption[-1] / finance_adoption[0]) ** (1 / (len(years) - 1)) - 1) * 100,
    ((retail_adoption[-1] / retail_adoption[0]) ** (1 / (len(years) - 1)) - 1) * 100,
    ((education_adoption[-1] / education_adoption[0]) ** (1 / (len(years) - 1)) - 1) * 100
]

# Create a subplot layout with 1 row and 2 columns
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Line Chart: Digital Transformation Adoption Rates
axes[0].plot(years, healthcare_adoption, marker='o', linestyle='-', linewidth=2, label='Healthcare', color='#FF5733', alpha=0.8)
axes[0].plot(years, manufacturing_adoption, marker='v', linestyle='--', linewidth=2, label='Manufacturing', color='#33FF57', alpha=0.8)
axes[0].plot(years, finance_adoption, marker='s', linestyle='-.', linewidth=2, label='Finance', color='#3357FF', alpha=0.8)
axes[0].plot(years, retail_adoption, marker='^', linestyle=':', linewidth=2, label='Retail', color='#FF33FF', alpha=0.8)
axes[0].plot(years, education_adoption, marker='D', linestyle='-', linewidth=2, label='Education', color='#FFFF33', alpha=0.8)

# Customize the first plot
axes[0].set_title("Digital Transformation Journey:\nIndustry Adoption Over Time", fontsize=16, fontweight='bold')
axes[0].set_xlabel("Year", fontsize=12)
axes[0].set_ylabel("Adoption Rate (%)", fontsize=12)
axes[0].set_xticks(years)
axes[0].set_xticklabels(years, rotation=45)
axes[0].set_yticks(np.arange(0, 101, 10))
axes[0].grid(True, alpha=0.3, linestyle='--', linewidth=0.7)
axes[0].legend(title="Industries", loc='upper left', fontsize=10)

# Bar Chart: Average Annual Growth Rate
bars = axes[1].bar(industries, growth_rates, color=['#FF5733', '#33FF57', '#3357FF', '#FF33FF', '#FFFF33'], alpha=0.7)
axes[1].set_title("Average Annual Growth Rate by Industry\n(2015-2025)", fontsize=16, fontweight='bold')
axes[1].set_xlabel("Industry", fontsize=12)
axes[1].set_ylabel("Growth Rate (%)", fontsize=12)
axes[1].set_ylim(0, max(growth_rates) + 10)
axes[1].grid(True, axis='y', alpha=0.3, linestyle='--', linewidth=0.7)

# Annotate bars with their height value
for bar in bars:
    height = bar.get_height()
    axes[1].annotate(f'{height:.2f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()