# TODO Round-robin (RR)
# each task is run for a time quantum (quantum = 3 or for the remainder of its CPU burst)
# time quantum = 10 milliseconds

# handling the schedule.txt
# for FCFS

# list to hold tasks
items = []
name = []
burst = []
with open("schedule.txt", 'r') as FO:
    allLines = FO.readlines()
# remove invisible extra characters and commas
for aLine in allLines:
    aLine = aLine.replace(',', '')
    aLine = aLine.strip()
    # putting tasks into a nested list to grab individual tasks and their attributes
    items.append(aLine.split(" "))
# splitting task name and burst amount into 2 different lists
for i in items:
    name.append(i[0])
    burst.append(int(i[2]))


def waitTime(names, number, burstTime, wait, quantum):
    # remaining burst time left in task
    rem_bt = [0] * n
    for num in range(n):
        rem_bt[num] = burstTime[num]
    t = 0
    # loop around until each task is complete
    while 1:
        done = True
        for num in range(n):
            # If task still has time left
            if rem_bt[num] > 0:
                done = False
                if rem_bt[num] > quantum:
                    t += quantum
                    rem_bt[num] -= quantum
                else:
                    t = t + rem_bt[num]
                    # Waiting time is current time - time used by task
                    wait[num] = t - burstTime[num]
                    rem_bt[num] = 0
        # If all processes are done
        if done:
            break


# calculate turn around time
def turnAroundTime(names, number, burstTime, wait, tat):
    # Calculating turnaround time
    for num in range(n):
        tat[num] = burstTime[num] + wait[num]


# calculate average waiting and turn-around times.
def avgTime(names, number, burstTime, quantum):
    wt = [0] * n
    tat = [0] * n
    waitTime(names, number, burstTime, wt, quantum)
    turnAroundTime(names, number, burstTime, wt, tat)
    total_wt = 0
    total_tat = 0
    for item in range(8):
        total_wt = total_wt + wt[item]
        total_tat = total_tat + tat[item]
        # name[item] to act like for loop into name to get each name
        print(f"Will run name: {name[item]}")
        print(f"Burst: {burstTime[item]}")
        print(f"Waiting time: {wt[item]}")
        print(f"Turn-Around time: {tat[item]}")
        print()
    print("\nAverage waiting time = %.5f " % (total_wt / n))
    print("Average turn around time = %.5f " % (total_tat / n))



n = len(name)
# Time quantum
quantum = 10
avgTime(name, n, burst, quantum)
