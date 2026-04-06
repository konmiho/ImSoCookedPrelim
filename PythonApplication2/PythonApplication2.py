# 1. Structure Overview
# Create a custom class representing a node [cite: 6]
class Node:
    def __init__(node, value):
        # Rule: Each node must contain exactly three attributes [cite: 6]
        node.center_value = value  # the number stored in this node [cite: 7]
        node.left_node = None      # another node or None [cite: 8]
        node.right_node = None     # another node or None [cite: 9]     
        node.height = 1 

def get_height(thing):
    # Returns 0 if empty, otherwise returns the stored height [cite: 46]
    if thing is None:
        return 0
    return thing.height

def get_balance(thing):
    # Compute balance factor: difference in height between left and right [cite: 37]
    if thing is None:
        return 0
    return get_height(thing.left_node) - get_height(thing.right_node)

# --- Balancing Logic (AVL-Inspired) [cite: 34] ---

def rotate_right(y):
    # A. Single Rotation (Right): Used for straight-line patterns [cite: 41, 42]
    x = y.left_node
    temp = x.right_node

    # Perform rotation
    x.right_node = y
    y.left_node = temp

    # Update heights after the move
    y.height = 1 + max(get_height(y.left_node), get_height(y.right_node))
    x.height = 1 + max(get_height(x.left_node), get_height(x.right_node))

    return x

def rotate_left(x):
    # A. Single Rotation (Left): Used for straight-line patterns [cite: 41, 42]
    y = x.right_node
    temp = y.left_node

    # Perform rotation
    y.left_node = x
    x.right_node = temp

    # Update heights after the move
    x.height = 1 + max(get_height(x.left_node), get_height(x.right_node))
    y.height = 1 + max(get_height(y.left_node), get_height(y.right_node))

    return y

# --- Required Behaviors ---

def insert(item, value):
    if item is None:
        return Node(value)

    if value < item.center_value:
        item.left_node = insert(item.left_node, value) # Recursively insert [cite: 23]
    else:
        item.right_node = insert(item.right_node, value) # Recursively insert [cite: 23]

    # Update height for the current node [cite: 46]
    item.height = 1 + max(get_height(item.left_node), get_height(item.right_node))

    # Determine if the structure is unbalanced [cite: 36, 38]
    balance = get_balance(item)

    # Rebalancing actions for the 4 cases [cite: 40]
    
    # CASE 1: Left-Left (Single Rotation)
    if balance > 1 and value < item.left_node.center_value:
        return rotate_right(item)

    # CASE 2: Right-Right (Single Rotation)
    if balance < -1 and value > item.right_node.center_value:
        return rotate_left(item)

    # CASE 3: Left-Right (Double Rotation: Zig-zag pattern) [cite: 43, 44]
    if balance > 1 and value > item.left_node.center_value:
        item.left_node = rotate_left(item.left_node)
        return rotate_right(item)

    # CASE 4: Right-Left (Double Rotation: Zig-zag pattern) [cite: 43, 44]
    if balance < -1 and value < item.right_node.center_value:
        item.right_node = rotate_right(item.right_node)
        return rotate_left(item)
    return item

def search(item, value):
    # C. Search for a value [cite: 24]
    if item is None:
        return False # False if not found [cite: 26]
    if item.center_value == value:
        return True # True if exists [cite: 26]
    
    if value < item.center_value:
        return search(item.left_node, value)
    return search(item.right_node, value)

def find_min(item):
    # D. Find the lowest value: Traverse left until no more exist [cite: 27, 28]
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
    
    print("--- Self-Balancing Recursive Structure ---")
    print("Enter numeric values to build your tree.")
    print("Type 'done' when you are finished.")

    while True:
        user_input = input("\nEnter a number: ")
        if user_input.lower() == 'done':
            break
        
        try:
            val = int(user_input)
            root = insert(root, val)
            
            # --- Added Logic to show "Holding" status ---
            balance = get_balance(root)
            
            if balance > 0:
                holding = "Left"
            elif balance < 0:
                holding = "Right"
            else:
                holding = "Balanced"
            
            print(f"Inserted {val}. Current Root: {root.center_value}")
            print(f"Status: Holding {holding} (Balance Factor: {balance})")
            # --------------------------------------------

        except ValueError:
            print("Please enter a valid integer.")

    # Demonstration of final statistics
    if root:
        print("\n--- Final Structure Statistics ---")
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