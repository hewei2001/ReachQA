import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Genre categories with AI personalization index and engagement scores
genres = ['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Documentary', 'Fantasy', 'Romance', 'Thriller']
personalization_index = np.array([78, 83, 76, 89, 85, 88, 75, 80])
engagement_scores = np.array([70, 82, 65, 90, 87, 88, 62, 77])

# Fit a smooth curve using a quadratic function
def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the model to the data
params, covariance = curve_fit(quadratic_model, personalization_index, engagement_scores)

# Generate x values for the fitted curve
x_values = np.linspace(min(personalization_index), max(personalization_index), 200)
y_values = quadratic_model(x_values, *params)

# Plotting the data
plt.figure(figsize=(12, 7))

# Scatter plot for genre data
scatter = plt.scatter(personalization_index, engagement_scores, c='green', s=120, edgecolor='black', alpha=0.8)

# Plot the smooth curve fitting
plt.plot(x_values, y_values, 'r-', label='Quadratic Fit', linewidth=2.5)

# Annotate each point with its genre
for i, genre in enumerate(genres):
    plt.annotate(genre, (personalization_index[i], engagement_scores[i]), 
                 textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10, color='blue')

# Add titles and labels
plt.title('The Rise of AI in Entertainment:\nAudience Engagement vs Content Personalization', fontsize=16, fontweight='bold')
plt.xlabel('AI Content Personalization Index', fontsize=13)
plt.ylabel('Audience Engagement Score (%)', fontsize=13)

# Add legend
plt.legend(loc='lower right', fontsize=12)

# Customize grid
plt.grid(visible=True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()