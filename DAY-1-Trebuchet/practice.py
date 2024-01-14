# from . import question_input
from question_input import QUESTION_INPUT, sample_string_two, number_map, identifier


class AdventDayOneTrebuchet:
    "This class is used to solve the advent of code question Day 1: Trebuchet"

    def __init__(self, input_string: str):
        self.input_string: str = input_string
        self.digits: int = 0
        self.combined_numbers = []

    def is_number_contains(self) -> bool:
        """This method is used to check if the input string contains a number"
        :RETURNS
            returns true if any number is contains 
        """
        is_number_contains: list[bool] = [
            char.isnumeric() for char in self.input_string
        ]
        return any(is_number_contains)

    def calculate_result(self) -> int:
        """This method is used to extract the digits from the input string and combined
        digit.
        :RETURNS
            returns the sum of the combined string numbers.
        """

        if not self.is_number_contains():
            return False

        for string in self.input_string:
            number_string: str = [
                num for num in list(string) if num.isnumeric()]
            combined_digit = str(number_string[0]) + str(number_string[-1])
            print(f" {string} -> {combined_digit}")
            self.combined_numbers.append(int(combined_digit))
            self.digits += int(combined_digit)
        return (self.digits, self.combined_numbers)

    def solution_two(self):
        string_array = self.input_string.splitlines()
        results = []

        for index, string in enumerate(string_array):
            final_string = string
            idx = 1
            while idx <= len(final_string):
                current_string = final_string[idx - 1]

                filtered_list = filtered_list = list(
                    filter(lambda val: val.startswith(
                        current_string), identifier)
                )

                if len(filtered_list) > 0:

                    for item in filtered_list:
                        item_length = len(item)

                        check_string = final_string[idx -
                                                    1: (idx - 1) + item_length]
                        num_letter = number_map.get(check_string)

                        if num_letter:
                            stripped_string = final_string[(
                                (idx - 1) + item_length):]
                            rest_string = final_string[:(idx - 1)]
                            final_string = rest_string + num_letter + stripped_string
                idx += 1

            results.append(final_string)
        self.input_string = results
        return results


if __name__ == "__main__":
    solution = AdventDayOneTrebuchet(QUESTION_INPUT)
    solution.solution_two()
    total, li = solution.calculate_result()
    print(li)
