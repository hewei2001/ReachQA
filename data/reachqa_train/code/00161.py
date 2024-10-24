import matplotlib.pyplot as plt
import numpy as np

# Data: Interstellar dishes and their flavor profiles
dishes = ['Zenorian Delight', 'Martian Spice Medley', 'Andromedan Fruit Salad', 'Lunar Tidal Soup']
flavors = ['Sweetness', 'Spiciness', 'Umami', 'Sourness', 'Saltiness', 'Bitterness']

# Flavor scores for each dish
flavor_profiles = {
    'Zenorian Delight': [8, 3, 6, 5, 2, 4],
    'Martian Spice Medley': [4, 9, 7, 3, 5, 6],
    'Andromedan Fruit Salad': [10, 2, 4, 8, 3, 5],
    'Lunar Tidal Soup': [3, 5, 9, 4, 7, 3]
}

# Calculate average flavor scores for the bar chart
average_flavors = [np.mean([profile[i] for profile in flavor_profiles.values()]) for i in range(len(flavors))]

# Function to plot radar and bar charts
def plot_combined_charts(dish, scores, avg_scores, categories, title):
    num_vars = len(categories)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    # Create subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Radar chart
    ax = plt.subplot(121, polar=True)
    scores += scores[:1]
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.plot(angles, scores, linewidth=1.5, linestyle='solid', label=dish)
    ax.fill(angles, scores, color='cyan', alpha=0.3)
    ax.set_ylim(0, 10)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=8)
    ax.set_yticks(range(1, 11))
    ax.set_yticklabels(map(str, range(1, 11)), fontsize=7)
    ax.set_title(title, size=14, y=1.1)

    # Bar chart
    axs[1].bar(categories, avg_scores, color='orange', alpha=0.7)
    axs[1].set_ylim(0, 10)
    axs[1].set_ylabel('Average Flavor Score', fontsize=10)
    for index, value in enumerate(avg_scores):
        axs[1].text(index, value + 0.2, f'{value:.1f}', ha='center', fontsize=9)
    axs[1].set_title('Average Flavor Profile Across All Dishes', size=14)

    plt.tight_layout()
    plt.show()

# Plot combined charts for each dish
for dish, scores in flavor_profiles.items():
    plot_combined_charts(dish, scores, average_flavors, flavors, f"Flavor Profile of\n{dish}")