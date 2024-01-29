def init_tasks():
    return [
        {'id': 1, 'description': "Complete Project Proposal", 'assigned_to': "John Doe", "subtasks": [
            {'id': 2, 'description': "Research", 'assigned_to': "Alice Brown", 'time_estimate': 5},
            {'id': 3, 'description': "Outline", 'assigned_to': "Bob Johnson", 'subtasks': [
                {'id': 4, 'description': "Introduction", 'assigned_to': "Jane Smith", 'time_estimate': 3},
                {'id': 5, 'description': "Body", 'assigned_to': "Jane Smith", 'time_estimate': 6},
                {'id': 6, 'description': "Conclusion", 'assigned_to': "David Wilson", 'time_estimate': 2}
            ]}
        ]}]

def displayOperations():
    """
    This function just writes the operations for an input
    """
    print("\nOperations:")
    print("\t1.Add a new task")
    print("\t2.Assign a task to a team member")
    print("\t3.Complete a task")
    print("\t4.Generate report")
    print("\t5.Exit")

def displayReport(tasks,indent):
    """
    This function partially does what generate_report_recursive does,
    but just the required part for the other functions(add_task_recursive, assign_task, complete_task_recursive)
    """
    sep = "--"
    for task in tasks:
        print(f"{indent * sep}{task['id']}.{task['description']} ({task['assigned_to']})")
        if 'subtasks' in task:
            generate_report_recursive(task['subtasks'], indent + 1)

def add_task_recursive(tasks, task_id, description, assigned_to, time_estimate, found):
    new_id = 0

    if task_id == 0:
        tasks.append({'id': search_last_id(tasks,new_id) + 1 ,
                      'description': description, 'assigned_to': assigned_to, 'time_estimate': time_estimate})
    else:
        if found:
            for task in tasks:
                if task['id'] >= task_id:
                    if 'subtasks' in task:
                        add_task_recursive(task["subtasks"], task_id, description, assigned_to, time_estimate, found)
                    else:
                        task['id'] = task["id"] + 1
        else:
            for task in tasks:
                if task.get('id') == task_id:
                    if "subtasks" in task:
                        task["subtasks"].insert(0, {'id': task_id, 'description': description,
                                                    'assigned_to': assigned_to, 'time_estimate': time_estimate})
                    found = True
                    add_task_recursive(tasks, task_id, description, assigned_to, time_estimate, found)

                elif 'subtasks' in task:
                    add_task_recursive(task["subtasks"], task_id, description, assigned_to, time_estimate, found)

def search_last_id(tasks,new_id):
    """
    This function used for finding the biggest id in the tasks. Is a sub function for add_task_recursive function
    """
    for task in tasks:
        if "subtasks" in task:
            if task["subtasks"]:
                new_id = search_last_id(task["subtasks"],new_id) + 1
            else:
                new_id = new_id + 1
        else:
            new_id += 1
    return new_id
def assign_task(tasks,task_id, new_member):
    for task in tasks:
        if task.get('id') == task_id:
            task['assigned_to'] = new_member
            print(f"Task {task.get('description')} assigned to {new_member}")
        elif 'subtasks' in task:
            assign_task(task['subtasks'], task_id, new_member)

def complete_task_recursive(tasks, task_id):
    for task in tasks:
        if task.get('id') == task_id:
            task['completed'] = True
            print(f"Task '{task.get('description')}' marked as completed.")
            if 'subtasks' in task:
                for subtask in task['subtasks']:
                    subtask['completed'] = True
        elif 'subtasks' in task:
            complete_task_recursive(task['subtasks'], task_id)

def calculate_time_recursive(task, remain):
    if remain:
        if 'subtasks' in task:
            subtask_sum_remaining = sum(calculate_time_recursive(subtask,remain) for subtask in task.get("subtasks"))
            return subtask_sum_remaining
        else:
            return task.get("time_estimate") if not task.get("completed") else 0
    else:
        if 'subtasks' in task:
            subtask_sum_remaining = sum(calculate_time_recursive(subtask,remain) for subtask in task.get("subtasks"))
            return subtask_sum_remaining
        else:
            return task.get("time_estimate")

def generate_report_recursive(tasks, indent):
    sep = "--"
    for task in tasks:
        remainingHours = calculate_time_recursive(task, True)
        totalHours = calculate_time_recursive(task, False)
        status = 'Completed' if remainingHours == 0 else 'Pending'
        print(f"{indent * sep}{task['id']}.{task['description']} ({task['assigned_to']}) -- Estimated Time to Finish: {remainingHours} out of {totalHours} hours, {status}")
        if 'subtasks' in task:
            generate_report_recursive(task['subtasks'], indent + 1)

def main():
    tasks = init_tasks()
    indent = 0
    found = False
    displayOperations()
    operation = input("Please select an operation: ")
    while operation != "5":
        if operation == "1":
            print("0.New Task")
            displayReport(tasks, indent)
            task_id = int(input("To add a new task, enter 0. To add a subtask, select the task ID: "))
            description = input("Enter the task description: ")
            assigned_to = input("Enter the name of the team member assigned to this task: ")
            time_estimate = int(input("Enter the time estimate for this task: "))
            add_task_recursive(tasks, task_id, description, assigned_to, time_estimate, found)
            print(description+" is added")

        elif operation == "2":
            displayReport(tasks,indent)
            task_id = int(input("Please select a task: "))
            new_member = input("Please enter the new team members name: ")
            assign_task(tasks,task_id,new_member)

        elif operation == "3":
            task_id = int(input("Enter task ID: "))
            complete_task_recursive(tasks,task_id)

        elif operation == "4":
            print("")
            generate_report_recursive(tasks,indent)
            print("\nThe total time of the project is: " +\
                  str(sum(calculate_time_recursive(task, False) for task in tasks)))
            print("The remaining time of the tasks to finish the project is: "+\
                  str(sum(calculate_time_recursive(task, True) for task in tasks)))

        displayOperations()
        operation = input("Please select an operation: ")


if __name__ == "__main__":
    main()