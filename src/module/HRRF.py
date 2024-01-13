def hrrf_scheduler(tasks):
    current_time = 0
    scheduled_tasks = []

    while tasks:
        response_ratios = [(i, (current_time - arrival_time + burst_time) / burst_time) for i, (_, arrival_time, burst_time) in enumerate(tasks)]
        # Sort tasks based on response ratio (higher first)
        response_ratios.sort(key=lambda x: x[1], reverse=True)

        selected_task_index = response_ratios[0][0]
        selected_task = tasks.pop(selected_task_index)

        waiting_time = max(0, current_time - selected_task[1])
        completion_time = current_time + selected_task[2]

        # Append task with completion time to the scheduled_tasks list
        scheduled_task = selected_task + [waiting_time, completion_time]
        scheduled_tasks.append(scheduled_task)

        current_time = completion_time

    return scheduled_tasks
