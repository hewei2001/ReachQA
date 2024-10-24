import matplotlib.pyplot as plt

# Define the departments
departments = ['Development', 'Marketing', 'HR', 'IT Support', 'Sales']

# Construct satisfaction score data for each department
# Each list contains the satisfaction scores (out of 10) for employees in that department
development_scores = [8, 7, 9, 7, 8, 6, 9, 8, 7, 8, 6, 9, 8, 7]
marketing_scores = [6, 5, 7, 6, 6, 5, 7, 6, 5, 6, 4, 6, 5, 7]
hr_scores = [9, 8, 9, 10, 9, 8, 9, 10, 8, 9, 10, 9, 10, 9]
it_support_scores = [7, 6, 6, 7, 5, 6, 7, 6, 7, 5, 6, 7, 6, 5]
sales_scores = [5, 6, 5, 4, 5, 6, 5, 6, 7, 5, 4, 6, 5, 4]

# Combine all the data into a single list
data = [development_scores, marketing_scores, hr_scores, it_support_scores, sales_scores]

# Plotting the horizontal box chart
plt.figure(figsize=(12, 8))

# Create a horizontal box plot
boxplot = plt.boxplot(data, vert=False, patch_artist=True, labels=departments, 
            boxprops=dict(facecolor='skyblue', color='blue'), 
            whiskerprops=dict(color='blue'),
            capprops=dict(color='blue'),
            medianprops=dict(color='red'),
            notch=True)

# Add colors to the boxes to distinguish categories
colors = ['lightgreen', 'lightcoral', 'lightblue', 'lightgoldenrodyellow', 'lightpink']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Customize the plot
plt.title("Employee Satisfaction Across Departments\nTech Company Survey Results", fontsize=16, fontweight='bold')
plt.xlabel("Satisfaction Score (0 - Very Dissatisfied, 10 - Very Satisfied)", fontsize=12)
plt.ylabel("Department", fontsize=12)

# Add a grid for better readability
plt.grid(axis='x', linestyle='--', linewidth=0.7, alpha=0.7)

# Ensure layout is neat without overlapping
plt.tight_layout()

# Display the plot
plt.show()