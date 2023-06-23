
nxt_line = '\n'

def close(item):
   return item.close()


def addingTodo():
    while True:
        user_action = input('Type Add, Show, Complete or Edit: ')
        
        match user_action:
            case 'add':
                todo = input('Enter a todo: ') + nxt_line
                
                
                # with-context-manager
                with open('./todos.txt', 'r') as file:
                     todos_list = file.readlines()
              
                
                todos_list.append(todo)
                
                with open('./todos.txt', 'r') as file:
                    todos_list = file.readlines()
                
              
            case 'show':
                
                with open('./todos.txt', 'r') as file:
                    todos_list = file.readlines()
                
                # list comprehension
                # mapping
                new_todos = [item.strip('\n') for item in todos_list] 
  
                
                for index, todo,  in enumerate(new_todos):
                    print(f'{index+1}.{ todo.title()}')
                
                    
            case 'edit':
                number = int(input('Number of the todo to edit: '))
                number =- 1
                new_todo = input('Enter a todo: ')
                todos_list[number] = new_todo
    
            case 'complete':
                number = int(input('Number of the todo to delete: '))
                todos_list.pop(number - 1)
                
            case 'exit':
                break
            case default:
                user_action
                
        
addingTodo()
