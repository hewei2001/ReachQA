import matplotlib.pyplot as plt
import numpy as np

# Define the cities and sustainability indicators
cities = ['Arcadia', 'Rivertown', 'Solace City', 'Harbor Heights', 'Emerald Oasis', 'Baytown', 'Meadowville']
indicators = [
    'Green Space', 
    'Public Transport (Coverage)', 
    'Public Transport (Frequency)',
    'Public Transport (Affordability)',
    'Waste Management',
    'Air Quality', 
    'Renewable Energy', 
    'Water Conservation'
]

# Sustainability scores for each city (scale 1-10)
sustainability_scores = {
    'Arcadia': [8, 6, 7, 5, 7, 9, 5, 8],
    'Rivertown': [7, 7, 6, 7, 6, 5, 7, 7],
    'Solace City': [6, 8, 5, 7, 8, 6, 8, 6],
    'Harbor Heights': [5, 7, 8, 6, 9, 8, 6, 5],
    'Emerald Oasis': [9, 8, 9, 6, 6, 7, 9, 8],
    'Baytown': [7, 6, 7, 8, 7, 6, 8, 7],
    'Meadowville': [8, 9, 7, 8, 5, 7, 7, 9]
}

# Weighted scores for each category
weights = [1.0, 0.8, 0.6, 0.6, 1.0, 1.0, 1.2, 0.9]

# Function to plot radar chart for each city
def plot_radar_chart(city, scores, categories, title, benchmark_scores):
    num_vars = len(categories)

    # Calculate angle for each category
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # Complete the loop
    scores = scores + scores[:1]
    benchmark_scores = benchmark_scores + benchmark_scores[:1]
    angles = angles + angles[:1]

    # Create polar plot
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Plot and fill for city
    ax.plot(angles, scores, color='blue', linewidth=2, label=city)
    ax.fill(angles, scores, color='blue', alpha=0.25)

    # Plot and fill for benchmark
    ax.plot(angles, benchmark_scores, color='red', linewidth=2, linestyle='--', label='Benchmark')
    ax.fill(angles, benchmark_scores, color='red', alpha=0.1)

    # Set category labels
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=9)
    ax.set_ylim(0, 10)

    # Add title
    ax.set_title(title, size=14, y=1.1)

    # Add a legend
    ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

    # Adjust layout
    plt.tight_layout()

    plt.show()

# Calculating benchmark scores as the average weighted scores of all cities
benchmark_scores = []
for i in range(len(indicators)):
    benchmark_scores.append(
        sum(scores[i] * weights[i] for scores in sustainability_scores.values()) / len(sustainability_scores)
    )

# Plot radar chart for each city
for city, scores in sustainability_scores.items():
    plot_radar_chart(city, scores, indicators, f"Sustainability Scorecard for\n{city}", benchmark_scores)