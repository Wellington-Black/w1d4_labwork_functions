import pdb

tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# def incomplete_tasks(list):
#     incompleted_tasks = []
#     for task in tasks:
#         if task["completed"] == False:
#             task_not_done = task
#             incompleted_tasks.append(task)
#     return incompleted_tasks
# print(incomplete_tasks(tasks))

# def completed_tasks(list):
#     completed_tasks = []
#     for task in tasks:
#         if task["completed"] == True:
#             task_is_done = task
#             completed_tasks.append(task)
#     return completed_tasks
# print(completed_tasks(tasks))


# def task_description(list):
#     task_description = []
#     for task in tasks:
#         task_description.append(task["description"])
#     return task_description
# print(task_description(tasks))


# def tasks_time_taken(list):
#     time_for_task = []
#     for task in tasks:
#         time_for_task.append(task["description"])
#         time_for_task.append(task["time_taken"])
#     return time_for_task

# print(tasks_time_taken(tasks))

# def task_has_description(list):
    
#     for task in tasks:
#         if task["description"] != None:
#             return task["description"]
#         # else:
#         #     return "not found"

#print(task_has_description(tasks))

def task_has_description(tasks):
    pdb.set_trace()
    description_located = []

    for task in tasks:
        description_located.append(task["description"])
        description_found = None
        if task["description"] != description_found:
            description_is_found = task
        
    return description_is_found

print(task_has_description(tasks))