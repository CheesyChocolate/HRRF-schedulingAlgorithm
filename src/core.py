from module.HRRF import hrrf_scheduler
from module.user_input import get_user_input
from module.visualize import visualize_schedule
from module.visualize import print_schedule

# Getting user input
tasks_list_hrrf = get_user_input()

if tasks_list_hrrf is None:
    # Example usage:
    # [Task Name, Arrival Time, Burst Time, Waiting Time, Completion Time]
    tasks_list_hrrf = [
        ['A', 0, 3],
        ['B', 2, 5],
        ['C', 4, 2],
        ['D', 5, 4],
        ['E', 6, 2],
        ['F', 7, 3],
        ['G', 8, 2],
        ['H', 9, 4],
    ]

# Running the HRRF scheduler
scheduled_tasks_hrrf = hrrf_scheduler(tasks_list_hrrf)

# Printing the schedule
print_schedule(scheduled_tasks_hrrf)

# Visualizing the schedule using the visualize module
visualize_schedule(scheduled_tasks_hrrf)
