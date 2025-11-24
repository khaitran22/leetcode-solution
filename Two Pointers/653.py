def findTarget(root, k):
    def bst_to_sorted_list_iterative(root):
        result = []
        stack = []
        current = root

        while current or stack:
            # Traverse left as far as possible, pushing nodes onto the stack
            while current:
                stack.append(current)
                current = current.left
            
            # Pop a node from the stack (this is the next smallest element)
            current = stack.pop()
            result.append(current.val)
            
            # Move to the right child to continue the in-order traversal
            current = current.right
            
        return result

    result_list = bst_to_sorted_list_iterative(root) if type(root) != list else sorted(root)
    start = 0
    end = len(result_list) - 1
    found = False
    while end > start:
        if result_list[start] != None and result_list[end] != None:
            if result_list[start] + result_list[end] > k:
                end -= 1
            elif result_list[start] + result_list[end] < k:
                start += 1
            else:
                found = True
                break
        elif result_list[start] == None:
            start += 1
        elif result_list[end] == None:
            end += 1
    
    return found
