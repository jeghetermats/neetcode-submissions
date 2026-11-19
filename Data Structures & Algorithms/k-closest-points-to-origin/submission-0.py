import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_distance = {}
        for point in points:
            dist = sqrt(point[0]**2 + point[1]**2)
            point = tuple(point)
            point_distance[point] = dist
        point_distance = sorted(point_distance.items(),key  =lambda x: x[1])
        point_distance = [i[0] for i in point_distance]
        return point_distance[:k]
        return heapq.nsmallest(k,points,key = lambda x: sqrt(x[0]**2+x[1]**2))