def add_task(todo_list):
    task = input("Enter a task to add: ")
    todo_list.append(task)
    print("Task added!")

def show_tasks(todo_list):
    print("\nYour Tasks:")
    for i, task in enumerate(todo_list):
        print(f"{i+1}. {task}")
    print()

# Main part
tasks = []  # This list is passed by reference

add_task(tasks)
add_task(tasks)
show_tasks(tasks)
