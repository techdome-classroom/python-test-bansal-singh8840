class Solution(object):
    def romanToInt(s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'c':100, 'D': 500, 'M': 1000}
        result=0
        prev_value =0

        for char in reversed(s):
            value= roman_dict[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value

      return result
def main():
    test_case =[
           ("III", 3),
           ("LVIII", 58),
           ("MCMXCIV", 1994)
]

for s, expected_output in test_cases:
    output = romanToInt(s)
    if output == expected_output:
        print(f"Input: {s} - Output: {output} -Test Passed")
    else:
        print(f"Input: {s} - Output: {output} -Test Failed")

if __name__ == "__main__":
    main()
