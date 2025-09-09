new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 
#Завершили task_005 и перенесли в список завершенных задач
completed_tasks.append(new_tasks.pop())
#Удалили task_007 из активных задач, так как она нуждается в корректирвоке
new_tasks.remove('task_007')
#Повысили приоритет task_015 до первоочередного
new_tasks.insert(0, new_tasks.pop())
#Вывод первоочередной задачи
print(new_tasks[0])