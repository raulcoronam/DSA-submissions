class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in operations:
            n = len(record)
            if i == "+" and n >= 2: 
                sum_prev_two = record[-1] + record[-2]
                record.append(sum_prev_two)
            elif i == "D" and n >= 1: 
                d_prev_score = record[-1] * 2
                record.append(d_prev_score)
            elif i == "C" and n >= 1: 
                record.pop()
            else: 
                x = int(i)
                record.append(x)
        
        suma = sum(record)

        return suma 

