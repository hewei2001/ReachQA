import matplotlib.pyplot as plt
import numpy as np

# Expanded technology hubs and additional tech industries
hubs = ['Silicon Valley', 'Bangalore', 'Beijing', 'Berlin', 'Tel Aviv', 'Shanghai']
industries = ['Software', 'Hardware', 'Biotech', 'AI', 'Fintech', 'Edtech', 'Cybersecurity', 'Green Energy']

# Startup success rates for startups in various technology hubs and expanded industries
startup_success = np.array([
    [82, 76, 65, 80, 87, 80, 73, 78],  # Silicon Valley: Software, Hardware, Biotech, AI, Fintech, Edtech, Cybersecurity, Green Energy
    [70, 48, 42, 72, 76, 58, 67, 64],  # Bangalore: Software, Hardware, Biotech, AI, Fintech, Edtech, Cybersecurity, Green Energy
    [59, 73, 54, 78, 61, 49, 70, 67],  # Beijing: Software, Hardware, Biotech, AI, Fintech, Edtech, Cybersecurity, Green Energy
    [68, 64, 47, 74, 62, 55, 67, 72],  # Berlin: Software, Hardware, Biotech, AI, Fintech, Edtech, Cybersecurity, Green Energy
    [75, 56, 48, 77, 73, 58, 62, 64],  # Tel Aviv: Software, Hardware, Biotech, AI, Fintech, Edtech, Cybersecurity, Green Energy
    [67, 62, 55, 76, 70, 57, 69, 67]   # Shanghai: Software, Hardware, Biotech, AI, Fintech, Edtech, Cybersecurity, Green Energy
])

# Adjust figure size based on expanded dimensions
fig, ax = plt.subplots(figsize=(15, 10))

# Use pcolormesh for irregular grid data
heatmap = ax.pcolormesh(startup_success, cmap='YlGnBu', vmin=40, vmax=90)

# Set labels and title
ax.set_title('Global Startup Success Rates in Key Tech Hubs\n2010s-2020s\n', fontdict={'fontsize': 16})
ax.set_xlabel('Tech Industries', fontsize=14)
ax.set_ylabel('Global Tech Hubs', fontsize=14)

# Set tick locations and labels to match the data grid
ax.set_xticks(np.arange(len(industries)) + 0.5)
ax.set_yticks(np.arange(len(hubs)) + 0.5)
ax.set_xticklabels(industries)
ax.set_yticklabels(hubs)

# Rotate x-tick labels for readability
plt.xticks(rotation=65, ha='right')

# Increase tick label fontsize for better visibility
ax.tick_params(axis='both', which='major', labelsize=12)

# Add color bar with label
cbar = fig.colorbar(heatmap, ax=ax, orientation='vertical')
cbar.set_label('Startup Success Rate (%)', fontsize=14)

# Annotate each cell with data values for clarity
for i in range(startup_success.shape[0]):
    for j in range(startup_success.shape[1]):
        text = ax.text(j + 0.5, i + 0.5, startup_success[i, j],
                       ha='center', va='center', color='black', fontsize=10)

# Adjust layout to prevent text overlapping
plt.tight_layout()

# Display the chart
plt.show()