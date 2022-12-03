class Solution:
    def intToRoman(self, num: int) -> str:
        num_dict = {1: "I", 5: "V", 10: "X",
                    50: "L", 100: "C", 500: "D", 1000: "M"}
        asw = ""

        b = 0

        while num > 0:
            cd = num % 10
            if cd == 5:
                asw += num_dict[cd*10**b]
            elif (9 > cd > 5):
                for i in range(cd-5):
                    asw += num_dict[10**b]
                asw += num_dict[5*10**b]
            elif (cd == 9):
                asw += num_dict[10**(b+1)] + num_dict[10**b]
            elif cd == 4:
                asw += num_dict[5*10**b] + num_dict[10**b]
            elif (4 > cd > 0):
                for i in range(cd):
                    asw += num_dict[10**b]
            num = int(num/10)
            b += 1

        return asw[::-1]
