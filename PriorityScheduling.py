# TODO Priority scheduling
# based on priority
# TODO the setup

# handling the schedule.txt
def file():
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


def prioritySchedule():
    # we will sort the list and then do FCFS
    print("Priority Scheduling")
    # taking items list from files method
    tasks = file()
    # start time
    started = 0
    # sport by priority
    # must change to int to ge able to properly sort from G -> L
    tasks = sorted(tasks, key= lambda task:int(task[1]), reverse= True)
    print(f"Sorted order: {tasks}\n")
    for i in tasks:
        print(i[0], end= " ")
        name = i[0]
        priority = i[1]
        burst = i[2]
        print(f"Started at: {started}")
        started = started + int(burst)
        print(f"Will run name: {name}")
        print(f"Priority: {priority}")
        print(f"Burst: {burst}")
        print(f"Ended at: {started}\n")


prioritySchedule()
