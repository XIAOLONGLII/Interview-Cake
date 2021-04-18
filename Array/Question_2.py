"""
Write a function that takes a list of characters and reverses the letters in place. 
"""
#solution 1
def reverse(list_of_chars):
    for i in range((int)(len(list_of_chars)/2)):
        temp = list_of_chars[i]
        list_of_chars[i] = list_of_chars[len(list_of_chars) - i -1]
        list_of_chars[len(list_of_chars) - i -1] = temp
    print(list_of_chars)
    pass

print(reverse(['E', 'A', 'B', 'D', 'C']))


#solution 2
def reverse(list_of_chars):
    left = 0
    right = len(list_of_chars) - 1
    while left < right:
        list_of_chars[left], list_of_chars[right] = list_of_chars[right], list_of_chars[left]
        left += 1
        right -=1
    print(list_of_chars)
print(reverse(['E', 'A', 'B', 'D', 'C']))
