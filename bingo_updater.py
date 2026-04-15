from PIL import Image, ImageDraw, ImageFont


X_MIN, Y_MIN = 601, 41
X_MAX, Y_MAX = 1237, 677
BORDER = 6
RADIUS = 24
CELL_SIZE = int((X_MAX - X_MIN - 6*BORDER) / 5)

CELL_COLOR = (50, 205, 50, 255)  # 'LimeGreen'
BORDER_COLOR = (0, 100, 0, 255)  # 'DarkGreen'
FONT_COLOR = (255, 255, 0, 255)  # 'Yellow'
SHADOW_COLOR = (0, 0, 0, 255)    # 'Black'
FONT = ImageFont.truetype('fonts/runescape.ttf', 16)


def update_board(board_list, board_image='bingo_board.png'):
    with Image.open(board_image) as board:
        overlay = board.copy()
        text_layer = Image.new('RGBA', board.size, (0, 0, 0, 0))

        checked_items = get_checked(board_list)

        for row in range(5):
            for col in range(5):
                complete = len(checked_items[row][col]) == len(board_list[row][col])
                if checked_items[row][col]:
                    update_tile(overlay, text_layer, row, col, to_str(checked_items[row][col]), complete)

        board = Image.blend(board, overlay, 0.5)
        board.paste(text_layer, mask=text_layer)
        board.save('new_board.png')


def update_tile(overlay, text_layer, row, col, list_text, complete):
    draw_square(overlay, row, col, complete)
    draw_text(text_layer, row, col, list_text)


def draw_text(board, row, col, list_text):
    draw = ImageDraw.Draw(board)
    padding = 6

    x0, y0, *_ = get_coords(row, col)
    x0 += padding
    y0 += padding

    # TODO: Handle wrapping & columns for text overflow.
    draw.multiline_text((x0+1, y0+1), list_text, SHADOW_COLOR, FONT)
    draw.multiline_text((x0, y0), list_text, FONT_COLOR, FONT)


def draw_square(board, row, col, complete):
    draw = ImageDraw.Draw(board)

    corners = ((row, col) == (0, 0), (row, col) == (0, 4), 
               (row, col) == (4, 4), (row, col) == (4, 0))
    
    draw.rounded_rectangle(get_coords(row, col), 
                           fill=CELL_COLOR if complete else BORDER_COLOR, 
                           outline=BORDER_COLOR, width=1, 
                           radius=RADIUS, corners=corners)


def get_checked(board_list):
    return [
        [[item['text'] for item in col if item['checked']] for col in row] for row in board_list
    ]


def to_str(checklist):
    return '\n'.join(f'- {item}' for item in checklist)


def get_coords(row, col):
    x0 = X_MIN + (col+1)*BORDER + col*CELL_SIZE
    y0 = Y_MIN + (row+1)*BORDER + row*CELL_SIZE
    x1 = X_MIN + (col+1)*BORDER + (col+1)*CELL_SIZE
    y1 = Y_MIN + (row+1)*BORDER + (row+1)*CELL_SIZE

    return [x0, y0, x1, y1]


if __name__ == '__main__':
    import json

    with open('board_list.json') as fd:
        board_list = json.load(fd)
        update_board(board_list)
