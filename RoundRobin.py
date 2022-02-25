# TODO Round-robin (RR)
# each task is run for a time quantum (quantum = 3 or for the remainder of its CPU burst)
# time quantum = 10 milliseconds

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
    task = fileS()
    # start time
    started = 0
    for i in task:
        name = i[0]
        priority = i[1]
        burst = i[2]
        quantum = 10
        # TODO change while loop placement, constantly runs only T1
        #  so that it will loop as long as there are tasks with burst time
        # while loop to constantly loop until we have completed all of our tasks
        while len(task) > 0:
            # subtracting quantum each time we loop around so we know what tasks still need to run
            rem = int(burst) - quantum
            # if tasks still require more time to run
            if rem != 0:
                print(f"{name} still has burst left!")
                print(f"Started at: {started}")
                started = started + int(burst)
                print(f"Will run name: {name}")
                print(f"Burst: {burst}")
                print(f"remaining burst: {rem}\n")
            # if tasks have completed running we pop them from the list
            elif rem == 0:
                place = task.index(i)
                task[place].pop()

    print(f"New task list: {task}")


output()


