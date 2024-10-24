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
    category_colors = plt.colormaps['tab20'](np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, 100)

    for i, (colname, color) in enumerate(zip(transport_modes, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(district_names, widths, left=starts, height=0.5, label=colname, color=color)

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color, fmt='%.0f%%')

    ax.legend(ncols=len(transport_modes), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
    ax.set_title("Urban Commute Preferences:\nCity Transport Modal Split for 2025", pad=20)
    ax.set_xlabel("Percentage (%)")

    plt.tight_layout()
    plt.show()

plot_transport_preferences(transport_preferences, district_names, transport_modes)