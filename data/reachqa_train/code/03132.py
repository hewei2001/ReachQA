import matplotlib.pyplot as plt

# Communication methods and their respective usage percentages
methods = ['Face-to-Face', 'Phone Calls', 'Text Messaging', 'Email', 'Video Calls', 'Social Media', 'VR Meetings']
percentages_2023 = [25, 15, 20, 15, 10, 10, 5]
percentages_2033 = [15, 10, 15, 10, 20, 20, 10]

# Colors for each communication method segment
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#C0C0C0', '#FF69B4']

# Create a figure with a 1x2 grid to compare both years
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Plot the 2023 donut chart
wedges_2023, texts_2023, autotexts_2023 = ax1.pie(percentages_2023, labels=methods, autopct='%1.1f%%', startangle=140, 
                                                  colors=colors, wedgeprops=dict(width=0.3), pctdistance=0.85,
                                                  explode=[0.1 if method == 'Face-to-Face' else 0 for method in methods])
ax1.set_title('Communication Methods in 2023', fontsize=14)

# Plot the 2033 donut chart
wedges_2033, texts_2033, autotexts_2033 = ax2.pie(percentages_2033, labels=methods, autopct='%1.1f%%', startangle=140, 
                                                  colors=colors, wedgeprops=dict(width=0.3), pctdistance=0.85,
                                                  explode=[0.1 if method == 'Virtual Reality Meetings' else 0 for method in methods])
ax2.set_title('Communication Methods in 2033', fontsize=14)

# Customize the text properties for both charts
for autotext in autotexts_2023 + autotexts_2033:
    autotext.set_color('black')
    autotext.set_fontsize(10)
for text in texts_2023 + texts_2033:
    text.set_fontsize(11)

# Add a central circle for the donut chart effect
for ax in [ax1, ax2]:
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    ax.add_artist(centre_circle)

# Adjust layout to ensure no overlapping and all elements are visible
plt.tight_layout()

# Add a super title to the entire figure
plt.suptitle("Evolution of Communication Methods:\nA Decade's Perspective", fontsize=16, fontweight='bold', y=1.05)

# Add a legend outside of the plots
plt.legend(wedges_2023, methods, title="Methods", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Display the chart
plt.show()