import matplotlib.pyplot as plt
import numpy as np

# Generate fake data for food wasted per week
weeks = ['Week 3/', 'Week 2', 'Week 3', 'Week 4']
food_waste = np.random.randint(1, 10, size=len(weeks))

# Create a bar chart of the data
fig, ax = plt.subplots()
ax.bar(weeks, food_waste)

# Set chart title and axis labels
ax.set_title('Amount of Food Wasted per Week (lbs)')
ax.set_xlabel('Weeks')
ax.set_ylabel('Amount of Food Wasted')

# Display the chart
plt.show()
