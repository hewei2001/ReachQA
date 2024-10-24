import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Define decades from 1900s to 2020s
decades = np.arange(1900, 2030, 10)

# Hypothetical interest levels in different art styles over the decades
impressionism_interest = np.array([70, 65, 60, 55, 50, 40, 30, 25, 20, 15, 10, 10, 8])
cubism_interest = np.array([5, 10, 20, 40, 60, 75, 65, 50, 40, 35, 30, 25, 20])
surrealism_interest = np.array([2, 5, 10, 20, 30, 50, 70, 80, 75, 60, 50, 40, 30])
abstract_art_interest = np.array([1, 3, 8, 15, 25, 40, 60, 70, 80, 85, 90, 95, 98])

# Create the line chart
plt.figure(figsize=(14, 10))

# Color gradients for lines
cmap = plt.get_cmap('coolwarm', 13)
colors = cmap(np.linspace(0, 1, 13))

# Plot each art style with gradients
plt.plot(decades, impressionism_interest, label='Impressionism', color='teal', linestyle='--', linewidth=1.5, marker='o')
plt.plot(decades, cubism_interest, label='Cubism', color='crimson', linestyle='-.', linewidth=1.5, marker='s')
plt.plot(decades, surrealism_interest, label='Surrealism', color='darkorange', linestyle=':', linewidth=1.5, marker='^')
plt.plot(decades, abstract_art_interest, label='Abstract Art', color='royalblue', linestyle='-', linewidth=1.5, marker='d')

# Add annotations for peak interest points
peak_years = [decades[np.argmax(impressionism_interest)], decades[np.argmax(cubism_interest)],
              decades[np.argmax(surrealism_interest)], decades[np.argmax(abstract_art_interest)]]
peak_interests = [max(impressionism_interest), max(cubism_interest), max(surrealism_interest), max(abstract_art_interest)]
art_styles = ['Impressionism', 'Cubism', 'Surrealism', 'Abstract Art']

for i, (year, interest, style) in enumerate(zip(peak_years, peak_interests, art_styles)):
    plt.annotate(f'Peak {style}', xy=(year, interest), xytext=(year + 5, interest + 5),
                 arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, color='black')

# Shaded areas between styles
plt.fill_between(decades, cubism_interest, surrealism_interest, color='gray', alpha=0.1, label='Cubism vs. Surrealism')
plt.fill_between(decades, impressionism_interest, abstract_art_interest, color='blue', alpha=0.05, label='Impressionism vs. Abstract Art')

# Set axis labels and title
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Interest Level (%)', fontsize=12)
plt.title('Evolution of Art Styles\nOver the Decades', fontsize=16, fontweight='bold')

# Add grid to the plot
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust tick positions and labels
plt.xticks(decades, rotation=45)
plt.yticks(np.arange(0, 101, 10))

# Add a legend to the plot
plt.legend(title='Art Styles', loc='upper left', fontsize=10, frameon=True)

# Use tight_layout to adjust subplot params for a better fit
plt.tight_layout()

# Display the plot
plt.show()