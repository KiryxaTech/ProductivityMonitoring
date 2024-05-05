from utils.data_utils import read_json

colors = read_json('data\\settings.json')['colors']

light_colors = 0
dark_colors = colors['dark']

DARK_HEADER = dark_colors['header']
DARK_LEFT_MENU = dark_colors['left_menu']
DARK_LEFT_BUTTON = dark_colors['left_button']
DARK_LEFT_BUTTON_ACTIVE = dark_colors['left_button_active']
DARK_BG_PAGE = dark_colors['bg_page']
DARK_FG_PAGE = dark_colors['fg_page']