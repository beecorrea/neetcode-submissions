class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        
        while l < r:
            w = (l, r)
            h = (heights[l], heights[r])
            area = self.calc_area(w, h)
            res = max(res, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
            

    def calc_area(self, w: (int, int), h: (int, int)) -> int:
        return (w[1] - w[0]) * min(h[0], h[1])