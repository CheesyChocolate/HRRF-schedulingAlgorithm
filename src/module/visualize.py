# visualize.py
import matplotlib.pyplot as plt


def print_schedule(tasks_list):
    for task in tasks_list:
        print(f"Task: {task[0]}, Arrival Time: {task[1]}, Burst Time: {task[2]}, Waiting Time: {task[3]}, Completion Time: {task[4]}")

    print(f"Average Waiting Time: {sum([task[3] for task in tasks_list]) / len(tasks_list)}")


def visualize_schedule(tasks):
    fig, ax = plt.subplots()

    for i, task in enumerate(tasks):
        task_name = task[0]
        arrival_time = task[1]
        completion_time = task[4]
        waiting_time = max(0, completion_time - arrival_time - task[2])
        burst_time = task[2]

        ax.barh(task_name, width=burst_time,
                left=arrival_time, label=f'Task {task_name}')

        # Annotate with waiting time and completion time
        ax.text(arrival_time + burst_time / 2, i + 0.1,
                f'Turnaround Time: {completion_time - arrival_time}\nWaiting Time: {waiting_time}\nCompletion Time: {completion_time}',
                color='black', ha='center', va='center')

    ax.set_xlabel('Time')
    ax.set_ylabel('Tasks')
    ax.set_title('Task Schedule Visualization\nAverage Waiting Time: {:.2f}'.format(
        sum([task[3] for task in tasks]) / len(tasks)))
    ax.legend()

    plt.show()
