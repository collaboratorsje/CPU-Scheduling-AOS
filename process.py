class Process:
    """
    Represents a process with a unique process ID, arrival time, burst time,
    and optional priority.
    """
    def __init__(self, pid, arrival_time, burst_time, priority=None):
        """
         Initialize a Process object.

         Args:
             pid (int): Process ID.
             arrival_time (int): Arrival time of the process.
             burst_time (int): Burst time required for the process execution.
             priority (int, optional): Priority of the process (default is None).
         """
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority if priority is not None else 0  # Assign a default priority if not specified
