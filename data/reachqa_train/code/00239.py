import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Popularity index data for each fashion trend
minimalism = np.array([20, 30, 45, 50, 55, 60, 70, 65, 60, 58, 55])
bohemian = np.array([40, 45, 50, 55, 60, 65, 50, 45, 40, 35, 30])
streetwear = np.array([10, 15, 25, 30, 35, 45, 55, 60, 70, 75, 80])
vintage = np.array([30, 28, 26, 25, 30, 35, 30, 25, 28, 30, 33])
athletic = np.array([15, 20, 30, 40, 50, 55, 60, 70, 80, 85, 90])

# Cumulative data for stacked plotting
cumulative_minimalism = minimalism
cumulative_bohemian = cumulative_minimalism + bohemian
cumulative_streetwear = cumulative_bohemian + streetwear
cumulative_vintage = cumulative_streetwear + vintage
cumulative_athletic = cumulative_vintage + athletic

# Plotting the stacked area chart
plt.figure(figsize=(12, 7))
plt.fill_between(years, 0, cumulative_minimalism, color='#FFDDC1', label='Minimalism')
plt.fill_between(years, cumulative_minimalism, cumulative_bohemian, color='#FFABAB', label='Bohemian')
plt.fill_between(years, cumulative_bohemian, cumulative_streetwear, color='#FFC3A0', label='Streetwear')
plt.fill_between(years, cumulative_streetwear, cumulative_vintage, color='#D5AAFF', label='Vintage')
plt.fill_between(years, cumulative_vintage, cumulative_athletic, color='#85E3FF', label='Athletic')

# Add title and labels
plt.title('Decade of Fashion:\nTrends from 2010 to 2020', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Popularity Index', fontsize=12)

# Add legend
plt.legend(loc='upper left', title='Fashion Trends')

# Customize x-axis ticks
plt.xticks(years, rotation=45)

# Add grid
plt.grid(visible=True, linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()