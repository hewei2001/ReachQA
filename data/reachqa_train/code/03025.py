import matplotlib.pyplot as plt
import numpy as np

# Define the years and the corresponding number of eco-friendly brands
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
brands = np.array([50, 65, 80, 95, 120, 140, 180, 220, 280, 350, 420])

# Initialize the plot
plt.figure(figsize=(12, 8))
plt.plot(years, brands, marker='o', color='seagreen', linewidth=2, linestyle='-')

# Annotate specific years with notable growth
annotations = {
    2012: "Material Innovations",
    2015: "Climate Agreement",
    2018: "Ethical Consumerism",
    2020: "Sustainability Focus"
}

# Add annotations to the plot
for year, text in annotations.items():
    plt.annotate(text,
                 xy=(year, brands[years.tolist().index(year)]), 
                 xytext=(year, brands[years.tolist().index(year)] + 40),
                 arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=8),
                 fontsize=10, color='darkgreen')

# Label each data point
for (x, y) in zip(years, brands):
    plt.text(x, y + 10, f'{y}', ha='center', va='bottom', fontsize=9, color='darkblue')

# Adding titles and labels
plt.title('Rise of Eco-Friendly Fashion Brands (2010-2020)', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Brands', fontsize=12)

# Adding a legend
plt.legend(['Number of Eco-Friendly Brands'], loc='upper left', fontsize=10)

# Enhance readability
plt.xticks(years)
plt.yticks(np.arange(0, 501, 50))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show plot
plt.show()