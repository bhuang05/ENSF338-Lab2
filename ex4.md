**_Question 4:_**

1. You could use interpolation search to find an estimated value of where you room might be.

2. We would first have to calculate the approximate position of the key:
   pos = (key - arr[lo]) \* (hi - lo) / (arr[hi] - arr[lo])

   **Where:**
   key = 128
   lo = 0
   hi = len(arr) - 1 = 19
   arr = [100, 102, 104, 106, 108, ..., 130, 132, 134, 136, 138]

   **Thus:**
   pos = (128 - 100) _ (19 - 0) / (138 - 100)
   pos = (28) _ 19 / (38)
   pos = 14

   **And:**
   arr[pos] = 128

Realistically, you cannot "teleport" to the room so a "step" is not a physical step but rather the thought of where the room could possibly be located, and then walking there and comparing the _"room you are looking for"_ and the _"room you are at"_ which in code would be indicated by a conditional statement such as:

    if (arr[pos] = key)
        return pos

3. This is a best case scenario. The reason why this is a best case scenario is because the value of the
   key (128) was found at the first comparison between **_arr[pos]_** and **_key_**

4. If someone was given the floor layout, the best case would be if the "key" is either the room on the left (100) or the room on the right (138). In technical terms, the arr[hi] or arr[lo].

The worst case scenario would be that the room you are looking for is right in the middle, namely room 118. No matter what, the person would have to walk the maximum distance to get to this room.

5. This implementation of interpolation search is iterative, not recursive. Thus, memoization could not be used.
   However, we could also add the distances between each room as a seperate array. For example, although the midpoint is either room 118/120, room 120 is closer if you were to turn right instead of left. Thus, by memorizing the floor layout, you could probably implement a better way to calculate **_pos_**.
