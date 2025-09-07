class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        speople= sorted(people)
        l=0
        r=len(speople)-1
        boat=0
        while l<=r:
            if speople[l]+speople[r]<=limit:
                l+=1
            r-=1
            boat+=1
        return boat