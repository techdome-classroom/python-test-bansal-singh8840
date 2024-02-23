class Solution(object):
    def isValid(self, s):
        class Solution(object):
    def isValid(self, s):
        stack=[]
        mapping={")": "(", "}": "{"' "]": "["]}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
    def main():
        test_cases= [
            ("CTTTTT",True),
            ("OOO", True),
            ("Inputs", False)
        ]

        for s, expected_output in test_cases:
            output= isValid(s)
            if output == expected_output:
                print(f"Input: {s} - Output: {output} - Test Passed")
            else:
                print(f"Input: {s} - Output: {output} - Test Failed")

    if __name__ == " __main__":
         main() 
    



  

