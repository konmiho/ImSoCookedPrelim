
class Node:
    def __init__(node, value):
        node.center_value = value  
        node.left_node = None      
        node.right_node = None       
        node.height = 1 

def get_height(thing):
    if thing is None:
        return 0
    return thing.height

def get_balance(thing):
    if thing is None:
        return 0
    return get_height(thing.left_node) - get_height(thing.right_node)

def rotate_right(y):
    x = y.left_node
    temp = x.right_node

    x.right_node = y
    y.left_node = temp

    y.height = 1 + max(get_height(y.left_node), get_height(y.right_node))
    x.height = 1 + max(get_height(x.left_node), get_height(x.right_node))

    return x

def rotate_left(x):
    y = x.right_node
    temp = y.left_node

    y.left_node = x
    x.right_node = temp

    x.height = 1 + max(get_height(x.left_node), get_height(x.right_node))
    y.height = 1 + max(get_height(y.left_node), get_height(y.right_node))

    return y

def insert(item, value):
    if item is None:
        return Node(value)

    if value < item.center_value:
        item.left_node = insert(item.left_node, value) 
    else:
        item.right_node = insert(item.right_node, value) 

    item.height = 1 + max(get_height(item.left_node), get_height(item.right_node))

    balance = get_balance(item)
    
    if balance > 1 and value < item.left_node.center_value:
        return rotate_right(item)

    if balance < -1 and value > item.right_node.center_value:
        return rotate_left(item)

    if balance > 1 and value > item.left_node.center_value:
        item.left_node = rotate_left(item.left_node)
        return rotate_right(item)

    if balance < -1 and value < item.right_node.center_value:
        item.right_node = rotate_right(item.right_node)
        return rotate_left(item)
    return item

def search(item, value):
    if item is None:
        return False 
    if item.center_value == value:
        return True 
    
    if value < item.center_value:
        return search(item.left_node, value)
    return search(item.right_node, value)

def find_min(item):
    current = item
    while current.left_node is not None:
        current = current.left_node
    return current.center_value

def find_max(item):
    # E. Find the highest value: Traverse right until no more exist [cite: 29, 31]
    current = item
    while current.right_node is not None:
        current = current.right_node
    return current.center_value

if __name__ == "__main__":
    root = None
    
    print("\n---------------------------------------\n")
    print("Enter numeric values to build the tree.")
    print("Type 'done' when you are finished.")

    while True:
        user_input = input("\nEnter a number: ")
        if user_input.lower() == 'done':
            break
        
        try:
            val = int(user_input)
            root = insert(root, val)            
            balance = get_balance(root)
            
            if balance > 0:
                holding = "Left"
            elif balance < 0:
                holding = "Right"
            else:
                holding = "Balanced"
            
            print(f"Inserted {val}. Current Root: {root.center_value}")
            print(f"Status: Holding {holding} (Balance: {balance})")

        except ValueError:
            print("Please enter a valid integer.")

    if root:
        print("\n---------------------------------------")
        print(f"Root center_value: {root.center_value}")
        print(f"Lowest Value found: {find_min(root)}")
        print(f"Highest Value found: {find_max(root)}")
        
        search_target = int(input("\nEnter a number to search for: "))
        if search(root, search_target):
            print(f"Result: {search_target} was found in the structure.")
        else:
            print(f"Result: {search_target} does not exist in the structure.")
    else:
        print("Structure is empty.")