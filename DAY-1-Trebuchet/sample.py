from practice import AdventDayOneTrebuchet, sample_string_two
from question_input import number_map


def test_sample_string_two():
    string_list = ["wothree"] #sample_string_two.splitlines()
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
        for letter in string:
            sub_string = temp + letter
            filtered_list = list(
                filter(lambda val: val.startswith(sub_string), identifier)
            )
            
            if len(filtered_list) > 0:
                temp += letter
                updated_string += temp
            else :
                updated_string += sub_string
                sub_string = ""
                continue
                
            if len(filtered_list) == 1:
                
                if num := number_map.get(temp):
                    updated_string += num 
                    temp = ""
                    continue
                else:
                    sub_string = ""
                    temp = ""   
                    continue
        new_list.append(updated_string)
        updated_string = ""
    return new_list          

print(test_sample_string_two())
