import matplotlib.pyplot as plt
import numpy as np

# Original data for weeks, coffee consumption, and pages written
weeks = np.arange(1, 9)
coffee_consumption = [15, 20, 18, 22, 24, 20, 21, 25]
pages_written = [30, 35, 32, 40, 45, 42, 44, 50]

# New data for the additional subplot: Total cumulative figures
cumulative_coffee = np.cumsum(coffee_consumption)
cumulative_pages = np.cumsum(pages_written)

# Create subplots side by side
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(16, 7))

# First subplot: Original data as line plots
axs[0].plot(weeks, coffee_consumption, label='Coffee Consumption (cups)',
            color='saddlebrown', marker='o', linestyle='--', linewidth=2)
axs[0].plot(weeks, pages_written, label='Pages Written',
            color='royalblue', marker='s', linestyle='-', linewidth=2)

# Annotate points on the first subplot
for i, (coffee, pages) in enumerate(zip(coffee_consumption, pages_written)):
    axs[0].annotate(f'{coffee} cups', (weeks[i], coffee - 1),
                    textcoords="offset points", xytext=(-15, -15), ha='center', color='saddlebrown')
    axs[0].annotate(f'{pages} pages', (weeks[i], pages + 1),
                    textcoords="offset points", xytext=(-15, 10), ha='center', color='royalblue')

# Set labels, title, and other properties for the first subplot
axs[0].set_xlabel('Week', fontsize=12)
axs[0].set_ylabel('Amount', fontsize=12)
axs[0].set_title('Weekly Coffee Consumption\nand Productivity Among Writers',
                 fontsize=14, weight='bold')
axs[0].legend(loc='upper left', fontsize=10)
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].set_xlim(0.5, 8.5)
axs[0].set_ylim(10, 55)
axs[0].set_xticks(weeks)
axs[0].set_yticks(np.arange(10, 60, 5))

# Second subplot: Cumulative data as a bar chart
width = 0.35  # width of the bars
axs[1].bar(weeks - width/2, cumulative_coffee, width=width, label='Cumulative Coffee (cups)', color='saddlebrown', alpha=0.7)
axs[1].bar(weeks + width/2, cumulative_pages, width=width, label='Cumulative Pages Written', color='royalblue', alpha=0.7)

# Set labels, title, and other properties for the second subplot
axs[1].set_xlabel('Week', fontsize=12)
axs[1].set_ylabel('Cumulative Amount', fontsize=12)
axs[1].set_title('Cumulative Coffee Consumption\nvs. Pages Written', fontsize=14, weight='bold')
axs[1].legend(loc='upper left', fontsize=10)
axs[1].set_xlim(0.5, 8.5)
axs[1].set_ylim(0, np.max(cumulative_pages) + 10)
axs[1].set_xticks(weeks)
axs[1].grid(True, linestyle='--', alpha=0.6)

# Automatically adjust the layout to ensure no overlapping
plt.tight_layout()

# Display the plot
plt.show()