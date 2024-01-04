# from . import question_input
from question_input import QUESTION_INPUT, sample_string_two, number_map

class AdventDayOneTrebuchet:
    "This class is used to solve the advent of code question Day 1: Trebuchet"

    def __init__(self, input_string: str):
        self.input_string: str = input_string
        self.digits: int = 0

    def is_number_contains(self) -> bool:
        """This method is used to check if the input string contains a number"
        :RETURNS
            returns true if any number is contains 
        """
        is_number_contains: list[bool] = [
            char.isnumeric() for char in self.input_string
        ]
        return any(is_number_contains)

    def calculate_result(self, input_string: list[str] = None) -> int:
        """This method is used to extract the digits from the input string and combined
        digit.
        :RETURNS
            returns the sum of the combined string numbers.
        """
        
        if not self.is_number_contains():
            return False

        # print(f"Input string: {self.input_string}")
        new_string = input_string or self.input_string.splitlines()

        splitted_string: list[str] = new_string
        for string in splitted_string:
            number_string: str = [num for num in list(string) if num.isnumeric()]
            combined_digit = str(number_string[0]) + str(number_string[-1])
            print(f" {string} -> {combined_digit}") , 
            self.digits += int(combined_digit)
            
        return self.digits

    def convert_letter(self) -> list[str]:
        string_list = self.input_string.splitlines()
        new_list = []

        identifier: list = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]
        
        updated_string = ""
        for string in string_list:
            temp = ""
            for letter in string:  # -> letter : e
                sub_string = temp + letter
                filtered_list = list(
                    filter(lambda val: val.startswith(sub_string), identifier)
                )
                if len(filtered_list) > 0:
                    temp = temp + letter
                else :
                    updated_string += letter
                    continue
                    
                if len(filtered_list) == 1:
                    
                    if num := number_map.get(temp):
                        updated_string += num 
                        temp = ""
                        continue
                    else:
                        continue
            new_list.append(updated_string)
            updated_string = ""
        return new_list   
    
if __name__ == "__main__" :
    # 29, 83, 13, 24, 42, 14, and 76
    solution = AdventDayOneTrebuchet(sample_string_two)
    li_string = solution.convert_letter()
    print(li_string)
    print(solution.calculate_result(li_string))
