def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])
    

    return merge(left, right, numbers)

def merge(left, right, merged):
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged[left_idx + right_idx] = left[left_idx]
            left_idx += 1
        else:
            merged[left_idx + right_idx] = right[right_idx]
            right_idx += 1

        for left_idx in range(left_idx, len(left)):
            merged[left_idx + right_idx] = left[left_idx]

        for right_idx in range(right_idx, len(right)):
            merged[left_idx + right_idx] = right[right_idx]

        return merged


arr_numbers = [1,5,2,7,3,8,4,9]
print(merge_sort(arr_numbers)) # saída: 1, 2, 7, 3, 4, 9, 9, 9]

def merge_sort(words):
    if len(words) <= 1:
        return words
    
    mid = len(words) // 2
    left = merge_sort(words[:mid])
    right = merge_sort(words[mid:])
    
    return merge(left, right)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    
    return ''.join(merged)

# Exemplo de uso
word_list = "banana"
sorted_words = merge_sort(word_list)
print(sorted_words) # saída: aaabnn
