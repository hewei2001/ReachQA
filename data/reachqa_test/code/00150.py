import matplotlib.pyplot as plt
import seaborn as sns

# Define the demographics and their macronutrient preferences
demographics = ['Young Adults\n(18-35)', 'Middle-Aged\nAdults (36-55)', 'Seniors\n(56+)']
macronutrient_labels = ['Carbohydrates', 'Proteins', 'Fats']

# Macronutrient preferences in percentages for each demographic
young_adults = [50, 30, 20]  # Carbs, Proteins, Fats
middle_aged_adults = [40, 35, 25]
seniors = [30, 45, 25]

# Combine data for plotting
macronutrient_data = [young_adults, middle_aged_adults, seniors]

# Define a color palette
colors = sns.color_palette("pastel", 3)

# Exploding the first slice for each pie chart
explode_values = [(0.1 if i == 0 else 0) for i in range(len(macronutrient_labels))]

# Create a figure with multiple pie charts
fig, axes = plt.subplots(1, 3, figsize=(20, 7), subplot_kw={'aspect': 'equal'}, facecolor='lavender')

for ax, data, title in zip(axes, macronutrient_data, demographics):
    wedges, texts, autotexts = ax.pie(data, labels=macronutrient_labels, autopct='%1.1f%%',
                                      startangle=140, colors=colors, textprops=dict(color="darkblue"),
                                      explode=explode_values, shadow=True, wedgeprops=dict(edgecolor='w'))
    
    # Enhance text visibility and format
    plt.setp(autotexts, size=10, weight="bold")
    ax.set_title(title, fontsize=14, fontweight='bold', color='darkgreen')

# Add global legend
fig.legend(wedges, macronutrient_labels, loc='upper right', fontsize=12, title="Macronutrients")

# Main title for the chart
plt.suptitle("Nutrition Awareness:\nDistribution of Macronutrient Preferences Among Diverse Demographics", 
             fontsize=18, fontweight='bold', color='darkblue')

# Data source and additional note
plt.figtext(0.5, 0.02, "Data source: Health Survey 2023\nNote: Percentages reflect general dietary preferences within demographics",
            ha="center", fontsize=10, color='gray')

# Adjust layout
plt.tight_layout(rect=[0, 0.05, 1, 0.95])

# Show the plot
plt.show()