import re
import os


def check_if_file(item):

    file_pattern = re.compile('[\\.].+')

    if file_pattern.search(item['name']) is not None:
        return True
    else:
        return False


def parse_document(path):

    with open(path) as mydata:
        data = mydata.read().split("\n")

    items = []

    parent_file = None
    parent_level = 1

    for i, arg in enumerate(data):

        if parent_file is not None:
            if not check_if_file(current_item) and current_item != parent_level:
                parent_file['contents'].append
                continue

        current_level = 1

        for c in arg:
            if c == '\t':
                current_level += 1

        current_item = {}
        current_item['name'] = arg[current_level - 1 :]
        current_item['level'] = current_level
        current_item['children'] = []

        current_item['is_file'] = check_if_file(current_item)

        if current_item['is_file']:
            parent_file = current_item
            parent_level = current_item['level']


        items.append(current_item)

    return items

def create_nested_item_list(current_item, level, Q, sibling_list):

    while len(Q) >= 0:
        print(current_item)

        if current_item is None:
            break

        if current_item['level'] == level:
            sibling_list.append(current_item)
            previous_item = current_item
            try:
                current_item = Q.pop(0)
            except:
                break
        elif current_item['level'] > level:
            current_item = create_nested_item_list(
                current_item, current_item['level'], Q, previous_item['children']
                )
            continue
        elif current_item['level'] < level:
            return current_item


def create_folders(root_path, base_items):

    for i in base_items:
        os.mkdir(f"{root_path}\\{i['name']}")
        if len(i['children']) > 0:
            create_folders(f"{root_path}\\{i['name']}", i['children'])



#################################################

Q = parse_document('folderstruct2.txt')
print(Q)
base_items = []
create_nested_item_list(Q.pop(0), 1, Q, base_items)

for i in base_items:
    print(i)

#create_folders(os.path.abspath(''), base_items)