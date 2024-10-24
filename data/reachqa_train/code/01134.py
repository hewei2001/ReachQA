import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import get_cmap

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Artificial data for programming language usage in percentages
python = np.array([10, 15, 20, 25, 30, 40, 50, 55, 60, 65, 70])
javascript = np.array([30, 35, 40, 50, 55, 60, 60, 62, 65, 68, 70])
java = np.array([50, 45, 40, 35, 30, 25, 20, 20, 18, 17, 15])
csharp = np.array([5, 5, 5, 6, 7, 8, 8, 10, 12, 13, 15])
ruby = np.array([5, 5, 5, 5, 5, 7, 9, 8, 5, 4, 3])

# Calculate bottom positions for stacking
bottom_js = python
bottom_java = bottom_js + javascript
bottom_csharp = bottom_java + java
bottom_ruby = bottom_csharp + csharp

# Set up color gradients
cmap = get_cmap('tab20b')
colors = [cmap(i) for i in range(5)]

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})
fig.suptitle('Programming Languages Usage and Trends in Tech Startups\n(2010-2020)', fontsize=16, fontweight='bold')

# Stacked bar chart
ax1.bar(years, python, label='Python', color=colors[0], width=0.6, alpha=0.9)
ax1.bar(years, javascript, bottom=bottom_js, label='JavaScript', color=colors[1], width=0.6, alpha=0.9)
ax1.bar(years, java, bottom=bottom_java, label='Java', color=colors[2], width=0.6, alpha=0.9)
ax1.bar(years, csharp, bottom=bottom_csharp, label='C#', color=colors[3], width=0.6, alpha=0.9)
ax1.bar(years, ruby, bottom=bottom_ruby, label='Ruby', color=colors[4], width=0.6, alpha=0.9)

ax1.set_ylabel('Usage Percentage', fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha="right")
ax1.legend(loc='upper left', title='Programming Languages', fontsize=10, title_fontsize='12')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate data values on bars
for year, py, js, ja, cs, rb in zip(years, python, javascript, java, csharp, ruby):
    ax1.text(year, py/2, f'{py}%', ha='center', va='center', color='white', fontsize=9)
    ax1.text(year, bottom_js[np.where(years == year)][0] + js/2, f'{js}%', ha='center', va='center', color='white', fontsize=9)
    ax1.text(year, bottom_java[np.where(years == year)][0] + ja/2, f'{ja}%', ha='center', va='center', color='white', fontsize=9)
    ax1.text(year, bottom_csharp[np.where(years == year)][0] + cs/2, f'{cs}%', ha='center', va='center', color='white', fontsize=9)
    ax1.text(year, bottom_ruby[np.where(years == year)][0] + rb/2, f'{rb}%', ha='center', va='center', color='white', fontsize=9)

# Line plot for overall trend
overall_usage = python + javascript + java + csharp + ruby
ax2.plot(years, overall_usage, marker='o', linestyle='-', color='#FF6F61', linewidth=2)
ax2.set_title('Overall Usage Trend', fontsize=12)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Total Usage %', fontsize=12)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45, ha="right")
ax2.grid(axis='both', linestyle='--', alpha=0.7)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()