import matplotlib.pyplot as plt
import numpy as np

# Programming languages
languages = ["Python", "JavaScript", "Java", "C++", "Ruby"]

# Popularity percentages in each age group
teens = [30, 40, 20, 5, 5]
young_adults = [35, 30, 15, 10, 10]
adults = [25, 25, 30, 15, 5]

# Combined data for the pie chart
total_popularity = [sum(x) for x in zip(teens, young_adults, adults)]

# Setting the figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Bar chart settings
x = np.arange(len(languages))
bar_width = 0.25

# Bar chart creation
bars1 = ax1.bar(x - bar_width, teens, width=bar_width, label='Teens', color='#1f77b4', edgecolor='black')
bars2 = ax1.bar(x, young_adults, width=bar_width, label='Young Adults', color='#ff7f0e', edgecolor='black')
bars3 = ax1.bar(x + bar_width, adults, width=bar_width, label='Adults', color='#2ca02c', edgecolor='black')

ax1.set_title("Popularity of Programming Languages\nby Age Group (Year 2023)", fontsize=14, pad=10)
ax1.set_xlabel("Programming Language", fontsize=12)
ax1.set_ylabel("Popularity (%)", fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(languages, fontsize=10)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.legend(title='Age Groups', fontsize=10)

# Add data annotations to bar chart
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{yval}%', ha='center', va='bottom', fontsize=9, color='black')

# Pie chart creation
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
ax2.pie(total_popularity, labels=languages, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops={'edgecolor': 'black'})

ax2.set_title("Overall Popularity Distribution\nAmong Programming Languages", fontsize=14, pad=20)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()