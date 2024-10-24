import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Popularity index for each art style
abstract_expressionism = [20, 25, 30, 35, 40, 50, 60, 70, 65, 60, 58]
minimalism = [30, 35, 38, 40, 45, 55, 68, 72, 75, 80, 85]
cyberpunk_art = [10, 15, 20, 25, 35, 45, 50, 60, 65, 70, 80]

# Plotting the line chart
plt.figure(figsize=(12, 8))

plt.plot(years, abstract_expressionism, marker='o', linestyle='-', color='#FF6F61', linewidth=2, label='Abstract Expressionism')
plt.plot(years, minimalism, marker='s', linestyle='--', color='#92A8D1', linewidth=2, label='Minimalism')
plt.plot(years, cyberpunk_art, marker='^', linestyle='-.', color='#76C7C0', linewidth=2, label='Cyberpunk Art')

# Title and labels
plt.title('Evolution of Art Styles in NeoCanvas District\n(2010-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Popularity Index', fontsize=12)

# Add grid for readability
plt.grid(True, linestyle='--', alpha=0.5)

# Annotate key trends
plt.annotate('Rise of Minimalism', xy=(2015, 55), xytext=(2013, 70),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')

plt.annotate('Cyberpunk Art Surge', xy=(2019, 70), xytext=(2017, 80),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')

# Annotate each data point with its value for clarity
for i, txt in enumerate(abstract_expressionism):
    plt.text(years[i], abstract_expressionism[i] + 2, str(txt), fontsize=9, ha='center', color='#FF6F61')
    
for i, txt in enumerate(minimalism):
    plt.text(years[i], minimalism[i] + 2, str(txt), fontsize=9, ha='center', color='#92A8D1')
    
for i, txt in enumerate(cyberpunk_art):
    plt.text(years[i], cyberpunk_art[i] - 5, str(txt), fontsize=9, ha='center', color='#76C7C0')

# Legend
plt.legend(title='Art Styles', loc='upper left', fontsize=10)

# Optimize layout for better readability
plt.tight_layout()

# Display the plot
plt.show()