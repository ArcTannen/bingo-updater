# Creates bingo board_list from user input for testing/debugging

import json


if __name__ == '__main__':
    board_list = [
        [[{'text': f'Item {index+1}', 'checked': False} for index in range(int(input(f'Number of items in ({row},{col}): ')))] for col in range(5)] for row in range(5)
    ]

    for r_index, row in enumerate(board_list):
        for c_index, col in enumerate(row):
            num_items = len(col)
            for i in range(num_items):
                item = input(f'({r_index},{c_index}:{i+1}) - ')
                if item:
                    col[i]['text'] = item
                    col[i]['checked'] = True
                else:
                    break

    with open('board_list.json', 'w') as fd:
        json.dump(board_list, fd)
