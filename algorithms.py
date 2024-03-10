# First Come First Served (FCFS) Scheduling
def fcfs(processes):
    """
    First Come First Served (FCFS) Scheduling algorithm.

    Args:
        processes (list): List of Process objects.

    Returns:
        tuple: A tuple containing the average waiting time and average turnaround time.
    """
    total_waiting_time = 0
    total_turnaround_time = 0
    current_time = 0

    for process in processes:
        waiting_time = max(0, current_time - process.arrival_time)
        turnaround_time = waiting_time + process.burst_time
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        current_time += process.burst_time

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    return avg_waiting_time, avg_turnaround_time


# Round Robin Scheduling
def round_robin(processes, time_slice):
    """
    Round Robin Scheduling algorithm.

    Args:
        processes (list): List of Process objects.
        time_slice (int): Time quantum for each process.

    Returns:
        tuple: A tuple containing the average waiting time and total turnaround time.
    """
    total_waiting_time = 0
    total_turnaround_time = 0
    num_processes_waited = 0
    current_time = 0

    while processes:
        process = processes.pop(0)
        if process.burst_time <= time_slice:
            total_waiting_time += max(0, current_time - process.arrival_time)
            current_time += process.burst_time
            total_turnaround_time += current_time - process.arrival_time
            num_processes_waited += 1
        else:
            total_waiting_time += max(0, current_time - process.arrival_time)
            current_time += time_slice
            process.burst_time -= time_slice
            processes.append(process)

    avg_waiting_time = total_waiting_time / num_processes_waited if num_processes_waited > 0 else 0

    return avg_waiting_time, total_turnaround_time


# Shortest Job First (SJF) Scheduling
def sjf(processes):
    """
    Shortest Job First (SJF) Scheduling algorithm.

    Args:
        processes (list): List of Process objects.

    Returns:
        tuple: A tuple containing the average waiting time and total turnaround time.
    """
    total_waiting_time = 0
    total_turnaround_time = 0
    current_time = 0

    processes.sort(key=lambda x: x.burst_time)

    for process in processes:
        total_waiting_time += current_time
        total_turnaround_time += total_waiting_time + process.burst_time
        current_time += process.burst_time

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    return avg_waiting_time, avg_turnaround_time


# Longest Job First Scheduling
def ljf(processes):
    """
    Longest Job First (LJF) Scheduling algorithm.

    Args:
        processes (list): List of Process objects.

    Returns:
        tuple: A tuple containing the average waiting time and total turnaround time.
    """
    total_waiting_time = 0
    total_turnaround_time = 0
    current_time = 0

    processes.sort(key=lambda x: x.burst_time, reverse=True)

    for process in processes:
        total_waiting_time += current_time
        total_turnaround_time += total_waiting_time + process.burst_time
        current_time += process.burst_time

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    return avg_waiting_time, avg_turnaround_time


# Priority Scheduling
def priority_scheduling(processes):
    """
    Priority Scheduling algorithm.

    Args:
        processes (list): List of Process objects.

    Returns:
        tuple: A tuple containing the average waiting time and total turnaround time.
    """
    total_waiting_time = 0
    total_turnaround_time = 0
    current_time = 0

    processes.sort(key=lambda x: x.priority, reverse=True)

    for process in processes:
        total_waiting_time += current_time
        total_turnaround_time += total_waiting_time + process.burst_time
        current_time += process.burst_time

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    return avg_waiting_time, avg_turnaround_time

#####
#####
#####

