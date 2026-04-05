class Solution:
    def isValid(self, s: str) -> bool:
        #all posible combinations 
        combinations = {
            "(":")",
            "{":"}",
            "[":"]"
        }

        holder = []
        for c in s:
            if c in combinations:
                holder.append(combinations[c])
            else:
                if not holder or holder[-1] != c:
                    return False 
                holder.pop()
                
        return not holder