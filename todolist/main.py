choice=eval(input('''
       press1 Add task
       press2 view task
       press3 complete task
       press4 remove task
       press5 Exit
       '''))

tasks=[]
def add_task():
    if choice==1:
       task_name=input('enter task name:')
       description=input('enter description:')
       priority=input('enter priority (High/Low/Medium)')
       complete=input('Is the task completed? (Yes/No)')

       task={
          'name': task_name,
          'description': description,
          'priority':priority,
          'complete':complete
        }
    tasks.append(task)
    print('task added successfully')

def view_task():
    if len(tasks)==0:
        print('task not available')
    else:
        for task in tasks:
            print('\n task_name:',task['name'])
            print('\n description:',task['description'])
            print('\n priority:',task['priority'])
            print('\n complete:',task['complete'])

def complete_task():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks):
            print(i + 1, task["name"], "-", task["complete"])

        choice = int(input("Enter task number to complete: "))

        if choice >= 1 and choice <= len(tasks):
            tasks[choice - 1]["complete"] = "Yes"
            print("Task completed successfully!")
        else:
            print("Invalid task number")

def remove_task():
    if len(tasks) == 0:
            print("No tasks available")
    else:
        for i, task in enumerate(tasks):
            print(i + 1, task["name"], "-", task["complete"])
    
        choice = int(input("Enter task number to remove: "))
    
        if choice >= 1 and choice <= len(tasks):
            tasks[choice - 1]["complete"] = "Yes"
            print("Task removed successfully!")
        else:
            print("Invalid task number")

add_task()
view_task()
complete_task()
remove_task()