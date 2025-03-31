
# Weekly Step Count Analysis

## Introduction

Tracking daily steps helps monitor physical activity levels. This report analyzes my step count over a week and compares it with my friends'.

## Methodology

The data was collected using a **fitness tracker** over seven days and compared across three individuals.

## Data Collection

- **Source:** Fitness tracker
- *Duration:* One week
- Comparison: Self vs. Friends

## Daily Step Counts

| Day        | My Steps | Friend A | Friend B |
|------------|---------|----------|----------|
| Monday     | 8,000   | 9,500    | 7,200    |
| Tuesday    | 7,500   | 8,000    | 6,800    |
| Wednesday  | 10,000  | 11,200   | 9,500    |
| Thursday   | 6,200   | 7,800    | 7,100    |
| Friday     | 12,000  | 12,500   | 11,200   |
| Saturday   | 14,500  | 13,000   | 12,800   |
| Sunday     | 9,800   | 10,200   | 9,900    |

## Key Observations

- **Highest step count:** Saturday with 14,500 steps.
- *Lowest step count:* Thursday with 6,200 steps.
- Friday and Saturday had the most consistent step counts among all participants.

## Code for Data Visualization

To visualize the data, the following Python code generates a step count bar chart:

```python
import matplotlib.pyplot as plt
import numpy as np

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
my_steps = [8000, 7500, 10000, 6200, 12000, 14500, 9800]
friend_a_steps = [9500, 8000, 11200, 7800, 12500, 13000, 10200]
friend_b_steps = [7200, 6800, 9500, 7100, 11200, 12800, 9900]

x = np.arange(len(days))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width, my_steps, width, label='My Steps', color='blue')
ax.bar(x, friend_a_steps, width, label='Friend A', color='green')
ax.bar(x + width, friend_b_steps, width, label='Friend B', color='red')

ax.set_xlabel("Days of the Week")
ax.set_ylabel("Steps")
ax.set_title("Weekly Step Count Comparison")
ax.set_xticks(x)
ax.set_xticklabels(days, rotation=45)
ax.legend()
plt.show()
```

## Comparison with Friends

> "Walking with a friend in the dark is better than walking alone in the light." – Helen Keller

Friendly competition helps in increasing daily step counts.

## Next Steps

1. **Increase daily step goal** to maintain higher averages.
2. Walk with friends for motivation.
3. Track step counts over a longer period.

## Additional Resources

For more on physical activity, visit [CDC Physical Activity Guidelines](https://www.cdc.gov/physicalactivity/basics/index.htm).

## Visual Summary

![Step Count Chart](https://example.com/step_chart.jpg)
