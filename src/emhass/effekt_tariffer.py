import pandas as pd
import numpy as np
from calendar import monthrange

n = 1  # Number of top power values to track per day
m = 3  # Number of top daily power values to track per month
månad = monthrange(2025, 1)[1]  # Number of days in January 2025

P_max_dag = [0] * n  # List to store daily peak values
P_max_månad = [0] * m  # List to store monthly peak values

# Load CSV file
fil = "/config/fake_power_data.csv"  # Adjust path as needed
a = pd.read_csv(fil, decimal=',', sep=';')
data = pd.DataFrame(a)

# Convert Pel [Wel] column to a list of integers
Pe = np.array(data['Pel [Wel]'])
Pel = [int(num) for num in Pe]

total_daily_peaks = 0

# Make sure the list is large enough to hold 24 * number of days
if len(Pel) < månad * 24:
    print("Error: Not enough data for the specified number of days.")
else:
    for b in range(månad):  # Iterate over days of the month
        P_max_dag.clear()  # Clear daily max list for each day

        for i in range(24):  # Loop through 24 hours per day
            E = Pel[b * 24 + i]  # Get the power for the current hour
            if E >= P_max_dag[-1] if P_max_dag else -1:  # If it's a new peak
                P_max_dag.append(E)
                P_max_dag.sort(reverse=True)  # Keep list sorted in descending order
                P_max_dag = P_max_dag[:n]  # Keep only the top n elements

        # Calculate the daily peak (average of the top n values)
        P_dag = sum(P_max_dag) / n if n > 0 else 0  # Avoid division by zero
        total_daily_peaks = total_daily_peaks + P_dag

        if P_dag >= P_max_månad[-1]:  # If it's a new monthly peak
            P_max_månad.append(P_dag)
            P_max_månad.sort(reverse=True)
            P_max_månad = P_max_månad[:m]  # Keep only the top m daily peaks

tariff = 82
average_daily_peak = total_daily_peaks / månad
if int(sum(P_max_månad) / m) > int(1.1*average_daily_peak):
    print(str(int(sum(P_max_månad) / m)))
else:
    print(str(int(1.1*average_daily_peak)))


cost = tariff*(sum(P_max_månad)/1000*m)


# Output only the P_max_månad value (average of top m values)
# print(str(int(sum(P_max_månad) / m)))
