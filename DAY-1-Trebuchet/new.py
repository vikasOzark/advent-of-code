# from practice import AdventDayOneTrebuchet, sample_string_two
from question_input import number_map, identifier


def test_sample_string_two():
    string_list = ["wothree"]  # sample_string_two.splitlines()
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
            else:
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


# print(test_sample_string_two())

def filter_list(character: str):
    return list(
        filter(lambda val: val.startswith(character), identifier)
    )


def solve():

    input_string: list[str] = ["wothree"]  # eightwothree

    for index, character in enumerate(input_string):

        pointer_one = 0
        pointer_two = 1

        index = 0
        final_str = ""
        while len(character) >= index:

            search_str = character[pointer_one: pointer_two]
            filtered_list = filter_list(search_str)

            if len(filtered_list) > 0:
                # this will bw call when there is more than one element is present in the filted list.
                if len(filtered_list) == 1:
                    # this block will call when there is only one element is found in the filtered list.
                    num = number_map.get(search_str)
                    if num:  # this will call when search string will match with any dict key
                        new_car = character.replace(search_str, num)
                        final_str += new_car

                        pointer_one = pointer_two
                        pointer_two = pointer_one + 1
                    else:  # this code will call when search string will not retuem any value
                        final_str += character[pointer_one: pointer_two - 1]
                        # pointer_one = pointer_two
                        pointer_two = pointer_one + 1
                else:
                    final_str += character[pointer_one: pointer_two - 1]
                    pointer_one = pointer_two
                    pointer_two = pointer_one + 1
                continue
            else:
                # this section will call if filtered list is empty
                final_str += search_str
                pointer_one = pointer_two
                pointer_two = pointer_one + 1
                continue
            index += 1


solve()
