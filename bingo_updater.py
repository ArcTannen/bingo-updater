from PIL import Image, ImageDraw
import sys


GRID_MIN = (192, 256)
GRID_MAX = (843, 907)
BORDER = 6
RADIUS = 24

CELL_COLOR = "LimeGreen"
BORDER_COLOR = "DarkGreen"
FONT_COLOR = "Lime"
FONT = "runescape.ttf"


with Image.open("bingo_board.png") as img:
    board = img.copy()
    draw = ImageDraw.Draw(board)

    x0, y0 = GRID_MIN
    x1, y1 = GRID_MAX
    cell_size = int((x1 - x0 - 6*BORDER) / 5) - 1

    draw.rounded_rectangle([x0+BORDER, y0+BORDER, x0+BORDER+cell_size, y0+BORDER+cell_size], 
                           fill=CELL_COLOR, outline=BORDER_COLOR, width=1, 
                           radius=RADIUS, corners=(1, 0, 0, 0))

    draw.rounded_rectangle([x0+3*BORDER+2*cell_size, y0+3*BORDER+2*cell_size, x0+3*BORDER+3*cell_size, y0+3*BORDER+3*cell_size], 
                           fill=CELL_COLOR, outline=BORDER_COLOR, width=1, 
                           radius=RADIUS, corners=(0, 0, 0, 0))

    update = Image.blend(img, board, 0.5)
    update.save("new_board.png")
