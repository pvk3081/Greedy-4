#Time Complexity: O(N)
#Space Complexity: O(N) N IS LENGTH OF TOP
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        dic = {}
        dic2 = {}
        flag = False
        for i in range(len(tops)):
            if tops[i] not in dic:
                dic[tops[i]] = 1
            else:
                dic[tops[i]] +=1
                if dic[tops[i]] >= len(bottoms):
                    element = tops[i]
                    flag = True                    
            if bottoms[i] not in dic:
                dic[bottoms[i]] = 1
            else:
                dic[bottoms[i]] +=1
                if dic[bottoms[i]] >= len(bottoms):
                    element = bottoms[i]
                    flag = True
        if not flag:
            return -1
        aptr = 0
        bptr = 0
        for i in range(len(bottoms)):
            if tops[i] != element and bottoms[i] != element:
                return -1
            elif tops[i] != element:
                aptr +=1
            elif bottoms[i] != element:
                bptr +=1
        return min(aptr,bptr)