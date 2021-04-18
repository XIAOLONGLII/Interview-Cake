
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#solution 1
def reverse_words(message):
    s = ""
    for char in message:
        s += char
    arr=s.split()
    return reverse(arr)
def reverse(list):
    left = 0
    right =len(list)-1
    while left < right:
        list[left], list[right] = list[right], list[left]
        left += 1
        right -=1
    return list

message = [ 'c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]
print(reverse_words(message))


#solution 2
def reverse_words(message):
    reverse(message, 0, len(message) - 1)
    currStart = 0
    for i in range(len(message) + 1):
        if (i == len(message) or message[i] == ' '):
          reverse(message, currStart, i - 1) 
          currStart = i + 1
    return message
def reverse(list, left, right):
    while left < right:
        list[left], list[right] = list[right], list[left]
        left += 1
        right -=1


# message = [ 't', 'h', 'i', 'e', 'f', ' ', 'c', 'a', 'k', 'e']
message = list('thief cake')
print(message)
print(reverse_words(message))
