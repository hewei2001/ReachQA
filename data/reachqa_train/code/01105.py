import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects

# Expanded data set with more tea types
tea_types = [
    'Green Tea', 'Black Tea', 'Herbal Tea', 'Oolong Tea', 'White Tea', 
    'Matcha', 'Chamomile', 'Earl Grey', 'Jasmine', 'Chai'
]
consumption_percentages = [20, 25, 10, 8, 7, 5, 6, 9, 5, 5]

# Colors for each tea type, designed for clear visual distinction
colors = ['#76c7c0', '#ff6347', '#98fb98', '#8a2be2', '#ffeb3b', 
          '#ff69b4', '#dda0dd', '#4b0082', '#ffdead', '#8b4513']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect="equal"))

# Define explode to emphasize top and least consumed teas
explode = [0.1 if percent >= 10 else 0 for percent in consumption_percentages]

# Plotting the donut pie chart
wedges, texts, autotexts = ax.pie(
    consumption_percentages,
    labels=tea_types,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    explode=explode,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Enhance the visual appeal with shadow effects
plt.gca().set_frame_on(True)
plt.setp(wedges, path_effects=[
    PathEffects.withStroke(linewidth=3, foreground='white')
])

# Add a subtitle for additional clarity and depth
plt.title('Global Tea Consumption Preferences\nA Study of Different Tea Types', fontsize=14, fontweight='bold', pad=20)

# Customize the autotexts for better readability
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Adjust legend position and avoid overlap
plt.legend(wedges, tea_types, title="Tea Types", loc="upper right", bbox_to_anchor=(1.2, 1), fontsize=10)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Second chart: Bar plot for statistical insights
fig, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(tea_types, consumption_percentages, color=colors)
ax2.set_title('Tea Consumption Comparison', fontsize=14, fontweight='bold')
ax2.set_ylabel('Consumption Percentage (%)')
ax2.set_xlabel('Tea Types')
ax2.set_xticklabels(tea_types, rotation=45, ha='right')

# Add labels to each bar for clarity
for i, v in enumerate(consumption_percentages):
    ax2.text(i, v + 0.5, f"{v}%", color='black', ha='center', fontsize=10, fontweight='bold')

# Adjust layout for the bar plot
plt.tight_layout()

# Show the plots
plt.show()