# scheduler will be assigned a set of tasks and schedule based on the selected algorithm
# each task has a priority and cpu burst.
# TODO First Come First Served (FCFS)
# schedules in the order in which they request the cpu
# TODO Priority scheduling
# based on priority
# TODO Round-robin (RR)
# each task is run for a time quantum (quantum = 3 or for the remainder of its CPU burst)
# time quantum = 10 milliseconds
# TODO FCFS and RR, use arriving order, T1, T2, T3, T4, T5, and no priority needed
# low (1 to 10) high priority
# TODO insert tasks into a list and invoke the scheduler

# FCFS
def fcfs():
    print("First Come First Serve Scheduling")
    # take file that holds tasks
    f = open("schedule.txt")

