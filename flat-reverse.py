
l1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l2 = [[1, 2], [3, 4], [5, 6, 7]]


flat_list = []

def flatten_list(l1):

    for element in l1:

        if type(element) == list:
            flatten_list(element)
        else:
            flat_list.append(element)
    
    return flat_list


def reverse_list(l2):

    reversed_list = l2[::-1]

    return reversed_list


print(flatten_list(l1))
print(reverse_list(l2))

    