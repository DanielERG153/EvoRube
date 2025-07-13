import duckdb
import numpy as np
from scipy.optimize import curve_fit

con = duckdb.connect()
df = con.sql("SELECT steps_used, best_score FROM 'data/runs.parquet' ORDER BY steps_used").df()
steps = df['steps_used'].to_numpy()
scores = df['best_score'].to_numpy()

# Exponential fit (score = a * (1 - exp(-b * steps)) + c)
def exp_fit(x, a, b, c):
    return a * (1 - np.exp(-b * x)) + c

popt, pcov = curve_fit(exp_fit, steps, scores, p0=(486, 0.001, scores[0]))
predicted_steps_to_486 = np.log(1 - (486 - popt[2]) / popt[0]) / -popt[1] if popt[1] != 0 else 'inf'
print(f"Predicted steps to 486: {predicted_steps_to_486:.2f}")

# Time per score increase
delta_scores = np.diff(scores)
delta_steps = np.diff(steps)
avg_steps_per_point = np.mean(delta_steps[delta_scores > 0] / delta_scores[delta_scores > 0])
print(f"Avg steps per score increase: {avg_steps_per_point:.2f}")