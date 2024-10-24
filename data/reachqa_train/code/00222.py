import matplotlib.pyplot as plt
import numpy as np

# Define the data
libraries = [
    "Great Library of\nAlexandria", 
    "British Library", 
    "Library of Congress", 
    "Vatican Apostolic Library"
]
categories = [
    "Ancient Texts", 
    "Scientific Works", 
    "Literature & Arts", 
    "History & Geography", 
    "Religion & Philosophy", 
    "Manuscripts & Rare Books"
]

# Percentage of categories in each library
alexandria_data = [30, 10, 20, 15, 10, 15]
british_data = [5, 25, 20, 20, 5, 25]
congress_data = [10, 30, 25, 10, 5, 20]
vatican_data = [15, 10, 15, 10, 40, 10]

# Growth rates for the categories (fictitious data for radar chart)
alexandria_growth = [5, 15, 10, 5, 10, 5]
british_growth = [2, 10, 5, 10, 1, 8]
congress_growth = [3, 12, 8, 2, 5, 7]
vatican_growth = [4, 5, 4, 3, 12, 3]

# Colors for categories
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Function to plot donut and radar chart
def plot_combined_chart(data, growth_data, title, categories, colors):
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.suptitle(title, fontsize=14)
    
    # Donut Chart
    wedges, texts, autotexts = ax.pie(
        data, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors,
        pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'), textprops=dict(size=10)
    )
    
    # Center circle for donut look
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    ax.set(aspect="equal")
    
    # Radar Chart Overlay
    # Calculate angles for radar chart
    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # Reorder data and append to close the loop
    growth_data += growth_data[:1]
    angles += angles[:1]
    
    # Radar plot setup
    ax_radar = fig.add_axes([0.8, 0.1, 0.2, 0.2], polar=True)
    ax_radar.set_theta_offset(np.pi / 2)
    ax_radar.set_theta_direction(-1)
    
    ax_radar.plot(angles, growth_data, color='green', linewidth=2, linestyle='dashed', label='Growth Rate')
    ax_radar.fill(angles, growth_data, color='green', alpha=0.25)
    
    # Add radar categories
    ax_radar.set_yticklabels([])
    ax_radar.set_xticks(angles[:-1])
    ax_radar.set_xticklabels(categories, fontsize=8)
    ax_radar.set_rlabel_position(30)

    # Final layout adjustments
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    plt.show()

# Plot combined charts for each library
plot_combined_chart(alexandria_data, alexandria_growth, "Great Library of Alexandria:\nCollection Diversity & Growth", categories, colors)
plot_combined_chart(british_data, british_growth, "British Library:\nCollection Diversity & Growth", categories, colors)
plot_combined_chart(congress_data, congress_growth, "Library of Congress:\nCollection Diversity & Growth", categories, colors)
plot_combined_chart(vatican_data, vatican_growth, "Vatican Apostolic Library:\nCollection Diversity & Growth", categories, colors)