# from . import question_input
from question_input import QUESTION_INPUT

class AdventDayOneTrebuchet:
    "This class is used to solve the advent of code question Day 1: Trebuchet"

    def __init__(self, input_string: str):
        self.input_string: str = input_string

    def is_number_contains(self) -> bool:
        """This method is used to check if the input string contains a number"
        :RETURNS
            returns true if any number is contains 
        """
        is_number_contains: list[bool] = [
            char.isnumeric() for char in self.input_string
        ]
        return any(is_number_contains)

    def __call__(self) -> int:
        """This method is used to extract the digits from the input string and combined
        digit.
        :RETURNS
            returns the sum of the combined string numbers.
        """
        digits: int = 0
        
        if not self.is_number_contains():
            return False

        splitted_string: list[str] = self.input_string.splitlines()
        for string in splitted_string:
            number_string: str = [num for num in list(string) if num.isnumeric()]
            combined_digit = str(number_string[0]) + str(number_string[-1])
            digits += int(combined_digit)
            
        return digits
    
    
    

if __name__ == "__main__" :
    solution = AdventDayOneTrebuchet(QUESTION_INPUT)
    print(solution())