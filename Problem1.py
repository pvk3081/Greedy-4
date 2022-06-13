#Time Complexity: O(M + N) N IS SOURCE AND M IS TARGET
#Space Complexity: O(N)
import bisect
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sl = len(source)
        tl = len(target)
        dic = {}
        sp = 0
        tp = 0
        count = 0
        
        for i in range(len(source)):
            if source[i] not in dic:
                dic[source[i]] = [i]
            else:
                dic[source[i]].append(i)
        pos=0
        count = 1
        i=0
        while i < tl:
            if target[i] not in dic:
                return -1
            li = dic[target[i]]
            index = bisect.bisect_left(li,pos)
            if index < 0:
                index = -index - 1
            if index == len(li):
                pos = 0
                count+=1
            else:
                pos = li[index] + 1
                i+=1
        return count

            