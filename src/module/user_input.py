def get_user_input():
    try:
        # Prompt the user to enter the number of processes
        num_processes = int(input("Enter the number of processes: "))
        if num_processes <= 0:
            raise ValueError("Number of processes should be greater than 0.")

        # Initialize an empty list to store process information
        processes = []

        # For each process, ask the user to input arrival time and burst time
        for i in range(num_processes):
            process_name = chr(ord('A') + i)
            arrival_time = int(input(f"Enter arrival time for Process {process_name}: "))
            burst_time = int(input(f"Enter burst time for Process {process_name}: "))
            processes.append([process_name, arrival_time, burst_time])

        return processes

    except ValueError as e:
        print(f"Error: {e}")
        return None
