class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        times = []
        for p, s in pair: 


            times.append((target - p) / s)
            if len(times) >= 2 and times[-1] <= times[-2]:
                times.pop()
        return len(times)