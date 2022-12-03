class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        sig = 1
        hassig = False

        for c in s:
            if c.isnumeric():
                res += c
            if len(res) != 0 and not c.isnumeric() and not hassig:
                break
            elif hassig and (c == '-' or c == '+'):
                break

            if c.isalpha():
                break
                
            if c == ".":
                break
                
            if (len(res) != 0 and c == " ") or (len(res) == 0 and hassig and c==" "):
                break

            if len(res) == 0:
                if c == "-":
                    hassig = True
                    sig = -1
                elif c == "+":
                    hassig = True
                    sig = 1

        if res == "":
            return 0        
        elif int(res)*sig > 2**31-1:
            return 2**31-1
        elif int(res)*sig < -2**31:
            return -2**31    

        return int(res)*sig