"""
K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)


Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Algorithm:
Initialize a max heap
For each point in list
    Get the Euclidean distance squared of the point from origin
    If the heap size is smaller than K
        Push point into max heap with distance squared as key
    Otherwise,
        Push new node into the max heap
        Pop the node with largest distance squared
Return all points (without the distances) within the heap
        
NOTE: Python heapq implementation is a min heap; turn the priority values negative in order to be a max heap

"""


import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        count = 0
        for (x, y) in points:
            dist2 = -(x**2 + y**2)
            if count < K:
                heapq.heappush(heap, (dist2, x,y))
            else:
                heapq.heappushpop(heap, (dist2,x,y))
            count+=1

     
        ret_list = [(x,y) for (dist2, x, y) in heap]
        
        return ret_list
     