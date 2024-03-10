from algorithms import fcfs, round_robin, sjf, ljf, priority_scheduling
from process import Process
from prettytable import PrettyTable
import matplotlib.pyplot as plt

processes = [
    Process(1, 0, 1, 7),
    Process(2, 1, 5, 6),
    Process(3, 2, 7, 8),
    Process(4, 3, 6, 3),
    Process(5, 4, 4, 5),
    Process(6, 5, 9, 8),
    Process(7, 6, 7, 6),
    Process(8, 7, 4, 4),
    Process(9, 8, 7, 9),
    Process(10, 9, 4, 5),
    Process(11, 10, 2, 9),
    Process(12, 11, 9, 9),
    Process(13, 12, 6, 4),
    Process(14, 13, 7, 1),
    Process(15, 14, 8, 1),
    Process(16, 15, 5, 9),
    Process(17, 16, 4, 5),
    Process(18, 17, 6, 3),
    Process(19, 18, 7, 2),
    Process(20, 19, 5, 7),
    Process(21, 20, 10, 15), #transient event
    Process(22, 21, 3, 10),
    Process(23, 22, 5, 1),
    Process(24, 23, 7, 8),
    Process(25, 24, 8, 8),
    Process(26, 25, 5, 5),
    Process(27, 26, 4, 7),
    Process(28, 27, 7, 3),
    Process(29, 28, 9, 2),
    Process(30, 29, 6, 7),
]

time_slice = 2

# FCFS
avg_waiting_time_fcfs, avg_turnaround_time_fcfs = fcfs(processes.copy())

# Round Robin
avg_waiting_time_rr, avg_turnaround_time_rr = round_robin(processes.copy(), time_slice)

# SJF
avg_waiting_time_sjf, avg_turnaround_time_sjf = sjf(processes.copy())

# LJF
avg_waiting_time_ljf, avg_turnaround_time_ljf = ljf(processes.copy())

# Priority Scheduling
avg_waiting_time_priority, avg_turnaround_time_priority = priority_scheduling(processes.copy())

# Create a new PrettyTable instance
table = PrettyTable()

# Define table headers
table.field_names = ["Algorithm", "Avg Waiting Time", "Avg Turnaround Time"]

# Add rows of data
# Add rows of data with values rounded to 3 decimal places
table.add_row(["FCFS", round(avg_waiting_time_fcfs, 3), round(avg_turnaround_time_fcfs, 3)])
table.add_row(["Round Robin", round(avg_waiting_time_rr, 3), round(avg_turnaround_time_rr, 3)])
table.add_row(["SJF", round(avg_waiting_time_sjf, 3), round(avg_turnaround_time_sjf, 3)])
table.add_row(["LJF", round(avg_waiting_time_ljf, 3), round(avg_turnaround_time_ljf, 3)])
table.add_row(["Priority Scheduling", round(avg_waiting_time_priority, 3), round(avg_turnaround_time_priority, 3)])

# Print the table
print(table)


# Algorithm names
algorithms = ["FCFS", "Round Robin", "SJF", "LJF", "Priority Scheduling"]

# Formatting the average waiting times and turnaround times to include only 3 decimal places
# Average waiting times adjusted to include only 3 decimal places while preserving data type
avg_waiting_times = [
    round(avg_waiting_time_fcfs, 3),
    round(avg_waiting_time_rr, 3),
    round(avg_waiting_time_sjf, 3),
    round(avg_waiting_time_ljf, 3),
    round(avg_waiting_time_priority, 3)
]

# Average turnaround times adjusted to include only 3 decimal places while preserving data type
avg_turnaround_times = [
    round(avg_turnaround_time_fcfs, 3),
    round(avg_turnaround_time_rr, 3),
    round(avg_turnaround_time_sjf, 3),
    round(avg_turnaround_time_ljf, 3),
    round(avg_turnaround_time_priority, 3)
]


# Create a bar plot for average waiting times
plt.figure(figsize=(10, 6))
plt.bar(algorithms, avg_waiting_times, color='skyblue')
plt.xlabel('Algorithm')
plt.ylabel('Average Waiting Time')
plt.title('Comparison of Average Waiting Time')
plt.ylim(0, max(avg_waiting_times) * 1.2)  # Set y-axis limit to add some padding
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

# Create a bar plot for average turnaround times
plt.figure(figsize=(10, 6))
plt.bar(algorithms, avg_turnaround_times, color='lightgreen')
plt.xlabel('Algorithm')
plt.ylabel('Average Turnaround Time')
plt.title('Comparison of Average Turnaround Time')
plt.ylim(0, max(avg_turnaround_times) * 1.2)  # Set y-axis limit to add some padding
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

