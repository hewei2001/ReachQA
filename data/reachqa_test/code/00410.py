import matplotlib.pyplot as plt

# Data for 2013-2023 average internet speeds (in Mbps) for each region and connection type
internet_speeds = {
    'North America': {
        'Mobile': [15, 25, 33, 42, 55, 69, 85, 102, 120, 135, 150],
        'Fixed Broadband': [30, 40, 52, 65, 80, 100, 125, 150, 180, 200, 220]
    },
    'Europe': {
        'Mobile': [9, 14, 18, 20, 26, 32, 38, 44, 50, 56, 60],
        'Fixed Broadband': [18, 24, 30, 35, 40, 47, 55, 65, 75, 85, 90]
    },
    # Add extra speed measurement for 2023 for all other regions and connections as well
    # Here as an example, Europe is shown, similarly add for other regions
}

# Years corresponding to the internet speed measurements
years = list(range(2013, 2024))

# Function to plot the data
def plot_global_internet_speed_trends(years, internet_speeds):
    plt.figure(figsize=(20, 12))

    # Plotting the data for each region and connection type
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'magenta', 'cyan']
    markers = ['o', 's', '^', '*', 'D', 'p', 'h']
    linestyles = ['-', '--', '-.', ':']
    marker_size = 8
    for i, (region, connections) in enumerate(internet_speeds.items()):
        for j, (connection, speeds) in enumerate(connections.items()):
            color = colors[i % len(colors)]
            marker = markers[i % len(markers)]
            linestyle = linestyles[j]
            plt.plot(years, speeds, marker=marker, linestyle=linestyle, color=color,
                     markersize=marker_size, label=f"{region} - {connection}")

    # Setting chart title and axis labels
    plt.title('Global Internet Speed Trends Over the Decade\n(2013-2023)')
    plt.xlabel('Year')
    plt.ylabel('Average Internet Speed (Mbps)')

    # Adjust the y-axis to have a proper tick spacing
    plt.yticks(range(0, 220, 20))
    plt.xticks(years)

    # Adding a grid
    plt.grid(True, which='major', linestyle='--', linewidth='0.5', alpha=0.7)
    plt.minorticks_on()
    plt.grid(True, which='minor', linestyle=':', linewidth='0.25', alpha=0.7)

    # Legend and adjusting layout
    plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
    plt.tight_layout()

    # Show the plot
    plt.show()

# Call the plotting function
plot_global_internet_speed_trends(years, internet_speeds)