
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
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
