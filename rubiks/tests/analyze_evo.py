import duckdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

con = duckdb.connect()
# Convergence for inductive (success rate per N)
df_inductive = con.sql("SELECT scramble_n, AVG(solved::INT) AS success_rate, AVG(best_score) AS avg_score, COUNT(*) AS runs FROM 'data/runs.parquet' WHERE track='inductive' GROUP BY scramble_n ORDER BY scramble_n").df()
plt.figure(figsize=(8,5))
plt.bar(df_inductive['scramble_n'], df_inductive['success_rate'])
plt.xlabel('Scramble N')
plt.ylabel('Success Rate')
plt.title('Inductive Game Convergence')
plt.savefig('inductive_convergence.png')
plt.show()

# Random EA progress (score vs time/steps)
df_random = con.sql("SELECT steps_used, best_score FROM 'data/runs.parquet' WHERE track='random' ORDER BY steps_used").df()
steps = df_random['steps_used'].to_numpy()
scores = df_random['best_score'].to_numpy()
plt.figure(figsize= (8,5))
plt.plot(steps, scores, 'b-')
plt.xlabel('Steps')
plt.ylabel('Best Score')
plt.title('Random EA Progress')
plt.savefig('random_ea_progress.png')
plt.show()

# Exponential fit for random EA solve time
def exp_fit(x, a, b, c):
    return a * (1 - np.exp(-b * x)) + c
popt, pcov = curve_fit(exp_fit, steps, scores, p0=(486, 0.001, scores[0]), maxfev=10000)
predicted_steps_to_486 = np.log(1 - (486 - popt[2]) / popt[0]) / -popt[1] if popt[1] != 0 else 'inf'
print(f"Predicted steps to 486: {predicted_steps_to_486:.2f}")