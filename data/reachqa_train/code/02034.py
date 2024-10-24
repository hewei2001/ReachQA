import matplotlib.pyplot as plt

# Define communication channels and their respective usage percentages
channels = [
    'Video Conferencing',
    'Social Media Messaging',
    'Email Communication',
    'Instant Messaging Apps',
    'Collaborative Platforms',
    'Virtual Reality Meetings'
]

usage_percentages = [25, 20, 15, 18, 12, 10]

# Define colors for each segment to enhance visual appeal
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Define explode parameters to highlight 'Video Conferencing' as the largest segment
explode = (0.1, 0, 0, 0, 0, 0)  # Only "explode" the first slice

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    usage_percentages,
    explode=explode,
    labels=channels,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    shadow=True,
    wedgeprops=dict(edgecolor='black')
)

# Enhance label appearance
plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=10, weight="bold")

# Set title and formatting
ax.set_title("Digital Communication Channels in 2025:\nProjected Usage Distribution", fontsize=14, fontweight='bold', pad=20)

# Add a legend for clarification
ax.legend(wedges, channels, title="Channels", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Ensure the layout is neat
plt.tight_layout()

# Display the plot
plt.show()