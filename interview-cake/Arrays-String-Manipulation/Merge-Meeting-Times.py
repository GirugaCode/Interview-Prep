"""
Your company built an in-house calendar tool called HiCal. 
You want to add a feature to see the times in a day when everyone is available.

To do this, you’ll need to know when any team is having a meeting. 
In HiCal, a meeting is stored as a tuple ↴ of integers (start_time, end_time). 
These integers represent the number of 30-minute blocks past 9:00am.

For example:
(2, 3)  # Meeting from 10:00 – 10:30 am
(6, 9)  # Meeting from 12:00 – 1:30 pm

Write a function merge_ranges() that takes a list of multiple 
meeting time ranges and returns a list of condensed ranges.

Input: [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
Output: [(0, 1), (3, 8), (9, 12)]

Here's a formal algorithm:

1) We treat the meeting with earlier start time as "first," and the other as "second."

2) If the end time of the first meeting is equal to or greater than the start time of the second meeting, 
   we merge the two meetings into one time range. The resulting time range's start time is the 
   first meeting's start, and its end time is the later of the two meetings' end times.

3) Else, we leave them separate.
So, we could compare every meeting to every other meeting in this way, merging them or leaving them separate.

"""

def merge_ranges(meetings: list):

    # Sorted list of meetings to ensure each comparison of meetings will be adjacent to eachother
    sorted_meetings = sorted(meetings)

    # Initalizes the result of merged meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    # Iterate through the meetings excluding the first time while 
    # declaring that start and end time of each meeting
    for current_start, current_end in sorted_meetings[1:]:

        # Keep a reference to the last start and end time of the meetings as we iterate
        merged_start, merged_end = merged_meetings[-1]
        
        # If the current and last meetings overlap, use the latest end time
        if current_start <= merged_end:
            merged_meetings[-1] = (merged_start, max(merged_end, current_end))

        # If the current meeting doesn't overlap, add it to the merged lst
        else:
            merged_meetings.append((current_start, current_end))
    
    return merged_meetings

# Runtime: O(n log n)
# O(n log n) worst case for sorting, then O(n) to walk through the list. Could
# solve in O(n) on presorted list.
# Space: O(n), since in the worst case if no meetings overlap, we're recreating
# an identical list to the input list.
    


print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
