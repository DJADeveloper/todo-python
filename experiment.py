waiting_list = ['sen', 'ben', 'jen']
waiting_list.sort()

for i, item in enumerate(waiting_list):
    row = f"{i+1}.{item.title()}"
    print(row)


def create_file(content):
    file = open('./new_file.txt', 'w')
    content_to_add = f'{content} \n '
    file.writelines(content_to_add)
    file.close()

    file = open('./new_file.txt', 'r')
    read_file = file.readlines()
    file.close()
    return read_file


new_content = ['1.' + item + '.txt' for item in waiting_list]


create_file(new_content)
