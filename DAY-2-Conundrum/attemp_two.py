from icecream import ic
from functools import reduce
from quetion_input import QUESTION_INPUT_ONE_SAMPLE

def compute_string(input_string:str):
    splitted = input_string.split(":")
    
    game_id = splitted[0]
    game_data = splitted[1].replace(";", ",").split(",")
    ic(game_data)
    return {game_id : game_data}
    
def main():
    input_string = QUESTION_INPUT_ONE_SAMPLE.splitlines()
    computed_data = list(map(compute_string, input_string))
    ic(computed_data)

if __name__ == "__main__":
    main()