# scheduler will be assigned a set of tasks and schedule based on the selected algorithm
# TODO First Come First Served (FCFS)
# schedules in the order in which they request the cpu
# TODO FCFS and RR, use arriving order, T1, T2, T3, T4, T5, and no priority needed
# low (1 to 10) high priority


# handling the schedule.txt
# for FCFS
def fileS():
    # list to hold tasks
    items = []
    with open("schedule.txt", 'r') as FO:
        allLines = FO.readlines()
    # remove invisible extra characters and commas
    for aLine in allLines:
        aLine = aLine.replace(',', '')
        aLine = aLine.strip()
        # putting tasks into a nested list to grab individual tasks and their attributes
        items.append(aLine.split(" "))

    print(f"This is the data we are working with: {items}\n")
    return items
    # grab T7 out of ['T7', '3', '30']
    # print(items[0][0])


def output():
    print("First Come First Serve Scheduling")
    # taking items list from fileS method
    name = fileS()
    # start time
    started = 0
    for i in name:
        name = i[0]
        priority = i[1]
        burst = i[2]
        print(f"Started at: {started}")
        started = started + int(burst)
        print(f"Will run name: {name}")
        print(f"Priority: {priority}")
        print(f"Burst: {burst}")
        print(f"Ended at: {started}\n")


output()
