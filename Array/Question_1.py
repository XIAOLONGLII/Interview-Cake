"""
Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available. 

Input:
[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

Output:
[(0, 1), (3, 8), (9, 12)]

"""

#Solution
#Sort the meeting(tuple) first element, then comparing current meeting the ending time with next meeting the start time

meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# print(meetings[-1])
meetings.sort()
print(meetings)
merge = [meetings[-1]]
print(merge[-1])
for currStart, currEnd in meetings[1:]:
    lastStart, lastEnd = merge[-1] #(0,1)
    if currStart <= lastEnd:
        merge[-1] = (currStart, max(currEnd, lastEnd))
    else:
        merge.append((currStart, currEnd))
print(merge)
    
