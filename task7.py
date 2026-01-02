import random
import pandas as pd

def monte_carlo_dice(rolls=100000):
    counts = {i: 0 for i in range(2, 13)}
    for _ in range(rolls):
        counts[random.randint(1, 6) + random.randint(1, 6)] += 1
    return {s: (c / rolls) * 100 for s, c in counts.items()}

# Compare results
sim_results = monte_carlo_dice()
print("Sum | Monte Carlo % | Analytical %")
analytical = {2:2.78, 3:5.56, 4:8.33, 5:11.11, 6:13.89, 7:16.67, 8:13.89, 9:11.11, 10:8.33, 11:5.56, 12:2.78}

for s in range(2, 13):
    print(f"{s:3} | {sim_results[s]:12.2f} | {analytical[s]:12.2f}")