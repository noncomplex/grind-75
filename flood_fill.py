# simply recursively check 4-directionally
# just ensure the bounds checking is correct

class Solution:
    def floodFill(self, image: List[List[int]], sr:int, sc: int, color: int)-> List[List[int]]:
        if image[sr][sc] == color: # otherwise infinite recursion (-1 is a valid index in Python)
            return image
        self.fill(image, sr, sc, image[sr][sc], color)
        return image

    def fill(self, image, r, c, init_color, color):
        if((r < 0)
           or (r >= len(image))
           or (c < 0)
           or (c >= len(image[0]))
           or image[r][c] != init_color
           ):
            return
        if image[r][c] == init_color:
            image[r][c] = color
        self.fill(image, r, c-1, init_color, color)
        self.fill(image, r+1, c, init_color, color)
        self.fill(image, r-1, c, init_color, color)
        self.fill(image, r, c+1, init_color, color)
