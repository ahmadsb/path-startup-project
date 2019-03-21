import cmd
from preprocess import data_preprocess
from view.paths_render import render_paths


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Paths(cmd.Cmd):
    filters = ['Date Filter', 'Region Filter', 'Time Filter', 'Window Filter', 'View Sample']
    intro = f'{color.BOLD}{color.UNDERLINE}Welcome..{color.END}'
    intro += f'{color.BOLD}\nPlease , choose one or more filter number:{color.END}'
    for i, filter in enumerate(filters):
        intro += f'\n{color.BOLD}{i+1}-{color.BLUE}{filter}{color.END}'
    prompt = ""

    # data_preprocess.preprocess()

    def do_1(self, line):
        print(
            f"Please enter {color.BOLD}{color.PURPLE}date{color.END} ,{color.BOLD}{color.PURPLE}start{color.END} and {color.PURPLE}end{color.END} time")
        date = input("date:\n")
        start_time = input("start time:\n")
        end_time = input("end time:\n")
        # do filter Date Filter
        print(f'{color.GREEN}Done{color.END}')

    def do_2(self, line):
        print(f"Please enter {color.BOLD}{color.PURPLE}Regions{color.END}{color.END}:")
        example = f"""
        for example: n x n , n = 3
        3 x 3
        input region 2,4
        |1|{color.CYAN}2{color.END}|3|
        |{color.CYAN}4{color.END}|5|6|
        |7|8|9|
                       """
        print(example)
        regions = input("Regions:\n")
        # do filter time filter
        print(f'{color.GREEN}Done{color.END}')

    def do_3(self, line):
        print(f"Please enter {color.BOLD}{color.PURPLE}start{color.END} and {color.PURPLE}end{color.END} time")
        start_time = input("start time:\n")
        end_time = input("end time:\n")
        # do filter time filter
        print(f'{color.GREEN}Done{color.END}')

    def do_4(self, line):
        print(
            f"Please enter {color.BOLD}{color.PURPLE}Top left{color.END} and {color.PURPLE}Bottom right{color.END} point")
        start_time = input(f"Top Left Point:\n")
        end_time = input("Bottom Right Point:\n")
        # do filter time filter
        print(f'{color.GREEN}Done{color.END}')

    def do_5(self, line):
        render_paths()

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    Paths().cmdloop()
