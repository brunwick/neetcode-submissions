class Solution:
    def isValid(self, s: str) -> bool:
        l_bracket = []
        for char in s:
            if char in ("(", "{", "["):
                l_bracket.append(char)
            else:
                if len(l_bracket) == 0:
                    return False
                l = l_bracket.pop()
                if (
                    (char == ")" and not l == "(") or
                    (char == "}" and not l == "{") or
                    (char == "]" and not l == "[")
                ):
                    return False
        return True if len(l_bracket) == 0 else False
