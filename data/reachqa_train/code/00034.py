import matplotlib.pyplot as plt
import numpy as np

district_names = ['Downtown', 'Uptown', 'Midtown', 'Suburbs', 'Industrial Area']
transport_modes = ['Cars', 'Public Transit', 'Bicycles', 'Walking', 'Others']

# Adjusted percentage distribution of transport modes in each district
transport_preferences = np.array([
    [35, 40, 10, 10, 5],  # Downtown
    [50, 25, 5, 10, 10],  # Uptown
    [25, 50, 15, 5, 5],   # Midtown
    [60, 15, 5, 15, 5],   # Suburbs
    [45, 30, 10, 10, 5],  # Industrial Area
])

def plot_transport_preferences(data, district_names, transport_modes):
    data_cum = data.cumsum(axis=1)
    category_colors = plt.cm.get_cmap('viridis', data.shape[1])

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, 100)

    for i, (colname, color) in enumerate(zip(transport_modes, category_colors.colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(district_names, widths, left=starts, height=0.5, label=colname, color=color, edgecolor='grey', alpha=0.8)

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color, fmt='%.0f%%')

    # Add grid
    ax.grid(axis='x', linestyle='--', alpha=0.7)

    # Highlight Downtown with a distinct border
    ax.get_children()[0].set_edgecolor('darkred')
    ax.get_children()[0].set_linewidth(2)

    ax.legend(ncols=len(transport_modes), bbox_to_anchor=(0.5, -0.1), loc='upper center', fontsize='small', frameon=False)
    ax.set_title("Urban Commute Preferences:\nCity Transport Modal Split for 2025", pad=20)
    ax.set_xlabel("Percentage (%)", labelpad=20)
    
    # Subtitle with insights
    fig.suptitle("Notice the dominance of public transit in Midtown", fontsize=10, fontweight='light')

    # Automatically adjust layout
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    plt.show()

plot_transport_preferences(transport_preferences, district_names, transport_modes)