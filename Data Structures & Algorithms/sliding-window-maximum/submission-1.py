
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_windows = []
        window = [(-nums[i],i) for i in range(k)]
        heapq.heapify(window)

        for i in range(len(nums)-k+1):
            while window[0][1] < i:
                heapq.heappop(window)
            m = -window[0][0]
            max_windows.append(m)
            if i + k < len(nums):

                heapq.heappush(window,(-nums[i+k],i+k))
        return max_windows