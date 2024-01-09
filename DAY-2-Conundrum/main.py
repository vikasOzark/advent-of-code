from quetion_input import QUESTION_INPUT_ONE, QUESTION_INPUT_ONE_SAMPLE
from icecream import ic
import time


class GameSolution:
    def __init__(self, game_input: str):
        self.game_input: str = game_input
        self.RED_CUBE: int = 12
        self.GREEN_CUBE: int = 13
        self.BLUE_CUBE: int = 14

    def get_slots_data(self, set_splitted_data: list[str]) -> list[dict[str, int]]:
        """This method is used to compute slot data.

        PARAMETERS:
        ----------
            set_splitted_data : list of string of the game data

        RETURNS:
        -------
            list : returns list of slot data.
        """
        slot_list: list = []
        for set in set_splitted_data: 
            set_splitted_data: list[str] = set.split(",")
            cube_data: dict = {}
            for cube in set_splitted_data:
                splitted_cube: list[str] = cube.split(" ")[1:]
                cube_data[splitted_cube[1]] = int(splitted_cube[0])
            slot_list.append(cube_data)
        return slot_list

    def combine_slot_data(self, slot_data: list[str, int]) -> dict[str, int]:
        combined_data: dict = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for data in slot_data:
            for key, value in data.items():
                if key in combined_data:
                    combined_data[key] += value
                else:
                    combined_data[key] = value
        return combined_data

    def compute_slot_data(self, formatted_data: dict[str, int]) -> dict[str, int]:
        game_id_sum = 0
        temp = []
        for key, value in formatted_data.items():
            verify = [
                value.get("red") <= self.RED_CUBE,
                value.get("green") <= self.GREEN_CUBE,
                value.get("blue") <= self.BLUE_CUBE,
            ]
            if all(verify):
                game_id_sum += int(key.split(" ")[1])
                temp.append(key)
        ic(temp)
        return game_id_sum

    def solution(self):
        formatted_data = {}
        for index, data in enumerate(self.game_input):
            splitted_data = data.split(":")
            game_id = splitted_data[0]

            set_splitted_data = splitted_data[1].split(";")
            data = self.get_slots_data(set_splitted_data)
            formatted_data[game_id] = self.combine_slot_data(data)
        return self.compute_slot_data(formatted_data)


if __name__ == "__main__":
    
    with open("/home/vikas/Desktop/DSA/ADVENT-OF-CODE/DAY-2-Conundrum/game_data.txt", "r") as f:
        QUESTION_INPUT_ONE_NEW = f.readlines()
 
        start_time = time.time()
        
        solution = GameSolution(QUESTION_INPUT_ONE_NEW)
        result = solution.solution()
        
        end_time = time.time()
        
        ic(result)
        ic(f'time taken {end_time - start_time:.2}',)
