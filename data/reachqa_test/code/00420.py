import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Functions for fitting models
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

def profitability(x, a, b):
    return a * np.log(x) + b

# Hypothetical data: Innovation scores and corresponding funding in millions of dollars
innovation_scores = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
funding_in_millions = np.array([1, 3, 2, 3, 5, 6, 7, 10, 9, 12])

# Fit the quadratic model to the funding data
popt_funding, _ = curve_fit(quadratic, innovation_scores, funding_in_millions)

# Hypothetical profitability data based on innovation scores
profitability_in_millions = np.array([0.5, 1.5, 2, 3, 3.5, 4, 4.2, 4.5, 4.6, 4.65])

# Fit the logarithmic model to the profitability data
popt_profit, _ = curve_fit(profitability, innovation_scores, profitability_in_millions)

# Create a smoother fitting curve for funding and profitability
x_fit = np.linspace(min(innovation_scores), max(innovation_scores), 1000)
y_fit_funding = quadratic(x_fit, *popt_funding)
y_fit_profit = profitability(x_fit, *popt_profit)

# Plotting the data points for funding with a scatter plot
plt.scatter(innovation_scores, funding_in_millions, color='blue', label='Startup Funding')

# Plotting the smooth fitting curve for funding
plt.plot(x_fit, y_fit_funding, color='red', linewidth=2, label='Funding Fit')

# Plotting the fitted curve for profitability with a dotted line
plt.plot(x_fit, y_fit_profit, color='green', linestyle='--', linewidth=2, label='Profitability Fit')

# Setting labels and title
plt.title('Funding & Profitability vs Innovation Score:\nA Hypothetical Perspective on Startups in Futuristic Technology')
plt.xlabel('Innovation Score (Scale 1-10)')
plt.ylabel('Value (in Millions)')

# Adding a grid for clarity and adjusting layout to avoid occlusion
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Adding a legend for clarity
plt.legend()

# Display the plot
plt.show()