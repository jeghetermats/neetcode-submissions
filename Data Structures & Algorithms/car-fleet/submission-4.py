class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position,speed),reverse=True)
        slowest = 0
        fleets =0
        for pos, speed in pos_speed:

            time = (target-pos)/speed
            if time>slowest:
                slowest=time
                fleets+=1

        return fleets