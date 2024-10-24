import matplotlib.pyplot as plt
import numpy as np

# Define the zodiac signs
zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 
                'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 
                'Capricorn', 'Aquarius', 'Pisces']

# Define the traits and corresponding scores for each zodiac sign
traits = ['Creativity', 'Leadership', 'Compassion', 'Practicality']

# Traits scores for each sign, creatively constructed
scores = {
    'Aries': [8, 9, 5, 6],
    'Taurus': [6, 5, 7, 9],
    'Gemini': [9, 6, 5, 6],
    'Cancer': [7, 4, 9, 7],
    'Leo': [8, 10, 4, 5],
    'Virgo': [5, 7, 6, 8],
    'Libra': [7, 6, 8, 5],
    'Scorpio': [5, 7, 9, 7],
    'Sagittarius': [10, 8, 5, 6],
    'Capricorn': [6, 9, 4, 10],
    'Aquarius': [9, 6, 6, 7],
    'Pisces': [8, 4, 10, 5]
}

# Function to create a radar chart for a specific zodiac sign
def create_radar_chart(labels, values, title, color):
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # Complete the loop
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color=color, alpha=0.25)
    ax.plot(angles, values, color=color, linewidth=2)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, color='grey', fontsize=10)

    ax.set_title(title, size=15, color=color, y=1.1, weight='bold')

    return fig, ax

# Set up the entire figure with multiple radar charts
plt.figure(figsize=(18, 12))
colors = plt.cm.viridis(np.linspace(0, 1, len(zodiac_signs)))

# Plot each zodiac sign's radar chart
for i, sign in enumerate(zodiac_signs):
    plt.subplot(3, 4, i+1, polar=True)
    create_radar_chart(traits, scores[sign], sign, colors[i])

# Overall title and layout adjustments
plt.suptitle("The Celestial Influence:\nAstrological Traits Across Zodiac Signs", 
             fontsize=22, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()