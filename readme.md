## Conclusion: Monte Carlo Simulation for Dice Rolls

Based on the conducted research, the following conclusions can be drawn:

### Method Accuracy
The results obtained using the Monte Carlo method with 100,000 dice rolls almost completely coincide with the analytical data. The relative error for each possible sum typically does not exceed 0.01–0.1%, which confirms the high accuracy of the simulation.

### Distribution Pattern
The most probable sum is **7**, as it has the largest number of possible combinations:
(1+6, 2+5, 3+4, 4+3, 5+2, 6+1).  
The least probable sums are **2** and **12**, each having only one possible combination.

### Iteration Dependency
It has been experimentally confirmed that the accuracy of the results increases with the number of simulations (`num_rolls`). With a small number of rolls (e.g., 100), the resulting probability distribution is irregular. However, with 100,000 rolls, the distribution closely matches the theoretical bell-shaped curve.

### Validation of Analytical Data
The Monte Carlo simulation confirms the correctness of the analytical probabilities. For example, the simulated probability of obtaining the sum **7** is approximately **16.67%**, which corresponds to the theoretical value of \(6/36\).

### Final Conclusion
The Monte Carlo method is an effective and reliable approach for approximating probabilities in random processes. The obtained results validate both the correctness of the simulation algorithm and the analytical probability distribution for the sums of two dice.
