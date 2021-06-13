import os
import subprocess
#from typing import List  # noqa: F401
from libqtile import bar, layout, widget, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# //////////////////////////////////////////////////////////////////////// VARIABLE DECLARATIONS //////////////////////////////////////////////////////////////////////// #

# ============== COLOR ============== #
COLOR_BACKGROUND            = "#2e3440"

COLOR_FOREGROUND            = "#eceff4"
COLOR_FOREGROUND_YELLOW     = "#5f4510"
COLOR_FOREGROUND_GREEN      = "#303f23"
COLOR_FOREGROUND_BLUE       = "#1b2634"
COLOR_FOREGROUND_PURPLE     = "#3a2636"
COLOR_FOREGROUND_LIGHT_BLUE = "#1f3040"
COLOR_FOREGROUND_AQUA       = "#253e3d"                   
COLOR_FOREGROUND_CYAN       = "#1d4049"

COLOR_RED                   = "#bf616a"
COLOR_ORANGE                = "#d08770"
COLOR_YELLOW                = "#ebcb8b"
COLOR_GREEN                 = "#a3be8c"
COLOR_BLUE                  = "#5e81ac"
COLOR_PURPLE                = "#b48ead"
COLOR_LIGHT_BLUE            = "#81a1c1"
COLOR_CYAN                  = "#88c0d0"
COLOR_AQUA                  = "#84b5b4"
COLOR_WHITE                 = "#ffffff"
COLOR_LIGHT_GREY            = "#677490"
COLOR_GREY                  = "#434c5e"
COLOR_DARK_GREY             = "#2e3440"
COLOR_BLACK                 = "#000000"

COLOR_ACTIVE_GROUP_BOX      = "#8fbcbb" 
COLOR_INACTIVE_GROUP_BOX    = "#4c566a" 
COLOR_HIGHLIGHT_GROUP_BOX   = "#3b4252"

BACKGROUND_COLOR_PROMPT_WIDGET = COLOR_DARK_GREY
FOREGROUND_COLOR_PROMPT_WIDGET = COLOR_FOREGROUND

# === CHARACTERS === #
ARROW_GLYPH_TEXT = ""
SPACE            = " "
EMPTY            = ""

# === DEFAULT APPLICATIONS === #
VOLUME_APP         = "pavucontrol"
TERMINAL_APP       = "alacritty"
WEB_BROWSER_APP    = "firefox"
PYTHON_INTERPRETER = "python"
FILE_MANAGER_APP   = "nemo"
CODE_EDITOR_APP    = "code"
HTOP_APP           = "htop"

# =================================== SCRIPTS =================================== #
SCRIPT_SHUTDOWN_HANDLER          = "/home/santiago/.scripts/shutdown-handler.sh -s"

SCRIPT_QUERY_UPDATES_PACMAN      = "pacman -Qu"
SCRIPT_QUERY_UPDATES_TAUR        = "/home/santiago/.scripts/taur.sh -Qu"

SCRIPT_INSTALL_UPDATES_PACMAN    = "doas pacman --noconfirm -Syu"
SCRIPT_INSTALL_UPDATES_TAUR      = "doas /home/santiago/.scripts/taur.sh -Syu"

TERMINAL_TITLE_INSTALLING_PACMAN = "Installing Pacman Updates"
TERMINAL_TITLE_INSTALLING_TAUR   = "Installing AUR Updates"

TERMINAL_TITLE_PACMAN            = "Available Pacman Updates"
TERMINAL_TITLE_TAUR              = "Available AUR Updates"


# ================================== GROUPS ================================== #
GROUP_NAMES = [ "MAIN", "SYS", "DEV", "WWW", "GFX", "6", "7", "8", "DOCS", "TV" ]
GROUP_DEFAULTS = { "layout": "monadtall" }

# ================= KEYS ================= #
KEY_XF86_AUDIO_LOWER = "XF86AudioLowerVolume"
KEY_XF86_AUDIO_RAISE = "XF86AudioRaiseVolume"
KEY_XF86_AUDIO_MUTE  = "XF86AudioMute"

KEY_CTRL   = "control"
KEY_RETURN = "Return"
KEY_SPACE  = "space"
KEY_SHIFT  = "shift"
KEY_MOD    = "mod4"
KEY_TAB    = "Tab"

KEY_H = "h"
KEY_J = "j"
KEY_K = "k"
KEY_L = "l"
KEY_N = "n"
KEY_F = "f"
KEY_B = "b"
KEY_V = "v"
KEY_C = "c"
KEY_Q = "q"
KEY_R = "r"
KEY_T = "t"

# == MOUSE BUTTONS == #
LEFT_CLICK   = "Button1"
MIDDLE_CLICK = "Button2"
RIGHT_CLICK  = "Button3"

# ============================ COMMANDS ============================ #
COMMAND_NOTIFY_NO_CALLBACK         = "dunstify -i /home/santiago/.config/dunst/icons/alert.png -u low -t 2500 -a 'Qtile Bar' 'No Callback' 'this widget has no callback' &"
COMMAND_UPDATE_PAC_CHECK           = "/home/santiago/.scripts/pacman-updates.sh -Lu"
COMMAND_UPDATE_AUR_CHECK           = "/home/santiago/.scripts/taur.sh -Syqu"
COMMAND_VOLUME_LOWER               = "amixer sset 'Master' 2%+ unmute"
COMMAND_VOLUME_RAISE               = "amixer sset 'Master' 2%+ unmute"
COMMAND_OPEN_ROOT_DIRECTORY        = "{} /".format(FILE_MANAGER_APP)
COMMAND_VOLUME_MUTE                = "amixer -q set Master toggle"
COMMAND_LAUNCH_IN_TERMINAL_FORMAT  = "{} --title '{}' {} -e {}"
COMMAND_LAUNCH_OPEN_WEATHER_FORMAT = "{} --new-window {}{}"

# ======================= PATHS ======================= #
PATH_LOGO_PYTHON      = "~/.config/qtile/icons/python.svg"
PATH_BAR_ICONS_FORMAT = "~/.config/qtile/icons/bar/{}.svg"

# ==================== TERMINAL FLAGS ==================== #
TERMINAL_FLAG_HOLD_OPEN = "--hold"

# ====== DEVICE VARIABLES ====== #
WIFI_NETWORK_INTERFACE = "wlp34s0"
LAN_NETWORK_INTERFACE  = "eno1"
LINUX_DISTRIBUTION     = "Arch"

# ====== WEATHER VARIABLES ====== #
OPEN_WEATHER_URL    = "https://openweathermap.org/city/"
MEDELLIN_CITY_CODE  = "3674962"


# ===== KEYBOARD LAYOUT ===== #
KEYBOARD_LAYOUT_LATAM = "LATAM"
KEYBOARD_LAYOUT_US    = "US"

CONFIGURED_KEYBOARDS = [KEYBOARD_LAYOUT_LATAM, KEYBOARD_LAYOUT_US]

# == WIDGET ICON NAMES == #
ICON_NAME_CPU        = "cpu"
ICON_NAME_TEMP       = "temp"
ICON_NAME_DISK       = "disk"
ICON_NAME_MEMORY     = "memory"
ICON_NAME_WEATHER    = "weather"
ICON_NAME_NET_DOWN   = "net_down"
ICON_NAME_NET_UP     = "net_up"
ICON_NAME_UPDATE_PAC = "update_pac"
ICON_NAME_UPDATE_AUR = "update_aur"
ICON_NAME_VOLUME     = "volume"
ICON_NAME_WINDOWS    = "windows"
ICON_NAME_CLOCK      = "clock"
ICON_NAME_KEYBOARD   = "keyboard"
ICON_NAME_POWER      = "power"

# ============ WIDGET FONT FAMILIES ============ #
FONT_FAMILY_WIDGET_PROMPT      = "Roboto Mono Bold"
FONT_FAMILY_WIDGET_WINDOW_NAME = "Roboto Mono Bold"
FONT_FAMILY_WIDGET_DEFAULT     = "Roboto Mono Bold"
FONT_FAMILY_WIDGET_BOX         = "Roboto Bold"
FONT_FAMILY_WIDGET_GROUP_BOX   = "Ubuntu Bold"

# ======== RUN PROMPT ======== #
PROMPT_WIDGET_PROMPT = "spawn: "

# ====== GROUP BOX STYLING ====== #
TEXT_OPEN_WIDGET_BOX        = " [...]    "
TEXT_CLOSE_WIDGET_BOX       = " [ X ]    "
TEXT_WIDGET_BOX_REPLACEMENT = EMPTY

HIGHLIGHT_METHOD_GROUP_BOX  = "line"

BUTTON_LOCATION_WIDGET_BOX = "right"

# ===== WIDGET FMTS ===== #
BOX_FMT           = "[ {} ]"
NO_FMT_WITH_SPACE = "{} "
NO_FMT            = "{}"

FMT_WIDGET_CPU        = NO_FMT
FMT_WIDGET_TEMP       = NO_FMT_WITH_SPACE
FMT_WIDGET_DISK       = NO_FMT
FMT_WIDGET_MEMORY     = NO_FMT
FMT_WIDGET_WEATHER    = NO_FMT
FMT_WIDGET_NET_DOWN   = NO_FMT
FMT_WIDGET_NET_UP     = NO_FMT
FMT_WIDGET_UPDATE_PAC = NO_FMT
FMT_WIDGET_UPDATE_AUR = NO_FMT
FMT_WIDGET_VOLUME     = NO_FMT_WITH_SPACE
FMT_WIDGET_WINDOWS    = NO_FMT_WITH_SPACE
FMT_WIDGET_CLOCK      = NO_FMT
FMT_WIDGET_KEYBOARD   = NO_FMT_WITH_SPACE

# ============ WIDGET FORMATS ============ #
FORMAT_WIDGET_CPU        = "{load_percent}%"
FORMAT_WIDGET_DISK       = "{r:.1f}%"
FORMAT_WIDGET_MEMORY     = "{MemPercent:.1f}%"
FORMAT_WIDGET_WEATHER    = "{main_temp:.1f}°{units_temperature}"
FORMAT_WIDGET_NET_DOWN   = "{down}"
FORMAT_WIDGET_NET_UP     = "{up} "
FORMAT_WIDGET_UPDATE_PAC = "{updates}"
FORMAT_WIDGET_UPDATE_AUR = "{updates}"
FORMAT_WIDGET_CLOCK      = "%I:%M %p"

FORMAT_WIDGET_BOX_01_CPU        = "running @ {freq_current}GHz"
FORMAT_WIDGET_BOX_01_DISK       = "measuring {p}"
FORMAT_WIDGET_BOX_02_DISK       = "{s}{m}B Total"
FORMAT_WIDGET_BOX_03_DISK       = "{uf}{m}B remaining"
FORMAT_WIDGET_BOX_01_MEMORY     = "{MemTotal}MiB in total"
FORMAT_WIDGET_BOX_02_MEMORY     = "{MemUsed}MiB being used"
FORMAT_WIDGET_BOX_03_MEMORY     = "{Shmem}MiB of shared"
FORMAT_WIDGET_BOX_04_MEMORY     = "{SwapTotal}MiB of swap"
FORMAT_WIDGET_BOX_01_WEATHER    = "{weather_details}"
FORMAT_WIDGET_BOX_02_WEATHER    = "{humidity}% humidity"
FORMAT_WIDGET_BOX_03_WEATHER    = "{wind_speed}{units_wind_speed} winds"
FORMAT_WIDGET_BOX_01_UPDATE_PAC = "See"
FORMAT_WIDGET_BOX_02_UPDATE_PAC = "Install"
FORMAT_WIDGET_BOX_01_UPDATE_AUR = "See"
FORMAT_WIDGET_BOX_02_UPDATE_AUR = "Install"
FORMAT_WIDGET_BOX_01_CLOCK      = "%a, %d %b"

# ======== DEFAULT STRINGS ======== #
DEFAULT_STRING_WIDGET_UPDATE_PAC = EMPTY
DEFAULT_STRING_WIDGET_UPDATE_AUR = EMPTY

# ============ WIDGET FONT SIZES ============ #
FONT_SIZE_WIDGET_PROMPT      = 14
FONT_SIZE_WIDGET_WINDOW_NAME = 12
FONT_SIZE_WIDGET_DEFAULT     = 12
FONT_SIZE_WIDGET_BOX         = 10
FONT_SIZE_WIDGET_GROUP_BOX   = 10
FONT_SIZE_ARROW_SPACER       = 72

# = WIDGET PADDING SIZES = #
PADDING_SEPARATOR      = 6
PADDING_WIDGET_PROMPT  = 10
PADDING_WIDGET_DEFAULT = 3
PADDING_GROUP_BOX      = 3
PADDING_WIDGET_SYSTRAY = 5
PADDING_ARROW_SPACER   = -14

# ======= ICON SIZE ======= #
ICON_SIZE_WIDGET_SYSTRAY = 15

# === MARGIN SIZES === #
MARGIN_LAYOUT_THEME = 12
MARGIN_ICON_DEFAULT = 2
MARGIN_PYTHON_LOGO  = 0

MARGIN_X_GROUP_BOX  = 0
MARGIN_Y_GROUP_BOX  = 4

# ===== BORDER SIZES ===== #
BORDER_WIDTH_LAYOUT_THEME = 2
BORDER_WIDTH_GROUP_BOX    = 2

# ====== SEPARATOR ====== #
SIZE_PERCENT_SEPARATOR = 75
LINE_WIDTH_SEPARATOR   = 2

# ========= BOOLS ========= #
SCALE_ICON_DEFAULT     = True
DISABLE_DRAG_GROUP_BOX = True

# ========= THRESHOLD ========= #
THRESHOLD_WIDGET_TEMP = 65
THRESHOLD_WIDGET_DISK = 200

# ========= UPDATE INTERVALS ========= #
UPDATE_INTERVAL_WIDGET_DEFAULT      = 1.0

UPDATE_INTERVAL_WIDGET_CPU          = UPDATE_INTERVAL_WIDGET_DEFAULT
UPDATE_INTERVAL_WIDGET_TEMP         = UPDATE_INTERVAL_WIDGET_DEFAULT
UPDATE_INTERVAL_WIDGET_DISK         = UPDATE_INTERVAL_WIDGET_DEFAULT
UPDATE_INTERVAL_WIDGET_MEMORY       = UPDATE_INTERVAL_WIDGET_DEFAULT
UPDATE_INTERVAL_WIDGET_WEATHER      = 600.0
UPDATE_INTERVAL_WIDGET_NET          = UPDATE_INTERVAL_WIDGET_DEFAULT
UPDATE_INTERVAL_WIDGET_UPDATE_PAC   = 1800.0
UPDATE_INTERVAL_WIDGET_UPDATE_AUR   = 1800.0
UPDATE_INTERVAL_WIDGET_VOLUME       = UPDATE_INTERVAL_WIDGET_DEFAULT
UPDATE_INTERVAL_WIDGET_CLOCK        = UPDATE_INTERVAL_WIDGET_DEFAULT
UPDATE_INTERVAL_WIDGET_KEYBOARD     = 10.0

# ================= WIDGET COLORS ================= #
BACKGROUND_COLOR_WIDGET_WINDOW_NAME = COLOR_BACKGROUND
BACKGROUND_COLOR_WIDGET_CPU         = COLOR_RED
BACKGROUND_COLOR_WIDGET_TEMP        = COLOR_ORANGE
BACKGROUND_COLOR_WIDGET_DISK        = COLOR_YELLOW
BACKGROUND_COLOR_WIDGET_MEMORY      = COLOR_GREEN
BACKGROUND_COLOR_WIDGET_WEATHER     = COLOR_BLUE
BACKGROUND_COLOR_WIDGET_NET         = COLOR_PURPLE
BACKGROUND_COLOR_WIDGET_UPDATE_PAC  = COLOR_LIGHT_BLUE
BACKGROUND_COLOR_WIDGET_UPDATE_AUR  = COLOR_CYAN
BACKGROUND_COLOR_WIDGET_VOLUME      = COLOR_AQUA
BACKGROUND_COLOR_WIDGET_WINDOWS     = COLOR_LIGHT_GREY
BACKGROUND_COLOR_WIDGET_CLOCK       = COLOR_GREY
BACKGROUND_COLOR_WIDGET_KEYBOARD    = COLOR_DARK_GREY
BACKGROUND_COLOR_WIDGET_POWER       = COLOR_BLACK

FOREGROUND_COLOR_WIDGET_DISK        = COLOR_FOREGROUND_YELLOW
FOREGROUND_COLOR_WIDGET_MEMORY      = COLOR_FOREGROUND_GREEN
FOREGROUND_COLOR_WIDGET_WEATHER     = COLOR_FOREGROUND_BLUE
FOREGROUND_COLOR_WIDGET_NET         = COLOR_FOREGROUND_PURPLE
FOREGROUND_COLOR_WIDGET_UPDATE_PAC  = COLOR_FOREGROUND_LIGHT_BLUE
FOREGROUND_COLOR_WIDGET_UPDATE_AUR  = COLOR_FOREGROUND_CYAN
FOREGROUND_COLOR_WIDGET_VOLUME      = COLOR_FOREGROUND_AQUA

ALERT_COLOR_TEMP = COLOR_WHITE
ALERT_COLOR_DISK = COLOR_WHITE

# ///////////////////////////////////////////////////////////////////////// FUNCTION DECLARATION ///////////////////////////////////////////////////////////////////////// #

class BarWidget:
    def __init__(self, widget_object, widget_box = None, callback = None, icon_name = None, background = None, foreground = None, use_arrow = False):
        self.widget_object = widget_object
        self.widget_box    = widget_box
        self.callback      = callback
        self.icon_name     = icon_name
        self.use_arrow     = use_arrow
        self.background    = background
        self.foreground    = foreground

def spawn(command):
    return  lambda: qtile.cmd_spawn(command)

def launchTerminalCommand(command, title = None, hold_open = False):
    title = title if title is not None else TERMINAL_APP
    hold_open = TERMINAL_FLAG_HOLD_OPEN if hold_open else EMPTY

    modified_command = COMMAND_LAUNCH_IN_TERMINAL_FORMAT.format(TERMINAL_APP, title, hold_open, command)

    return spawn(modified_command)

def getSeparator(line_width, background_color = COLOR_BACKGROUND, foreground_color = COLOR_GREY):
    return widget.Sep( linewidth    = line_width
                     , padding      = PADDING_SEPARATOR + line_width
                     , size_percent = SIZE_PERCENT_SEPARATOR
                     , background   = background_color
                     , foreground   = foreground_color )

def getBoxWidgets(widget_list, background_color, foreground_color):
    return widget.WidgetBox( font                  = FONT_FAMILY_WIDGET_BOX
                           , fontsize              = FONT_SIZE_WIDGET_BOX
                           , background            = background_color
                           , foreground            = foreground_color
                           , text_closed           = TEXT_OPEN_WIDGET_BOX
                           , text_open             = TEXT_CLOSE_WIDGET_BOX
                           , close_button_location = BUTTON_LOCATION_WIDGET_BOX
                           , widgets               = widget_list )

def getWidgetIcon(icon, background_color, callback_function):
    return widget.Image( filename        = PATH_BAR_ICONS_FORMAT.format(icon)
                       , margin          = MARGIN_ICON_DEFAULT
                       , scale           = SCALE_ICON_DEFAULT
                       , mouse_callbacks = setMouseCallbacks(callback_function)
                       , background      = background_color )

def getArrowSpacer(color, previous_color):
    return widget.TextBox( text       = ARROW_GLYPH_TEXT
                         , fontsize   = FONT_SIZE_ARROW_SPACER 
                         , padding    = PADDING_ARROW_SPACER
                         , background = previous_color
                         , foreground = color )

# A replacement for widgets that don't have a widget box
def getBoxReplacement(background_color):
    return widget.TextBox( fmt        = NO_FMT
                         , text       = TEXT_WIDGET_BOX_REPLACEMENT
                         , background = background_color
                         , foreground = COLOR_FOREGROUND )

def getBar(widget_instances_list):
    bar_widgets_array = []
    previous_color = COLOR_BACKGROUND

    for widget in widget_instances_list:
        widget.background = widget.background if widget.background is not None else COLOR_BACKGROUND
        widget.foreground = widget.foreground if widget.foreground is not None else COLOR_FOREGROUND

        if widget.use_arrow: 
            bar_widgets_array.append( getArrowSpacer(widget.background, previous_color) )

        if widget.icon_name is not None: 
            bar_widgets_array.append( getWidgetIcon(widget.icon_name, widget.background, widget.callback) )

        bar_widgets_array.append(widget.widget_object)

        if widget.widget_box is not None: 
            bar_widgets_array.append( getBoxWidgets(widget.widget_box, widget.background, widget.foreground) )
        
        else:
            bar_widgets_array.append( getBoxReplacement(widget.background) )

        previous_color = widget.background

    return bar_widgets_array

def setMouseCallbacks(left_click_function=None, middle_click_function=None, right_click_function=None):
    return { LEFT_CLICK:   left_click_function
           , MIDDLE_CLICK: middle_click_function
           , RIGHT_CLICK:  right_click_function }

# ///////////////////////////////////////////////////////////////////////////// KEY BINDINGS ///////////////////////////////////////////////////////////////////////////// #

#        [ Mod ]                    [ Key ]               [ Action ]
keys = [ Key( [KEY_MOD],            KEY_H,                lazy.layout.up() )
       , Key( [KEY_MOD],            KEY_L,                lazy.layout.down() )
       , Key( [KEY_MOD],            KEY_J,                lazy.layout.left() )
       , Key( [KEY_MOD],            KEY_K,                lazy.layout.right() )
       , Key( [KEY_MOD],            KEY_SPACE,            lazy.layout.next() )
                       
       , Key( [KEY_MOD, KEY_SHIFT], KEY_H,                lazy.layout.shuffle_up() )
       , Key( [KEY_MOD, KEY_SHIFT], KEY_L,                lazy.layout.shuffle_down() )
       , Key( [KEY_MOD, KEY_SHIFT], KEY_J,                lazy.layout.shuffle_left() )
       , Key( [KEY_MOD, KEY_SHIFT], KEY_K,                lazy.layout.shuffle_right() )
                       
       , Key( [KEY_MOD, KEY_CTRL],  KEY_J,                lazy.layout.grow_left() )
       , Key( [KEY_MOD, KEY_CTRL],  KEY_K,                lazy.layout.grow_right() )
       , Key( [KEY_MOD, KEY_CTRL],  KEY_H,                lazy.layout.grow_down() )
       , Key( [KEY_MOD, KEY_CTRL],  KEY_L,                lazy.layout.grow_up() )
       , Key( [KEY_MOD, KEY_CTRL],  KEY_N,                lazy.layout.normalize() )
                      
       , Key( [KEY_MOD, KEY_SHIFT], KEY_RETURN,           lazy.layout.toggle_split() )
                      
       , Key( [KEY_MOD],            KEY_TAB,              lazy.next_layout() )
               
       # My bindings               
       , Key( [KEY_MOD],            KEY_RETURN,           lazy.spawn(TERMINAL_APP) )
       , Key( [KEY_MOD],            KEY_F,                lazy.spawn(FILE_MANAGER_APP) )
       , Key( [KEY_MOD, KEY_SHIFT], KEY_F,                lazy.window.toggle_fullscreen() )
       , Key( [KEY_MOD],            KEY_B,                lazy.spawn(WEB_BROWSER_APP) )
       , Key( [KEY_MOD],            KEY_C,                lazy.spawn(CODE_EDITOR_APP) )
       , Key( [KEY_MOD],            KEY_V,                lazy.spawn(VOLUME_APP) )
       , Key( [KEY_MOD, KEY_CTRL],  KEY_Q,                lazy.shutdown() )
       , Key( [KEY_MOD, KEY_SHIFT], KEY_Q,                lazy.window.kill() )
       , Key( [KEY_MOD],            KEY_R,                lazy.spawncmd() )
       , Key( [KEY_MOD, KEY_SHIFT], KEY_R,                lazy.restart() )
       , Key( [KEY_MOD],            KEY_T,                lazy.window.toggle_floating() )
       
       # Sound bindings
       , Key( [],                   KEY_XF86_AUDIO_MUTE,  lazy.spawn(COMMAND_VOLUME_MUTE) )
       , Key( [],                   KEY_XF86_AUDIO_LOWER, lazy.spawn(COMMAND_VOLUME_LOWER) )
       , Key( [],                   KEY_XF86_AUDIO_RAISE, lazy.spawn(COMMAND_VOLUME_RAISE) ) ]  

# //////////////////////////////////////////////////////////////////////////// MOUSE BINDINGS //////////////////////////////////////////////////////////////////////////// #

mouse = [ Drag(  [KEY_MOD], LEFT_CLICK,   lazy.window.set_position_floating(), start=lazy.window.get_position() )
        , Drag(  [KEY_MOD], RIGHT_CLICK,  lazy.window.set_size_floating(),     start=lazy.window.get_size()     )
        , Click( [KEY_MOD], MIDDLE_CLICK, lazy.window.bring_to_front()                                          ) ]

# //////////////////////////////////////////////////////////////////////////// GROUP SETTINGS //////////////////////////////////////////////////////////////////////////// #

groups = [ Group(group, GROUP_DEFAULTS) for group in GROUP_NAMES]

# Bind to groups
for i, _ in enumerate(groups):
    group_name = str( (i + 1) % 10 ) # Mod 10 to make 10 bind to 0

    keys.extend([ Key( [KEY_MOD],            group_name, lazy.group[GROUP_NAMES[i]].toscreen()                  )    # Switch to group
                , Key( [KEY_MOD, KEY_SHIFT], group_name, lazy.window.togroup(GROUP_NAMES[i], switch_group=True) ) ]) # Switch to and move focused window to group

# //////////////////////////////////////////////////////////////////////////////// LAYOUT //////////////////////////////////////////////////////////////////////////////// #

layout_theme = { "border_width":  BORDER_WIDTH_LAYOUT_THEME
               , "margin":        MARGIN_LAYOUT_THEME
               , "border_focus":  COLOR_FOREGROUND
               , "border_normal": COLOR_BACKGROUND }

layouts = [ layout.MonadTall(**layout_theme)
          , layout.Max(**layout_theme)
          , layout.Matrix(**layout_theme)
          , layout.VerticalTile(**layout_theme)
          , layout.Zoomy(**layout_theme)
          , layout.MonadWide(**layout_theme) ]

# Try more layouts by unleashing below layouts.
# layout.Columns(border_focus_stack='#d75f5f'),
# layout.Stack(num_stacks=2),
# layout.Bsp(),
# layout.RatioTile(),
# layout.Tile(),
# layout.TreeTab(),

# /////////////////////////////////////////////////////////////////////////// FLOATING WINDOWS /////////////////////////////////////////////////////////////////////////// #

FLOAT_WINDOWS = [ *layout.Floating.default_float_rules 
                , Match( title    = "branchdialog" )
                , Match( title    = "pinentry" )
                , Match( wm_class = "confirmreset" )
                , Match( wm_class = "makebranch" ) 
                , Match( wm_class = "maketag" )
                , Match( wm_class = "ssh-askpass" )
                
                # Custom windows
                , Match( title    = "AUR Updates" )
                , Match( title    = "Pacman Updates" )
                , Match( wm_class = "pavucontrol" ) ]

FLOATING_LAYOUT_RULES = layout.Floating( float_rules   = FLOAT_WINDOWS
                                       , border_focus  = COLOR_FOREGROUND
                                       , border_normal = COLOR_BACKGROUND )

# ////////////////////////////////////////////////////////////////////////// WIDGET DEFINITIONS ////////////////////////////////////////////////////////////////////////// #

# --------------------------------------------------------------------------- WIDGET CALLBACKS --------------------------------------------------------------------------- #

CALLBACK_PYTHON_LOGO              = launchTerminalCommand(PYTHON_INTERPRETER)
CALLBACK_WIDGET_CPU               = spawn(COMMAND_NOTIFY_NO_CALLBACK)
CALLBACK_WIDGET_TEMP              = spawn(COMMAND_NOTIFY_NO_CALLBACK)
CALLBACK_WIDGET_DISK              = spawn(COMMAND_OPEN_ROOT_DIRECTORY)
CALLBACK_WIDGET_MEMORY            = launchTerminalCommand(HTOP_APP)
CALLBACK_WIDGET_WEATHER           = spawn(COMMAND_LAUNCH_OPEN_WEATHER_FORMAT.format(WEB_BROWSER_APP, OPEN_WEATHER_URL, MEDELLIN_CITY_CODE))
CALLBACK_WIDGET_NET               = spawn(COMMAND_NOTIFY_NO_CALLBACK)
CALLBACK_WIDGET_UPDATE_PAC        = launchTerminalCommand(SCRIPT_QUERY_UPDATES_PACMAN, TERMINAL_TITLE_PACMAN, True)
CALLBACK_WIDGET_BOX_02_UPDATE_PAC = launchTerminalCommand(SCRIPT_INSTALL_UPDATES_PACMAN, TERMINAL_TITLE_INSTALLING_PACMAN)
CALLBACK_WIDGET_UPDATE_AUR        = launchTerminalCommand(SCRIPT_QUERY_UPDATES_TAUR, TERMINAL_TITLE_TAUR, True)
CALLBACK_WIDGET_BOX_02_UPDATE_AUR = launchTerminalCommand(SCRIPT_INSTALL_UPDATES_TAUR, TERMINAL_TITLE_INSTALLING_TAUR)
CALLBACK_WIDGET_VOLUME            = spawn(VOLUME_APP)
CALLBACK_WIDGET_WINDOWS           = spawn(COMMAND_NOTIFY_NO_CALLBACK)
CALLBACK_WIDGET_CLOCK             = spawn(COMMAND_NOTIFY_NO_CALLBACK)
CALLBACK_WIDGET_KEYBOARD          = spawn(COMMAND_NOTIFY_NO_CALLBACK)
CALLBACK_WIDGET_POWER             = spawn(SCRIPT_SHUTDOWN_HANDLER)

# ---------------------------------------------------------------------------- WIDGET OBJECTS ---------------------------------------------------------------------------- #

separator_widget      = getSeparator(LINE_WIDTH_SEPARATOR)
   
python_logo_widget    = widget.Image( filename        = PATH_LOGO_PYTHON
                                    , mouse_callbacks = setMouseCallbacks(CALLBACK_PYTHON_LOGO)
                                    , margin          = MARGIN_PYTHON_LOGO
                                    , background      = COLOR_BACKGROUND )
   
group_box_widget      = widget.GroupBox( font                        = FONT_FAMILY_WIDGET_GROUP_BOX
                                       , fontsize                    = FONT_SIZE_WIDGET_GROUP_BOX
                                       , margin_x                    = MARGIN_X_GROUP_BOX
                                       , margin_y                    = MARGIN_Y_GROUP_BOX
                                       , padding                     = PADDING_GROUP_BOX
                                       , borderwidth                 = BORDER_WIDTH_GROUP_BOX
                                       , disable_drag                = DISABLE_DRAG_GROUP_BOX
                                       , highlight_method            = HIGHLIGHT_METHOD_GROUP_BOX
                                       , highlight_color             = COLOR_HIGHLIGHT_GROUP_BOX
                                       , active                      = COLOR_FOREGROUND
                                       , inactive                    = COLOR_INACTIVE_GROUP_BOX
                                       , this_current_screen_border  = COLOR_FOREGROUND
                                       , this_screen_border          = COLOR_BLUE
                                       , other_current_screen_border = COLOR_PURPLE
                                       , other_screen_border         = COLOR_GREY
                                       , background                  = COLOR_BACKGROUND
                                       , foreground                  = COLOR_FOREGROUND )
   
prompt_widget         = widget.Prompt( prompt     = PROMPT_WIDGET_PROMPT
                                     , font       = FONT_FAMILY_WIDGET_PROMPT
                                     , fontsize   = FONT_SIZE_WIDGET_PROMPT
                                     , padding    = PADDING_WIDGET_PROMPT
                                     , background = BACKGROUND_COLOR_PROMPT_WIDGET
                                     , foreground = FOREGROUND_COLOR_PROMPT_WIDGET )
   
window_name_widget    = widget.WindowName( font       = FONT_FAMILY_WIDGET_WINDOW_NAME
                                         , fontsize   = FONT_SIZE_WIDGET_WINDOW_NAME
                                         , background = BACKGROUND_COLOR_WIDGET_WINDOW_NAME
                                         , foreground = COLOR_FOREGROUND )

minimal_window_name_widget = widget.WindowName( font       = FONT_FAMILY_WIDGET_WINDOW_NAME
                                              , fontsize   = FONT_SIZE_WIDGET_WINDOW_NAME
                                              , background = BACKGROUND_COLOR_WIDGET_WINDOW_NAME
                                              , foreground = COLOR_FOREGROUND )
   
systray_widget        =  widget.Systray( padding    = PADDING_WIDGET_SYSTRAY
                                       , icon_size  = ICON_SIZE_WIDGET_SYSTRAY
                                       , background = COLOR_BACKGROUND
                                       , foreground = COLOR_FOREGROUND )
   
cpu_widget            = widget.CPU( fmt             = FMT_WIDGET_CPU 
                                  , format          = FORMAT_WIDGET_CPU
                                  , update_interval = UPDATE_INTERVAL_WIDGET_CPU
                                  , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_CPU)
                                  , background      = BACKGROUND_COLOR_WIDGET_CPU
                                  , foreground      = COLOR_FOREGROUND )
   
cpu_widget_box        = [ widget.CPU( fmt              = BOX_FMT
                                    , format           = FORMAT_WIDGET_BOX_01_CPU
                                    , update_interval  = UPDATE_INTERVAL_WIDGET_CPU
                                    , mouse_callbacks  = setMouseCallbacks(CALLBACK_WIDGET_CPU)
                                    , background       = BACKGROUND_COLOR_WIDGET_CPU
                                    , foreground       = COLOR_FOREGROUND ) ]
   
temp_widget           = widget.ThermalSensor( fmt              = FMT_WIDGET_TEMP
                                            , threshold        = THRESHOLD_WIDGET_TEMP
                                            , update_interval  = UPDATE_INTERVAL_WIDGET_TEMP
                                            , mouse_callbacks  = setMouseCallbacks(CALLBACK_WIDGET_TEMP)
                                            , background       = BACKGROUND_COLOR_WIDGET_TEMP
                                            , foreground       = COLOR_FOREGROUND
                                            , foreground_alert = ALERT_COLOR_TEMP )
   
disk_widget           = widget.DF( fmt             = FMT_WIDGET_DISK
                                 , format          = FORMAT_WIDGET_DISK
                                 , warn_space      = THRESHOLD_WIDGET_DISK
                                 , warn_color      = ALERT_COLOR_DISK
                                 , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_DISK)
                                 , visible_on_warn = False
                                 , background      = BACKGROUND_COLOR_WIDGET_DISK
                                 , foreground      = FOREGROUND_COLOR_WIDGET_DISK )
   
disk_widget_box       = [ widget.DF( fmt              = BOX_FMT
                                   , format           = FORMAT_WIDGET_BOX_01_DISK
                                   , warn_space       = THRESHOLD_WIDGET_DISK
                                   , warn_color       = ALERT_COLOR_DISK
                                   , mouse_callbacks  = setMouseCallbacks(CALLBACK_WIDGET_DISK)
                                   , visible_on_warn  = False
                                   , background       = BACKGROUND_COLOR_WIDGET_DISK
                                   , foreground       = FOREGROUND_COLOR_WIDGET_DISK )
   
                        , widget.DF( fmt              = BOX_FMT
                                   , format           = FORMAT_WIDGET_BOX_02_DISK
                                   , warn_space       = THRESHOLD_WIDGET_DISK
                                   , warn_color       = ALERT_COLOR_DISK
                                   , mouse_callbacks  = setMouseCallbacks(CALLBACK_WIDGET_DISK)
                                   , visible_on_warn  = False
                                   , background       = BACKGROUND_COLOR_WIDGET_DISK
                                   , foreground       = FOREGROUND_COLOR_WIDGET_DISK )
             
                        , widget.DF( fmt              = BOX_FMT
                                   , format           = FORMAT_WIDGET_BOX_03_DISK
                                   , warn_space       = THRESHOLD_WIDGET_DISK
                                   , warn_color       = ALERT_COLOR_DISK
                                   , mouse_callbacks  = setMouseCallbacks(CALLBACK_WIDGET_DISK)
                                   , visible_on_warn  = False
                                   , background       = BACKGROUND_COLOR_WIDGET_DISK
                                   , foreground       = FOREGROUND_COLOR_WIDGET_DISK ) ]
   
memory_widget         = widget.Memory( fmt              = FMT_WIDGET_MEMORY
                                     , format           = FORMAT_WIDGET_MEMORY
                                     , update_interval  = UPDATE_INTERVAL_WIDGET_MEMORY
                                     , mouse_callbacks  = setMouseCallbacks(CALLBACK_WIDGET_MEMORY)
                                     , background       = BACKGROUND_COLOR_WIDGET_MEMORY
                                     , foreground       = FOREGROUND_COLOR_WIDGET_MEMORY )
   
memory_widget_box     = [ widget.Memory( fmt             = BOX_FMT
                                       , format          = FORMAT_WIDGET_BOX_01_MEMORY
                                       , update_interval = UPDATE_INTERVAL_WIDGET_MEMORY
                                       , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_MEMORY)
                                       , background      = BACKGROUND_COLOR_WIDGET_MEMORY
                                       , foreground      = FOREGROUND_COLOR_WIDGET_MEMORY )
   
                        , widget.Memory( fmt             = BOX_FMT
                                       , format          = FORMAT_WIDGET_BOX_02_MEMORY
                                       , update_interval = UPDATE_INTERVAL_WIDGET_MEMORY
                                       , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_MEMORY)
                                       , background      = BACKGROUND_COLOR_WIDGET_MEMORY
                                       , foreground      = FOREGROUND_COLOR_WIDGET_MEMORY )
   
                        , widget.Memory( fmt             = BOX_FMT
                                       , format          = FORMAT_WIDGET_BOX_03_MEMORY
                                       , update_interval = UPDATE_INTERVAL_WIDGET_MEMORY
                                       , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_MEMORY)
                                       , background      = BACKGROUND_COLOR_WIDGET_MEMORY
                                       , foreground      = FOREGROUND_COLOR_WIDGET_MEMORY )
   
                        , widget.Memory( fmt             = BOX_FMT
                                       , format          = FORMAT_WIDGET_BOX_04_MEMORY
                                       , update_interval = UPDATE_INTERVAL_WIDGET_MEMORY
                                       , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_MEMORY)
                                       , background      = BACKGROUND_COLOR_WIDGET_MEMORY
                                       , foreground      = FOREGROUND_COLOR_WIDGET_MEMORY ) ]
   
weather_widget        = widget.OpenWeather( fmt              = FMT_WIDGET_WEATHER
                                          , format           = FORMAT_WIDGET_WEATHER
                                          , cityid           = MEDELLIN_CITY_CODE
                                          , update_interval  = UPDATE_INTERVAL_WIDGET_WEATHER
                                          , mouse_callbacks  = setMouseCallbacks(CALLBACK_WIDGET_WEATHER)
                                          , background       = BACKGROUND_COLOR_WIDGET_WEATHER
                                          , foreground       = FOREGROUND_COLOR_WIDGET_WEATHER )
   
weather_widget_box    = [ widget.OpenWeather( fmt             = BOX_FMT
                                            , format          = FORMAT_WIDGET_BOX_01_WEATHER
                                            , cityid          = MEDELLIN_CITY_CODE
                                            , update_interval = UPDATE_INTERVAL_WIDGET_WEATHER
                                            , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_WEATHER)
                                            , background      = BACKGROUND_COLOR_WIDGET_WEATHER
                                            , foreground      = FOREGROUND_COLOR_WIDGET_WEATHER )
        
                        , widget.OpenWeather( fmt             = BOX_FMT
                                            , format          = FORMAT_WIDGET_BOX_02_WEATHER
                                            , cityid          = MEDELLIN_CITY_CODE
                                            , update_interval = UPDATE_INTERVAL_WIDGET_WEATHER
                                            , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_WEATHER)
                                            , background      = BACKGROUND_COLOR_WIDGET_WEATHER
                                            , foreground      = FOREGROUND_COLOR_WIDGET_WEATHER )
        
                        , widget.OpenWeather( fmt             = BOX_FMT
                                            , format          = FORMAT_WIDGET_BOX_03_WEATHER
                                            , cityid          = MEDELLIN_CITY_CODE
                                            , update_interval = UPDATE_INTERVAL_WIDGET_WEATHER
                                            , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_WEATHER)
                                            , background      = BACKGROUND_COLOR_WIDGET_WEATHER
                                            , foreground      = FOREGROUND_COLOR_WIDGET_WEATHER ) ]
   
net_down_widget       = widget.Net( fmt        = FMT_WIDGET_NET_DOWN
                                  , format     = FORMAT_WIDGET_NET_DOWN
                                  , interface  = LAN_NETWORK_INTERFACE
                                  , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_NET)
                                  , background = BACKGROUND_COLOR_WIDGET_NET
                                  , foreground = FOREGROUND_COLOR_WIDGET_NET )
   
net_up_widget         = widget.Net( fmt          = FMT_WIDGET_NET_UP
                                  , format       = FORMAT_WIDGET_NET_UP
                                  , interface    = LAN_NETWORK_INTERFACE
                                  , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_NET)
                                  , background   = BACKGROUND_COLOR_WIDGET_NET
                                  , foreground   = FOREGROUND_COLOR_WIDGET_NET )
   
update_pac_widget     = widget.CheckUpdates( fmt                  = FMT_WIDGET_UPDATE_PAC
                                           , display_format       = FORMAT_WIDGET_UPDATE_PAC
                                           , distro               = LINUX_DISTRIBUTION
                                           , no_update_string     = DEFAULT_STRING_WIDGET_UPDATE_PAC
                                           , colour_have_updates  = FOREGROUND_COLOR_WIDGET_UPDATE_PAC
                                           , colour_no_updates    = FOREGROUND_COLOR_WIDGET_UPDATE_PAC
                                           , update_interval      = UPDATE_INTERVAL_WIDGET_UPDATE_PAC
                                           , custom_command       = COMMAND_UPDATE_PAC_CHECK
                                           , mouse_callbacks      = setMouseCallbacks(CALLBACK_WIDGET_UPDATE_PAC)
                                           , background           = BACKGROUND_COLOR_WIDGET_UPDATE_PAC
                                           , foreground           = FOREGROUND_COLOR_WIDGET_UPDATE_PAC )
   
update_pac_widget_box = [ widget.TextBox( fmt                     = BOX_FMT
                                        , text                    = FORMAT_WIDGET_BOX_01_UPDATE_PAC
                                        , mouse_callbacks         = setMouseCallbacks(CALLBACK_WIDGET_UPDATE_PAC)
                                        , background              = BACKGROUND_COLOR_WIDGET_UPDATE_PAC
                                        , foreground              = FOREGROUND_COLOR_WIDGET_UPDATE_PAC )
   
                        , widget.TextBox( fmt                     = BOX_FMT
                                        , text                    = FORMAT_WIDGET_BOX_02_UPDATE_PAC
                                        , mouse_callbacks         = setMouseCallbacks(CALLBACK_WIDGET_BOX_02_UPDATE_PAC)
                                        , background              = BACKGROUND_COLOR_WIDGET_UPDATE_PAC
                                        , foreground              = FOREGROUND_COLOR_WIDGET_UPDATE_PAC ) ]
   
update_aur_widget     = widget.CheckUpdates( fmt                  = FMT_WIDGET_UPDATE_AUR
                                           , display_format       = FORMAT_WIDGET_UPDATE_AUR
                                           , distro               = LINUX_DISTRIBUTION
                                           , no_update_string     = DEFAULT_STRING_WIDGET_UPDATE_AUR
                                           , colour_have_updates  = FOREGROUND_COLOR_WIDGET_UPDATE_AUR
                                           , colour_no_updates    = FOREGROUND_COLOR_WIDGET_UPDATE_AUR
                                           , update_interval      = UPDATE_INTERVAL_WIDGET_UPDATE_AUR
                                           , custom_command       = COMMAND_UPDATE_AUR_CHECK
                                           , mouse_callbacks      = setMouseCallbacks(CALLBACK_WIDGET_UPDATE_AUR)
                                           , background           = BACKGROUND_COLOR_WIDGET_UPDATE_AUR
                                           , foreground           = FOREGROUND_COLOR_WIDGET_UPDATE_AUR )
    
update_aur_widget_box = [ widget.TextBox( fmt                     = BOX_FMT
                                        , text                    = FORMAT_WIDGET_BOX_01_UPDATE_AUR
                                        , mouse_callbacks         = setMouseCallbacks(CALLBACK_WIDGET_UPDATE_AUR)
                                        , background              = BACKGROUND_COLOR_WIDGET_UPDATE_AUR
                                        , foreground              = FOREGROUND_COLOR_WIDGET_UPDATE_AUR )

                        , widget.TextBox( fmt                     = BOX_FMT
                                        , text                    = FORMAT_WIDGET_BOX_02_UPDATE_AUR
                                        , mouse_callbacks         = setMouseCallbacks(CALLBACK_WIDGET_BOX_02_UPDATE_AUR)
                                        , background              = BACKGROUND_COLOR_WIDGET_UPDATE_AUR
                                        , foreground              = FOREGROUND_COLOR_WIDGET_UPDATE_AUR ) ]

volume_widget         = widget.Volume( fmt             = FMT_WIDGET_VOLUME
                                     , volume_app      = VOLUME_APP
                                     , update_interval = UPDATE_INTERVAL_WIDGET_VOLUME
                                     , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_VOLUME)
                                     , background      = BACKGROUND_COLOR_WIDGET_VOLUME
                                     , foreground      = FOREGROUND_COLOR_WIDGET_VOLUME )

windows_widget        = widget.WindowCount( fmt             = FMT_WIDGET_WINDOWS
                                          , show_zero       = False
                                          , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_WINDOWS)
                                          , background      = BACKGROUND_COLOR_WIDGET_WINDOWS
                                          , foreground      = COLOR_FOREGROUND )

minimal_windows_widget = widget.WindowCount( fmt             = FMT_WIDGET_WINDOWS
                                           , show_zero       = False
                                           , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_WINDOWS)
                                           , background      = COLOR_LIGHT_GREY
                                           , foreground      = COLOR_FOREGROUND )

clock_widget          = widget.Clock( fmt              = FMT_WIDGET_CLOCK
                                    , format           = FORMAT_WIDGET_CLOCK 
                                    , update_interval  = UPDATE_INTERVAL_WIDGET_CLOCK
                                    , mouse_callbacks  = setMouseCallbacks(CALLBACK_WIDGET_CLOCK)
                                    , background       = BACKGROUND_COLOR_WIDGET_CLOCK
                                    , foreground       = COLOR_FOREGROUND )

clock_widget_box      = [ widget.Clock( fmt             = BOX_FMT
                                      , format          = FORMAT_WIDGET_BOX_01_CLOCK
                                      , update_interval = UPDATE_INTERVAL_WIDGET_CLOCK
                                      , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_CLOCK)
                                      , background      = BACKGROUND_COLOR_WIDGET_CLOCK
                                      , foreground      = COLOR_FOREGROUND ) ]

minimal_clock_widget  = widget.Clock( fmt              = FMT_WIDGET_CLOCK
                                    , format           = FORMAT_WIDGET_CLOCK 
                                    , update_interval  = UPDATE_INTERVAL_WIDGET_CLOCK
                                    , mouse_callbacks  = setMouseCallbacks(CALLBACK_WIDGET_CLOCK)
                                    , background       = COLOR_ORANGE
                                    , foreground       = COLOR_FOREGROUND )

minimal_clock_widget_box = [ widget.Clock( fmt             = BOX_FMT
                                         , format          = FORMAT_WIDGET_BOX_01_CLOCK
                                         , update_interval = UPDATE_INTERVAL_WIDGET_CLOCK
                                         , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_CLOCK)
                                         , background      = COLOR_ORANGE
                                         , foreground      = COLOR_FOREGROUND ) ]

keyboard_widget       = widget.KeyboardLayout( fmt                  = FMT_WIDGET_KEYBOARD
                                             , configured_keyboards = CONFIGURED_KEYBOARDS
                                             , update_interval      = UPDATE_INTERVAL_WIDGET_KEYBOARD
                                             , mouse_callbacks      = setMouseCallbacks(CALLBACK_WIDGET_KEYBOARD)
                                             , background           = BACKGROUND_COLOR_WIDGET_KEYBOARD
                                             , foreground           = COLOR_FOREGROUND )

power_widget          = widget.Image( filename        = PATH_BAR_ICONS_FORMAT.format(ICON_NAME_POWER)
                                    , margin          = MARGIN_ICON_DEFAULT
                                    , scale           = SCALE_ICON_DEFAULT
                                    , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_POWER)
                                    , background      = BACKGROUND_COLOR_WIDGET_POWER
                                    , foreground      = COLOR_FOREGROUND )

minimal_power_widget = widget.Image( filename        = PATH_BAR_ICONS_FORMAT.format(ICON_NAME_POWER)
                                   , margin          = MARGIN_ICON_DEFAULT
                                   , scale           = SCALE_ICON_DEFAULT
                                   , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_POWER)
                                   , background      = COLOR_RED
                                   , foreground      = COLOR_FOREGROUND )
# WIFI
# widget.Wlan( interface            = WIFI_NETWORK_INTERFACE
#            , format               = "{essid} {quality}/70"
#            , disconnected_message = "disconnected" )

# //////////////////////////////////////////////////////////////////////////// WIDGET LAYOUT //////////////////////////////////////////////////////////////////////////// #

all_bar_widgets = [ BarWidget( widget_object = python_logo_widget 
                             , callback      = CALLBACK_PYTHON_LOGO ) 
                             
                  , BarWidget( widget_object = separator_widget ) 
                  
                  , BarWidget( widget_object = group_box_widget ) 

                  , BarWidget( widget_object = separator_widget ) 

                  , BarWidget( widget_object = prompt_widget ) 

                  , BarWidget( widget_object = window_name_widget ) 

                  , BarWidget( widget_object = systray_widget ) 

                  , BarWidget( widget_object = cpu_widget
                             , widget_box    = cpu_widget_box
                             , callback      = CALLBACK_WIDGET_CPU
                             , icon_name     = ICON_NAME_CPU
                             , use_arrow     = True
                             , background    = COLOR_RED ) 

                  , BarWidget( widget_object = temp_widget
                             , callback      = CALLBACK_WIDGET_TEMP
                             , icon_name     = ICON_NAME_TEMP
                             , use_arrow     = True
                             , background    = COLOR_ORANGE ) 
                             
                  , BarWidget( widget_object = disk_widget
                             , widget_box    = disk_widget_box
                             , callback      = CALLBACK_WIDGET_DISK
                             , icon_name     = ICON_NAME_DISK
                             , use_arrow     = True
                             , background    = COLOR_YELLOW
                             , foreground    = COLOR_FOREGROUND_YELLOW ) 
                             
                  , BarWidget( widget_object = memory_widget
                             , widget_box    = memory_widget_box
                             , callback      = CALLBACK_WIDGET_MEMORY
                             , icon_name     = ICON_NAME_MEMORY
                             , use_arrow     = True
                             , background    = COLOR_GREEN
                             , foreground    = COLOR_FOREGROUND_GREEN )

                  , BarWidget( widget_object = weather_widget
                             , widget_box    = weather_widget_box
                             , callback      = CALLBACK_WIDGET_WEATHER
                             , icon_name     = ICON_NAME_WEATHER
                             , use_arrow     = True
                             , background    = COLOR_BLUE
                             , foreground    = COLOR_FOREGROUND_BLUE ) 
                             
                  , BarWidget( widget_object = net_down_widget
                             , callback      = CALLBACK_WIDGET_NET
                             , icon_name     = ICON_NAME_NET_DOWN
                             , use_arrow     = True
                             , background    = COLOR_PURPLE
                             , foreground    = COLOR_FOREGROUND_PURPLE ) 
                             
                  , BarWidget( widget_object = net_up_widget
                             , callback      = CALLBACK_WIDGET_NET
                             , icon_name     = ICON_NAME_NET_UP
                             , background    = COLOR_PURPLE
                             , foreground    = COLOR_FOREGROUND_PURPLE ) 
                             
                  , BarWidget( widget_object = update_pac_widget
                             , widget_box    = update_pac_widget_box
                             , callback      = CALLBACK_WIDGET_UPDATE_PAC
                             , icon_name     = ICON_NAME_UPDATE_PAC
                             , use_arrow     = True
                             , background    = COLOR_LIGHT_BLUE
                             , foreground    = COLOR_FOREGROUND_LIGHT_BLUE ) 
                             
                  , BarWidget( widget_object = update_aur_widget
                             , widget_box    = update_aur_widget_box
                             , callback      = CALLBACK_WIDGET_UPDATE_AUR
                             , icon_name     = ICON_NAME_UPDATE_AUR
                             , use_arrow     = True
                             , background    = COLOR_CYAN
                             , foreground    = COLOR_FOREGROUND_CYAN ) 
                             
                  , BarWidget( widget_object = volume_widget
                             , callback      = CALLBACK_WIDGET_VOLUME
                             , icon_name     = ICON_NAME_VOLUME
                             , use_arrow     = True
                             , background    = COLOR_AQUA
                             , foreground    = COLOR_FOREGROUND_AQUA )
                             
                  , BarWidget( widget_object = windows_widget
                             , callback      = CALLBACK_WIDGET_WINDOWS
                             , icon_name     = ICON_NAME_WINDOWS
                             , use_arrow     = True
                             , background    = COLOR_LIGHT_GREY ) 
                             
                  , BarWidget( widget_object = clock_widget
                             , widget_box    = clock_widget_box
                             , callback      = CALLBACK_WIDGET_CLOCK
                             , icon_name     = ICON_NAME_CLOCK
                             , use_arrow     = True
                             , background    = COLOR_GREY )
                             
                  , BarWidget( widget_object = keyboard_widget
                             , callback      = CALLBACK_WIDGET_KEYBOARD
                             , icon_name     = ICON_NAME_KEYBOARD
                             , use_arrow     = True
                             , background    = COLOR_DARK_GREY ) 
                             
                  , BarWidget( widget_object = power_widget
                             , callback      = CALLBACK_WIDGET_POWER
                             , use_arrow     = True
                             , background    = COLOR_BLACK ) ]

minimal_bar_widgets = [ BarWidget( widget_object = python_logo_widget 
                                 , callback      = CALLBACK_PYTHON_LOGO ) 
                             
                      , BarWidget( widget_object = separator_widget ) 
                      
                      , BarWidget( widget_object = group_box_widget ) 
    
                      , BarWidget( widget_object = separator_widget ) 
    
                      , BarWidget( widget_object = prompt_widget ) 
    
                      , BarWidget( widget_object = minimal_window_name_widget ) 
    
                      , BarWidget( widget_object = minimal_windows_widget
                                 , callback      = CALLBACK_WIDGET_WINDOWS
                                 , icon_name     = ICON_NAME_WINDOWS
                                 , use_arrow     = True
                                 , background    = COLOR_LIGHT_GREY ) 
                                 
                      , BarWidget( widget_object = minimal_clock_widget
                                 , widget_box    = minimal_clock_widget_box
                                 , callback      = CALLBACK_WIDGET_CLOCK
                                 , icon_name     = ICON_NAME_CLOCK
                                 , use_arrow     = True
                                 , background    = COLOR_ORANGE )
                                   
                      , BarWidget( widget_object = minimal_power_widget
                                 , callback      = CALLBACK_WIDGET_POWER
                                 , use_arrow     = True
                                 , background    = COLOR_RED ) ]

# /////////////////////////////////////////////////////////////////////////// SCREEN SETTINGS /////////////////////////////////////////////////////////////////////////// #

screen_0_bar = getBar(all_bar_widgets)
screen_1_bar = getBar(minimal_bar_widgets)

screen_0     = Screen( bottom = bar.Bar( screen_0_bar, 24 ) )
screen_1     = Screen( top    = bar.Bar( screen_1_bar, 24 ) )

screens      = [ screen_0
               , screen_1 ]

# //////////////////////////////////////////////////////////////////////////// STARTUP HOOKS //////////////////////////////////////////////////////////////////////////// #

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# /////////////////////////////////////////////////////////////////////////// OTHER SETTINGS /////////////////////////////////////////////////////////////////////////// #

dgroups_key_binder         = None
dgroups_app_rules          = [] # #type: List
main                       = None # WARNING: this is deprecated and will be removed soon
follow_mouse_focus         = True
bring_front_click          = False
cursor_warp                = False
        
floating_layout            = FLOATING_LAYOUT_RULES
        
auto_fullscreen            = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
