class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows: return s

        k = i = 0
        j = numRows - 2
        list = [[] for i in range(numRows)]
        answer = ''
        flag = 0

        while i < len(s):
            list[k%(numRows)].append(s[i])
            i+=1
            k+=1
            if k%numRows == 0 and 0 < i: flag = 1
            while 0 < j and flag == 1 and i < len(s):
                list[j].append(s[i])
                j-=1
                i+=1
                if j == 0:
                    k=0
                    flag = 0
                    j = numRows - 2
        for i in range(numRows):
            answer = answer + ''.join(list[i])
        return answer
