from practice import sample_string_two
from question_input import number_map, identifier


def solution():
    string_array = sample_string_two.splitlines()
    results = []
    
    for index,string in enumerate(string_array):

        final_string = string
        idx = 1
        while idx <= len(final_string):
            current_string = final_string[idx -1]
            
            filtered_list = filtered_list = list(
                filter(lambda val: val.startswith(current_string), identifier)
            )
            
            if len(filtered_list) > 0:
                
                for item in filtered_list:
                    item_length = len(item)

                    s = final_string[idx - 1]
                    
                    check_string = final_string[ idx - 1 : (idx - 1) + item_length]
                    num_letter = number_map.get(check_string)
                    
                    if num_letter:
                        stripped_string = final_string[((idx - 1) + item_length):]
                        rest_string = final_string[:(idx - 1)]
                        final_string = rest_string + num_letter + stripped_string
                else:
                    pass

            idx += 1

        results.append(final_string)
        
    return results

print(solution())
