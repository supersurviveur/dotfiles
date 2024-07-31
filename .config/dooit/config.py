from rich.text import Text
from datetime import datetime
from dooit.api import manager

black = "#2e3440"
white = "#e5e9f0"
grey = "#d8dee9"
frost_green = "#8fbcbb"
cyan = "#85dacc"
magenta = "#b48ead"

# primary colors
red = "#ff6188"
orange = "#fc9867"
yellow = "#ffd866"
green = "#a9dc76"
blue = "#78dce8"
purple = "#ab9df2"
# base colors, sorted from darkest to lightest
base0 = "#19181a"
base1 = "#221f22"
base2 = "#2d2a2e"
base3 = "#403e41"
base4 = "#5b595c"
base5 = "#727072"
base6 = "#939293"
base7 = "#c1c0c0"
base8 = "#fcfcfa"


#################################
#             UTILS             #
#################################


def colored(text: str, color: str):
    return f"[{color}]{text}[/]"


def get_status(status):
    return colored(f" {status} ", "r " + blue)


def get_message(message):
    return " " + message


def get_clock() -> Text:
    return Text(f"{datetime.now().time().strftime(' %X ')}", "r " + cyan)


def get_data():
    data = {
        "pending": 0,
        "completed": 0,
        "overdue": 0
    }

    for workspace in manager.get_all_workspaces():
        for todo in workspace.get_all_todos():
            data["completed"] += todo.is_completed()
            data["overdue"] += todo.is_overdue()
            data["pending"] += todo.is_pending()

    return data


data = get_data()

#################################
#           GENERAL             #
#################################

BACKGROUND = black  # background color of the app
BAR_BACKGROUND = black  # background color of bar
WORKSPACES_BACKGROUND = black  # background color for workspaces pane
TODOS_BACKGROUND = black  # background color for todos pane
BORDER_DIM = grey + " 50%"  # color for non-focused pane
BORDER_LIT = cyan  # color for focused pane

# A comma-separated color tuple for foreground and background colors for title of un-focused pane
# It can be a single string as well, it will then use the `BORDER_DIM` as bg color
# BORDER_TITLE_DIM = grey, dark_black

# Same as above for focused pane
BORDER_TITLE_LIT = white, cyan

SEARCH_COLOR = red  # highlight color when searching
YANK_COLOR = blue  # a color flash for yanking a todo/workspace/description
# whether to cancel the todo or save it when esc is pressed. `False` means cancel
SAVE_ON_ESCAPE = False
USE_DATE_FIRST = True  # whether to use dd-mm or mm-dd. True means day first

# This defines how the date is referenced in the Due Column
# See here: https://strftime.org/
DATE_FORMAT = "%d %h"
TIME_FORMAT = "%H:%M"  # use this format for time if time is non zero


#################################
#          DASHBOARD            #
#################################

legend = {"B": blue, "O": orange, "G": green, "M": magenta}
legend = {i + "]": j + "]" for i, j in legend.items()}

regex_style = {
    "U": red,
    "Y": grey,
    "6": blue,
    "a": blue,
    "#": yellow,
    r"(?<=\()[^()\n]+(?=\))": white,
}


def change(s: str):
    for i, j in legend.items():
        s = s.replace(i, j)

    return s


def stylize(art):
    art = "\n".join([change(i) for i in art])
    art = Text.from_markup(art)
    for i, j in regex_style.items():
        art.highlight_regex(i, j)

    return art


art = [
    r"[B]       __I___       [/B][M]                                      [/M]",
    r"[B]   .-''  .  ''-.    [/B][M]                                      [/M]",
    r"[B] .'  / . ' . \  '.  [/B][M]                                      [/M]",
    r"[B]/_.-..-..-..-..-._\ [/B][G] .----------------------------------. [/G]",
    r"[O]         #  _,,_    [/O][G]( Can you complete your tasks today? )[/G]",
    r"[O]         #/`    `\  [/O][G]/'----------------------------------' [/G]",
    r"[O]         / / 6 6\ \ [/O][M]                                      [/M]",
    r"[O]         \/\  Y /\/ [/O][M]       /\_/\                          [/M]",
    r"[O]         #/ `'U` \  [/O][M]      /a a  \               _         [/M]",
    r"[O]       , (  \   | \ [/O][M]     =\ Y  =/-~~~~~~-,_____/ /        [/M]",
    r"[O]       |\|\_/#  \_/ [/O][M]       '^--'          ______/         [/M]",
    r"[O]       \/'.  \  /'\ [/O][M]         \           /                [/M]",
    r"[O]        \    /=\  / [/O][M]         ||  |---'\  \                [/M]",
    r"[O]        /____)/____)[/O][M]        (_(__|   ((__|                [/M]",
]

ART = stylize(art)
NL = " \n"
SEP = colored("─" * 60, "d " + grey)
STATS = [
    colored(f"󱫌 Overdue : {data['overdue']}", red),
    colored(f"󰙏 Pending : {data['pending']}", orange),
    colored(f"󱓞 Done : {data['completed']}", green),
]
DASHBOARD = [ART, NL, SEP, NL, *STATS]


EMPTY_WORKSPACE = [
    "No workspaces yet?",
    f"Press [{cyan}]'a'[/{cyan}] to add some!"
]  # Message to show when there are no workspaces, it's a list of renderable and works just like DASHBOARD

WORKSPACE = {
    "editing": cyan,  # style/color for a focused item when editing
    "pointer": ">",  # A pointer to show the cursor position

    # Text to show if there are children's workspaces
    # You can use some vars for a hint
    # VARS
    # count: number of children inside the workspace
    # You can use this in 2 different ways
    # Example 1: This will indicate that the workspaces have additional child workspaces
    # Example 2: This will indicate the presence of children along with a count
    "children_hint": colored(" +{count}", cyan),

    # Develop Branch: On startup expand all workspaces with child workspaces
    "start_expanded": True,
}

# order of columns for todo pane
COLUMN_ORDER = ["description", "due", "urgency"]
TODO = {
    # this will color the todos based on their status (overdue: red, pending: yellow, done: green)
    "color_todos": False,
    "editing": cyan,  # style/color for focused todo when not editing
    "pointer": ">",  # cursor pointer
    "due_icon": "󰃰 ",  # icon to use for due
    "effort_icon": "󱐋 ",  # icon to use for effort
    "effort_color": yellow,  # color to use for effort
    "recurrence_icon": " ⟲ ",  # icon to use for recurrence
    "recurrence_color": blue,  # color to use for recurrence
    "tags_color": red,  # color for tags
    "completed_icon": "󰄲",  # icon for completed todo
    "pending_icon": "󰡖",  # icon for pending todo
    "overdue_icon": "󰀧",  # icon for overdue todo

    "urgency1_icon": "󰎤",  # icon for urgency 1 (lowest)
    "urgency2_icon": "󰎧",
    "urgency3_icon": "󰎪",
    "urgency4_icon": "󰎭",

    # Develop Branch: Change the color of each urgency
    "urgency1_color": green,
    "urgency2_color": yellow,
    "urgency3_color": orange,
    "urgency4_color": red,

    "initial_urgency": 1,  # Develop Branch: Create new todos with this urgency

    # See workspace children hint for details
    # VARS
    # remaining: Todos remaining
    # done     : Todos done
    # total    : Total todos
    "children_hint": colored(" ({done}/{total})", cyan),
    # "children_hint": "{remaining}",

    "start_expanded": False,  # Develop Branch: On startup expand all todos with child todos
}

EMPTY_TODO = [
    "Wow so Empty !?",
    "Add some todos to get started !",
    # Message to show when there are no todos. The list works just like dashboard's list
]  # Message to show when there are no todos. The list works just like dashboard's list



#################################
#          STATUS BAR           #
#################################
bar = {
    "A": [(get_status, 0.1)],
    "C": [(lambda : colored(f"󱍧 {get_data()['completed']}  ", green), 0.5), (lambda : colored(f"󱍥 {get_data()['pending']}  ", orange), 0.5), (lambda : colored(f"󱍮 {get_data()['overdue']}  ", red), 0.5)],
}
