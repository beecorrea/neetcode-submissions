class Solution:
    def rob(self, nums: List[int]) -> int:
        # Let's say that these are the houses:
        #   [6, 3, 12, 9, 4]
        # Alternative 1:
        #   We could compute all amounts of money and
        #   choose the best solution.
        #   Two passes + auxiliary array = O(n) / O(n)
        # Alternative 2:
        #   If you pick an even house, you can only pick even houses.
        #   If you pick an odd house, you can only pick odd houses.
        #   Q: Do you have to rob every house?
        # Alternative 3:
        #   Only keep track of house[i-1] and house[i-2].
        #   Optimize by maximizing the value of both variables.
        house1, house2 = 0, 0

        for rob in nums:
            # Try to rob the current house
            candidate = max(house1 + rob, house2)
            house1 = house2
            house2 = candidate

        return house2

