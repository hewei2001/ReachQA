import matplotlib.pyplot as plt

# Languages and their estimated number of native speakers in millions
languages = ['Mandarin', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian']
native_speakers = [918, 460, 377, 341, 274, 273, 258, 154]

# Total number of native speakers for proportions
total_native_speakers = sum(native_speakers)

# Colors for each segment of the pie chart
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#ff6666', '#99e6e6']

# Prepare the explode setting to highlight Mandarin (most spoken language)
explode = [0.1 if language == 'Mandarin' else 0 for language in languages]

# Plotting the pie chart
plt.figure(figsize=(10, 8))
plt.pie(
    native_speakers,
    labels=languages,
    colors=colors,
    autopct=lambda p: '{:.1f}%'.format(p) if p > 5 else '',
    startangle=140,
    pctdistance=0.85,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black'}
)

# Draw circle for a donut-style plot
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Title and legend
plt.title("Global Language Diversity:\nNative Speakers of Top Languages", fontsize=14, fontweight='bold')
plt.legend(languages, title="Languages", loc="center left", bbox_to_anchor=(1, 0.5))

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()