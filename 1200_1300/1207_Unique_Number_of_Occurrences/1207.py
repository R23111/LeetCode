class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cont = list((Counter(arr).values()))
        
        return len(cont) == len(set(cont))
            