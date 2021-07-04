import os
import subprocess
#from typing import List  # noqa: F401
from libqtile import bar, layout, widget, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# ////////////////////////////////////////////////////////////// VARIABLE DECLARATIONS ////////////////////////////////////////////////////////////// #

# ============= COLORS ============= #
COLOR_RED          = "#bf616a" # "#e06c75" 
COLOR_ORANGE       = "#d19a66" # "#d19a66" 
COLOR_YELLOW       = "#ebcb8b" # "#e5c07b"
COLOR_GREEN        = "#a3be8c" # "#97c278"
COLOR_CYAN         = "#88c0d0" # "#56b6c2" 
COLOR_BLUE         = "#81a1c1" # "#61afef"
COLOR_PURPLE       = "#b48ead" # "#c678dd"
COLOR_LIGHT_RED    = "#c6727a" # "#fbeaeb"
COLOR_LIGHT_YELLOW = "#edd198" # "#faf3e6"
COLOR_DARK_WHITE   = "#e5e9f0" #"#abb2bf"
COLOR_BLACK        = "#2e3440"
COLOR_LIGHT_BLACK  = "#4c566a"
COLOR_DARK_GREY    = "#3b4252" # "#5b6477" 
COLOR_BACKGROUND   = COLOR_BLACK
COLOR_FOREGROUND   = COLOR_DARK_WHITE

# = CHARACTERS = #
CHAR_ARROW = "❮"
CHAR_EMPTY = ""

# ===== DEFAULT APPLICATIONS ===== #
APP_ROFI         = "rofi -show run"
APP_PAVUCONTROL  = "pavucontrol"
APP_TERMINAL     = "alacritty"
APP_WEB_BROWSER  = "firefox"
APP_PYTHON       = "python"
APP_FILE_MANAGER = "nemo"
APP_CODE_EDITOR  = "code" 

# ====================================================== SCRIPTS ====================================================== #
SCRIPT_WATCH_SENSORS         = "watch -n 1 -p sensors"
SCRIPT_WATCH_CPU             = "watch --no-title -c -n 1 -x zsh /home/santiago/.scripts/Qtile\ Bar\ Scripts/cpu-info.sh"
SCRIPT_WATCH_MEM             = "watch -n 1 -p /home/santiago/.scripts/mem-info.sh"
SCRIPT_MANAGE_UPDATES_PACMAN = "/home/santiago/.scripts/pacman-updates.sh -Mu"
SCRIPT_MANAGE_UPDATES_AUR    = "/home/santiago/.scripts/rpm -M"
SCRIPT_SHUTDOWN_HANDLER      = "/home/santiago/.scripts/shutdown-handler.sh -s"

# ================== TERMINAL TITLES ================== #
TERMINAL_TITLE_WATCH_CPU     = "Watching CPU"
TERMINAL_TITLE_WATCH_SENSORS = "Watching Sensors"
TERMINAL_TITLE_WATCH_MEM     = "Watching MEM"
TERMINAL_TITLE_PACMAN        = "Available Pacman Updates"
TERMINAL_TITLE_AUR           = "Available AUR Updates"

# =================================== GROUPS =================================== #
GROUP_NAMES = [ "MAIN", "SYS", "DEV", "WWW", "GFX", "6", "7", "8", "DOCS", "TV" ]
GROUP_DEFAULTS = { "layout": "monadtall" }

# ================== KEYS ================== #
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

# === MOUSE BUTTONS === #
LEFT_CLICK   = "Button1"
MIDDLE_CLICK = "Button2"
RIGHT_CLICK  = "Button3"

# =================================== COMMANDS =================================== #
COMMAND_NOTIFY_NO_CALLBACK         = "dunstify -i /home/santiago/.config/dunst/icons/alert.png -u low -t 2500 -a 'Qtile Bar' 'No Callback' 'this widget has no callback' &"
COMMAND_UPDATE_PAC_CHECK           = "/home/santiago/.scripts/pacman-updates.sh -Lu"
COMMAND_UPDATE_AUR_CHECK           = "/home/santiago/.scripts/rpm -q -Syqu"
COMMAND_VOLUME_LOWER               = "amixer sset 'Master' 2%+ unmute"
COMMAND_VOLUME_RAISE               = "amixer sset 'Master' 2%+ unmute"
COMMAND_OPEN_ROOT_DIRECTORY        = "{} /".format(APP_FILE_MANAGER)
COMMAND_VOLUME_MUTE                = "amixer -q set Master toggle"
COMMAND_LAUNCH_IN_TERMINAL_FORMAT  = "{} --title '{}' {} -e {}"
COMMAND_LAUNCH_OPEN_WEATHER_FORMAT = "{} --new-window {}{}"

# ======================== PATHS ======================== #
PATH_LOGO_PYTHON      = "~/.config/qtile/icons/python.svg"
PATH_BAR_ICONS_FORMAT = "~/.config/qtile/icons/bar/{}.svg"

# ======= TERMINAL FLAGS ======= #
TERMINAL_FLAG_HOLD_OPEN = "--hold"

# ====== DEVICE VARIABLES ====== #
WIFI_NETWORK_INTERFACE = "wlp34s0"
LAN_NETWORK_INTERFACE  = "eno1"
LINUX_DISTRIBUTION     = "Arch"

# ============== OPEN WEATHER VARIABLES ============== #
OPEN_WEATHER_URL    = "https://openweathermap.org/city/"
MEDELLIN_CITY_CODE  = "3674962"

# ===== KEYBOARD LAYOUT ===== #
KEYBOARD_LAYOUT_LATAM = "LATAM"
KEYBOARD_LAYOUT_US    = "US"

CONFIGURED_KEYBOARDS = [KEYBOARD_LAYOUT_LATAM, KEYBOARD_LAYOUT_US]

# ====== WIDGET ICON NAMES ====== #
ICON_NAME_TEMP      = "temp"
ICON_NAME_CPU_SPEED = "cpu_speed"
ICON_NAME_CPU_USAGE = "cpu_usage"
ICON_NAME_DISK      = "disk"
ICON_NAME_MEMORY    = "memory"
ICON_NAME_WEATHER   = "weather"
ICON_NAME_UPDATE    = "update"
ICON_NAME_NET       = "net"
ICON_NAME_VOLUME    = "volume"
ICON_NAME_WINDOWS   = "windows"
ICON_NAME_CLOCK     = "clock"
ICON_NAME_KEYBOARD  = "keyboard"
ICON_NAME_POWER     = "power"

# ========= WIDGET FMTs ========= #
DEFAULT_FMT            = "{}"

FMT_WIDGET_WEATHER      = DEFAULT_FMT
FMT_WIDGET_WEATHER_TEMP = DEFAULT_FMT
FMT_WIDGET_CPU_USAGE    = DEFAULT_FMT
FMT_WIDGET_CPU_SPEED    = DEFAULT_FMT
FMT_WIDGET_TEMP         = DEFAULT_FMT
FMT_WIDGET_DISK         = DEFAULT_FMT
FMT_WIDGET_MEMORY       = DEFAULT_FMT
FMT_WIDGET_NET          = DEFAULT_FMT
FMT_WIDGET_UPDATE_PAC   = DEFAULT_FMT
FMT_WIDGET_UPDATE_AUR   = DEFAULT_FMT
FMT_WIDGET_VOLUME       = DEFAULT_FMT
FMT_WIDGET_WINDOWS      = DEFAULT_FMT
FMT_WIDGET_DATE         = DEFAULT_FMT
FMT_WIDGET_CLOCK        = DEFAULT_FMT
FMT_WIDGET_KEYBOARD     = DEFAULT_FMT

# ====================== WIDGET FORMATS ====================== #
FORMAT_WIDGET_WEATHER      = "{weather}" # "{main_temp:.1f}°{units_temperature}"
FORMAT_WIDGET_WEATHER_TEMP = "{main_temp:.1f}°{units_temperature}" # "{main_temp:.1f}°{units_temperature}"
FORMAT_WIDGET_CPU_USAGE    = "{load_percent}%"
FORMAT_WIDGET_CPU_SPEED    = "{freq_current}GHz"
FORMAT_WIDGET_DISK         = "{r:.1f}%"
FORMAT_WIDGET_MEMORY       = "{MemPercent:.1f}%"
FORMAT_WIDGET_NET_DOWN     = "{down}"
FORMAT_WIDGET_NET_UP       = "{up}"
FORMAT_WIDGET_UPDATE_PAC   = "{updates}"
FORMAT_WIDGET_UPDATE_AUR   = "{updates}"
FORMAT_WIDGET_DATE         = "%d %b"
FORMAT_WIDGET_CLOCK        = "%I:%M %p"

# ============ DEFAULT STRINGS ============ #
DEFAULT_STRING_WIDGET_UPDATE_PAC = "0" #CHAR_EMPTY
DEFAULT_STRING_WIDGET_UPDATE_AUR = "0" #CHAR_EMPTY

# ============= GROUP BOX STYLING ============= #
GROUP_BOX_FONT_COLOR_ACTIVE   = COLOR_FOREGROUND
GROUP_BOX_FONT_COLOR_INACTIVE = COLOR_DARK_GREY
GROUP_BOX_HIGHLIGHT_CURRENT   = COLOR_BLUE
GROUP_BOX_HIGHLIGHT_OTHER     = COLOR_DARK_GREY
GROUP_BOX_HIGHLIGHT_METHOD    = "line"
GROUP_BOX_COLOR_BACKGROUND    = COLOR_BACKGROUND
GROUP_BOX_COLOR_FOREGROUND    = COLOR_FOREGROUND

# =============== WIDGET COLORS =============== #
WIDGET_BACKGROUND_WINDOW_NAME = COLOR_BACKGROUND
WIDGET_BACKGROUND_TEMP        = COLOR_BACKGROUND 
WIDGET_BACKGROUND_CPU_USAGE   = COLOR_BACKGROUND
WIDGET_BACKGROUND_CPU_SPEED   = COLOR_BACKGROUND
WIDGET_BACKGROUND_DISK        = COLOR_BACKGROUND 
WIDGET_BACKGROUND_MEMORY      = COLOR_BACKGROUND 
WIDGET_BACKGROUND_WEATHER     = COLOR_BACKGROUND 
WIDGET_BACKGROUND_UPDATE      = COLOR_BACKGROUND 
WIDGET_BACKGROUND_NET         = COLOR_BACKGROUND 
WIDGET_BACKGROUND_CLOCK       = COLOR_BACKGROUND 
WIDGET_BACKGROUND_VOLUME      = COLOR_BACKGROUND 
WIDGET_BACKGROUND_WINDOWS     = COLOR_BACKGROUND 
WIDGET_BACKGROUND_KEYBOARD    = COLOR_BACKGROUND 
WIDGET_BACKGROUND_POWER       = COLOR_BACKGROUND 

WIDGET_FOREGROUND_SEPARATOR   = COLOR_LIGHT_BLACK
WIDGET_FOREGROUND_WINDOW_NAME = COLOR_FOREGROUND
WIDGET_FOREGROUND_WEATHER     = COLOR_RED
WIDGET_FOREGROUND_TEMP        = COLOR_ORANGE
WIDGET_FOREGROUND_CPU_SPEED   = COLOR_YELLOW
WIDGET_FOREGROUND_CPU_USAGE   = COLOR_GREEN
WIDGET_FOREGROUND_DISK        = COLOR_CYAN
WIDGET_FOREGROUND_MEMORY      = COLOR_BLUE
WIDGET_FOREGROUND_UPDATE      = COLOR_PURPLE
WIDGET_FOREGROUND_NET         = COLOR_BLUE
WIDGET_FOREGROUND_CLOCK       = COLOR_CYAN
WIDGET_FOREGROUND_VOLUME      = COLOR_GREEN
WIDGET_FOREGROUND_WINDOWS     = COLOR_YELLOW
WIDGET_FOREGROUND_KEYBOARD    = COLOR_ORANGE
WIDGET_FOREGROUND_POWER       = COLOR_RED

WIDGET_ALERT_TEMP             = COLOR_LIGHT_RED
WIDGET_ALERT_DISK             = COLOR_LIGHT_YELLOW

LAYOUT_BORDER_COLOR_FOCUSED   = COLOR_BLUE
LAYOUT_BORDER_COLOR           = COLOR_BACKGROUND

# == BAR == #
BAR_SIZE = 22

# ===== THRESHOLDS ===== #
THRESHOLD_WIDGET_TEMP = 80
THRESHOLD_WIDGET_DISK = 200

# ====================== UPDATE INTERVALS ====================== #
WIDGET_UPDATE_INTERVAL_DEFAULT   = 1.0
WIDGET_UPDATE_INTERVAL_TEMP      = WIDGET_UPDATE_INTERVAL_DEFAULT
WIDGET_UPDATE_INTERVAL_CPU       = WIDGET_UPDATE_INTERVAL_DEFAULT
WIDGET_UPDATE_INTERVAL_CPU_SPEED = WIDGET_UPDATE_INTERVAL_DEFAULT
WIDGET_UPDATE_INTERVAL_DISK      = WIDGET_UPDATE_INTERVAL_DEFAULT
WIDGET_UPDATE_INTERVAL_MEMORY    = WIDGET_UPDATE_INTERVAL_DEFAULT
WIDGET_UPDATE_INTERVAL_WEATHER   = 600.0
WIDGET_UPDATE_INTERVAL_NET       = WIDGET_UPDATE_INTERVAL_DEFAULT
WIDGET_UPDATE_INTERVAL_UPDATE    = 1800.0
WIDGET_UPDATE_INTERVAL_VOLUME    = WIDGET_UPDATE_INTERVAL_DEFAULT
WIDGET_UPDATE_INTERVAL_CLOCK     = WIDGET_UPDATE_INTERVAL_DEFAULT
WIDGET_UPDATE_INTERVAL_KEYBOARD  = 10.0

# ============== WIDGET FONT FAMILIES ============== #
FONT_FAMILY_WIDGET_DEFAULT     = "JetBrains Mono bold"
FONT_FAMILY_WIDGET_WINDOW_NAME = "JetBrains"
FONT_FAMILY_WIDGET_GROUP_BOX   = "Ubuntu bold"
FONT_FAMILY_ARROW_SPACER       = "JetBrains Mono"

# ===== WIDGET FONT SIZES ===== #
FONT_SIZE_WIDGET_DEFAULT     = 13
FONT_SIZE_WIDGET_WINDOW_NAME = 13
FONT_SIZE_WIDGET_GROUP_BOX   = 10
FONT_SIZE_ARROW_SPACER       = 21

# == WIDGET PADDING SIZES == #
PADDING_SEPARATOR          = 6 
PADDING_SEPARATOR_SECTION  = 3
PADDING_GROUP_BOX          = 3
PADDING_WIDGET_SYSTRAY     = 5
PADDING_ARROW_SPACER       = 1

# ======= ICON SIZE ======= #
ICON_SIZE_WIDGET_SYSTRAY = 15

# ======== MARGIN SIZE ======== #
MARGIN_SIZE_LAYOUT          = 12
MARGIN_PYTHON_LOGO          = 0

MARGIN_X_GROUP_BOX          = 0
MARGIN_X_WIDGET_IMAGE       = 3
MARGIN_X_WIDGET_IMAGE_POWER = 0

MARGIN_Y_WIDGET_IMAGE       = 2
MARGIN_Y_WIDGET_IMAGE_POWER = 0
MARGIN_Y_GROUP_BOX          = 4

# ==== BORDER SIZE ==== #
BORDER_SIZE_GROUP_BOX = 2
BORDER_SIZE_LAYOUT    = 2

# ====== SEPARATOR ====== #
SIZE_PERCENT_SEPARATOR = 75
LINE_WIDTH_SEPARATOR   = 2

# =========== BOOLS =========== #
SWITCH_WINDOW_WHEN_MOVED = False
SCALE_ICON_DEFAULT       = True
DISABLE_DRAG_GROUP_BOX   = True

# /////////////////////////////////////////////////////////////// FUNCTION DECLARATION /////////////////////////////////////////////////////////////// #

class BarWidget:
    def __init__(self, widget_object, callback = None, icon_name = None, background = None, foreground = None, use_arrow = False):
        self.widget_object = widget_object
        self.callback      = callback
        self.icon_name     = icon_name
        self.use_arrow     = use_arrow
        self.background    = background
        self.foreground    = foreground

def spawn(command):
    return  lambda: qtile.cmd_spawn(command)

def launchTerminalCommand(command, title = None, hold_open = False):
    title = title if title is not None else APP_TERMINAL
    hold_open = TERMINAL_FLAG_HOLD_OPEN if hold_open else CHAR_EMPTY

    modified_command = COMMAND_LAUNCH_IN_TERMINAL_FORMAT.format(APP_TERMINAL, title, hold_open, command)

    return spawn(modified_command)

def getSeparator(line_width, background_color = COLOR_BACKGROUND, foreground_color = WIDGET_FOREGROUND_SEPARATOR):
    return widget.Sep( linewidth    = line_width
                     , padding      = PADDING_SEPARATOR + line_width
                     , size_percent = SIZE_PERCENT_SEPARATOR
                     , background   = background_color
                     , foreground   = foreground_color )

def getWidgetIcon(icon, background_color, callback_function):
    return widget.Image( filename        = PATH_BAR_ICONS_FORMAT.format(icon)
                       , margin_x        = MARGIN_X_WIDGET_IMAGE
                       , margin_y        = MARGIN_Y_WIDGET_IMAGE
                       , scale           = SCALE_ICON_DEFAULT
                       , mouse_callbacks = setMouseCallbacks(callback_function)
                       , background      = background_color )

def getArrowSpacer(color, previous_color):
    return widget.TextBox( text       = CHAR_ARROW
                         , font       = FONT_FAMILY_ARROW_SPACER
                         , fontsize   = FONT_SIZE_ARROW_SPACER 
                         , padding    = PADDING_ARROW_SPACER
                         , background = previous_color
                         , foreground = color )

def getSectionSpacer(background_color):
    return widget.Sep( linewidth    = 0
                     , padding      = PADDING_SEPARATOR_SECTION
                     , size_percent = SIZE_PERCENT_SEPARATOR
                     , background   = background_color
                     , foreground   = COLOR_FOREGROUND )

def getBar(widget_instances_list):
    bar_widgets_array = []
    previous_color = COLOR_BACKGROUND

    for widget in widget_instances_list:
        widget.background = widget.background if widget.background is not None else COLOR_BACKGROUND
        widget.foreground = widget.foreground if widget.foreground is not None else COLOR_FOREGROUND

        if widget.use_arrow: 
            bar_widgets_array.append( getSectionSpacer(widget.background) )
            bar_widgets_array.append( getArrowSpacer(widget.foreground, previous_color) )

        bar_widgets_array.append(widget.widget_object)

        if widget.icon_name is not None: 
            bar_widgets_array.append( getWidgetIcon(widget.icon_name, widget.background, widget.callback) )

        previous_color = widget.background

    return bar_widgets_array

def setMouseCallbacks(left_click_function=None, middle_click_function=None, right_click_function=None):
    return { LEFT_CLICK:   left_click_function
           , MIDDLE_CLICK: middle_click_function
           , RIGHT_CLICK:  right_click_function }

# /////////////////////////////////////////////////////////////////// KEY BINDINGS /////////////////////////////////////////////////////////////////// #

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
       , Key( [KEY_MOD],            KEY_RETURN,           lazy.spawn(APP_TERMINAL) )
       , Key( [KEY_MOD],            KEY_F,                lazy.spawn(APP_FILE_MANAGER) )
       , Key( [KEY_MOD, KEY_SHIFT], KEY_F,                lazy.window.toggle_fullscreen() )
       , Key( [KEY_MOD],            KEY_B,                lazy.spawn(APP_WEB_BROWSER) )
       , Key( [KEY_MOD],            KEY_C,                lazy.spawn(APP_CODE_EDITOR) )
       , Key( [KEY_MOD],            KEY_V,                lazy.spawn(APP_PAVUCONTROL) )
       , Key( [KEY_MOD, KEY_CTRL],  KEY_Q,                lazy.shutdown() )
       , Key( [KEY_MOD, KEY_SHIFT], KEY_Q,                lazy.window.kill() )
       , Key( [KEY_MOD],            KEY_R,                lazy.spawn(APP_ROFI) ) #lazy.spawncmd()
       , Key( [KEY_MOD, KEY_SHIFT], KEY_R,                lazy.restart() )
       , Key( [KEY_MOD],            KEY_T,                lazy.window.toggle_floating() )
       
       # Sound bindings
       , Key( [],                   KEY_XF86_AUDIO_MUTE,  lazy.spawn(COMMAND_VOLUME_MUTE) )
       , Key( [],                   KEY_XF86_AUDIO_LOWER, lazy.spawn(COMMAND_VOLUME_LOWER) )
       , Key( [],                   KEY_XF86_AUDIO_RAISE, lazy.spawn(COMMAND_VOLUME_RAISE) ) ]  

# ////////////////////////////////////////////////////////////////// MOUSE BINDINGS ////////////////////////////////////////////////////////////////// #

mouse = [ Drag(  [KEY_MOD], LEFT_CLICK,   lazy.window.set_position_floating(), start=lazy.window.get_position() )
        , Drag(  [KEY_MOD], RIGHT_CLICK,  lazy.window.set_size_floating(),     start=lazy.window.get_size()     )
        , Click( [KEY_MOD], MIDDLE_CLICK, lazy.window.bring_to_front()                                          ) ]

# ////////////////////////////////////////////////////////////////// GROUP SETTINGS ////////////////////////////////////////////////////////////////// #

groups = [ Group(group, GROUP_DEFAULTS) for group in GROUP_NAMES]

# Bind to groups
for i, _ in enumerate(groups):
    group_name = str( (i + 1) % 10 ) # Mod 10 to make 10 bind to 0

    keys.extend([ Key( [KEY_MOD],            group_name, lazy.group[GROUP_NAMES[i]].toscreen()                  )                          # Switch to group
                , Key( [KEY_MOD, KEY_SHIFT], group_name, lazy.window.togroup(GROUP_NAMES[i], switch_group = SWITCH_WINDOW_WHEN_MOVED) ) ]) # Move focused window to group

# ////////////////////////////////////////////////////////////////////// LAYOUT ////////////////////////////////////////////////////////////////////// #

layout_theme = { "border_width" : BORDER_SIZE_LAYOUT
               , "margin"       : MARGIN_SIZE_LAYOUT
               , "border_focus" : LAYOUT_BORDER_COLOR_FOCUSED
               , "border_normal": LAYOUT_BORDER_COLOR }

layouts = [ layout.MonadTall( **layout_theme )
          , layout.Max( **layout_theme )
          , layout.Matrix( **layout_theme )
          , layout.VerticalTile( **layout_theme )
          , layout.Zoomy( **layout_theme )
          , layout.MonadWide( **layout_theme ) ]

# Try more layouts by unleashing below layouts.
# layout.Columns(border_focus_stack='#d75f5f'),
# layout.Stack(num_stacks=2),
# layout.Bsp(),
# layout.RatioTile(),
# layout.Tile(),
# layout.TreeTab(),

# ///////////////////////////////////////////////////////////////// FLOATING WINDOWS ///////////////////////////////////////////////////////////////// #

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
                , Match( title    = TERMINAL_TITLE_WATCH_SENSORS )
                , Match( title    = TERMINAL_TITLE_WATCH_CPU )
                , Match( title    = TERMINAL_TITLE_WATCH_MEM )
                , Match( wm_class = APP_PAVUCONTROL ) ]

FLOATING_LAYOUT_RULES = layout.Floating( float_rules   = FLOAT_WINDOWS
                                       , border_focus  = COLOR_FOREGROUND
                                       , border_normal = COLOR_BACKGROUND )

# //////////////////////////////////////////////////////////////// WIDGET DEFINITIONS //////////////////////////////////////////////////////////////// #

# ----------------------------------------------------------------- WIDGET CALLBACKS ----------------------------------------------------------------- #

CALLBACK_PYTHON_LOGO       = launchTerminalCommand(APP_PYTHON)
CALLBACK_WIDGET_CPU        = launchTerminalCommand(SCRIPT_WATCH_CPU, TERMINAL_TITLE_WATCH_CPU)
CALLBACK_WIDGET_TEMP       = launchTerminalCommand(SCRIPT_WATCH_SENSORS, TERMINAL_TITLE_WATCH_SENSORS)
CALLBACK_WIDGET_DISK       = spawn(COMMAND_OPEN_ROOT_DIRECTORY)
CALLBACK_WIDGET_MEMORY     = launchTerminalCommand(SCRIPT_WATCH_MEM, TERMINAL_TITLE_WATCH_MEM)
CALLBACK_WIDGET_WEATHER    = spawn(COMMAND_LAUNCH_OPEN_WEATHER_FORMAT.format(APP_WEB_BROWSER, OPEN_WEATHER_URL, MEDELLIN_CITY_CODE))
CALLBACK_WIDGET_NET        = spawn(COMMAND_NOTIFY_NO_CALLBACK)
CALLBACK_WIDGET_UPDATE_PAC = launchTerminalCommand(SCRIPT_MANAGE_UPDATES_PACMAN, TERMINAL_TITLE_PACMAN, False)
CALLBACK_WIDGET_UPDATE_AUR = launchTerminalCommand(SCRIPT_MANAGE_UPDATES_AUR, TERMINAL_TITLE_AUR, False)
CALLBACK_WIDGET_VOLUME     = spawn(APP_PAVUCONTROL)
CALLBACK_WIDGET_WINDOWS    = spawn(COMMAND_NOTIFY_NO_CALLBACK)
CALLBACK_WIDGET_CLOCK      = spawn(COMMAND_NOTIFY_NO_CALLBACK)
CALLBACK_WIDGET_KEYBOARD   = spawn(COMMAND_NOTIFY_NO_CALLBACK)
CALLBACK_WIDGET_POWER      = spawn(SCRIPT_SHUTDOWN_HANDLER)

# ------------------------------------------------------------------ WIDGET OBJECTS ------------------------------------------------------------------ #

separator_widget = getSeparator(LINE_WIDTH_SEPARATOR)
   
python_logo_widget = widget.Image( filename        = PATH_LOGO_PYTHON
                                 , mouse_callbacks = setMouseCallbacks(CALLBACK_PYTHON_LOGO)
                                 , margin          = MARGIN_PYTHON_LOGO
                                 , background      = COLOR_BACKGROUND )
   
group_box_widget = widget.GroupBox( font                        = FONT_FAMILY_WIDGET_GROUP_BOX
                                  , fontsize                    = FONT_SIZE_WIDGET_GROUP_BOX
                                  , margin_x                    = MARGIN_X_GROUP_BOX
                                  , margin_y                    = MARGIN_Y_GROUP_BOX
                                  , padding                     = PADDING_GROUP_BOX
                                  , borderwidth                 = BORDER_SIZE_GROUP_BOX
                                  , disable_drag                = DISABLE_DRAG_GROUP_BOX
                                  , highlight_method            = GROUP_BOX_HIGHLIGHT_METHOD
                                  , highlight_color             = GROUP_BOX_COLOR_BACKGROUND
                                  , active                      = GROUP_BOX_FONT_COLOR_ACTIVE  
                                  , inactive                    = GROUP_BOX_FONT_COLOR_INACTIVE
                                  , this_current_screen_border  = GROUP_BOX_HIGHLIGHT_CURRENT
                                  , this_screen_border          = GROUP_BOX_HIGHLIGHT_OTHER
                                  , other_current_screen_border = GROUP_BOX_HIGHLIGHT_CURRENT
                                  , other_screen_border         = GROUP_BOX_HIGHLIGHT_OTHER
                                  , background                  = GROUP_BOX_COLOR_BACKGROUND
                                  , foreground                  = GROUP_BOX_COLOR_FOREGROUND )
   
window_name_widget = widget.WindowName( font       = FONT_FAMILY_WIDGET_WINDOW_NAME
                                      , fontsize   = FONT_SIZE_WIDGET_WINDOW_NAME
                                      , background = WIDGET_BACKGROUND_WINDOW_NAME
                                      , foreground = WIDGET_FOREGROUND_WINDOW_NAME )

minimal_window_name_widget = widget.WindowName( font       = FONT_FAMILY_WIDGET_WINDOW_NAME
                                              , fontsize   = FONT_SIZE_WIDGET_WINDOW_NAME
                                              , background = WIDGET_BACKGROUND_WINDOW_NAME
                                              , foreground = WIDGET_FOREGROUND_WINDOW_NAME )
   
systray_widget = widget.Systray( padding    = PADDING_WIDGET_SYSTRAY
                               , icon_size  = ICON_SIZE_WIDGET_SYSTRAY
                               , background = COLOR_BACKGROUND
                               , foreground = COLOR_FOREGROUND )

weather_widget = widget.OpenWeather( fmt             = FMT_WIDGET_WEATHER
                                   , format          = FORMAT_WIDGET_WEATHER
                                   , font            = FONT_FAMILY_WIDGET_DEFAULT
                                   , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                   , cityid          = MEDELLIN_CITY_CODE
                                   , update_interval = WIDGET_UPDATE_INTERVAL_WEATHER
                                   , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_WEATHER)
                                   , background      = WIDGET_BACKGROUND_WEATHER
                                   , foreground      = WIDGET_FOREGROUND_WEATHER )

weather_temp_widget = widget.OpenWeather( fmt             = FMT_WIDGET_WEATHER_TEMP
                                        , format          = FORMAT_WIDGET_WEATHER_TEMP
                                        , font            = FONT_FAMILY_WIDGET_DEFAULT
                                        , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                        , cityid          = MEDELLIN_CITY_CODE
                                        , update_interval = WIDGET_UPDATE_INTERVAL_WEATHER
                                        , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_WEATHER)
                                        , background      = WIDGET_BACKGROUND_WEATHER
                                        , foreground      = WIDGET_FOREGROUND_WEATHER )                                  
   
cpu_usage_widget = widget.CPU( fmt             = FMT_WIDGET_CPU_USAGE 
                             , format          = FORMAT_WIDGET_CPU_USAGE
                             , font            = FONT_FAMILY_WIDGET_DEFAULT
                             , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                             , update_interval = WIDGET_UPDATE_INTERVAL_CPU
                             , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_CPU)
                             , background      = WIDGET_BACKGROUND_CPU_USAGE
                             , foreground      = WIDGET_FOREGROUND_CPU_USAGE )

cpu_speed_widget = widget.CPU( fmt             = FMT_WIDGET_CPU_SPEED 
                             , format          = FORMAT_WIDGET_CPU_SPEED 
                             , font            = FONT_FAMILY_WIDGET_DEFAULT
                             , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                             , update_interval = WIDGET_UPDATE_INTERVAL_CPU 
                             , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_CPU)
                             , background      = WIDGET_BACKGROUND_CPU_SPEED 
                             , foreground      = WIDGET_FOREGROUND_CPU_SPEED  )
   
temp_widget = widget.ThermalSensor( fmt              = FMT_WIDGET_TEMP
                                  , font             = FONT_FAMILY_WIDGET_DEFAULT
                                  , fontsize         = FONT_SIZE_WIDGET_DEFAULT
                                  , threshold        = THRESHOLD_WIDGET_TEMP
                                  , update_interval  = WIDGET_UPDATE_INTERVAL_TEMP
                                  , mouse_callbacks  = setMouseCallbacks(CALLBACK_WIDGET_TEMP)
                                  , background       = WIDGET_BACKGROUND_TEMP
                                  , foreground       = WIDGET_FOREGROUND_TEMP
                                  , foreground_alert = WIDGET_ALERT_TEMP )
   
disk_widget = widget.DF( fmt             = FMT_WIDGET_DISK
                       , format          = FORMAT_WIDGET_DISK
                       , font            = FONT_FAMILY_WIDGET_DEFAULT
                       , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                       , warn_space      = THRESHOLD_WIDGET_DISK
                       , warn_color      = WIDGET_ALERT_DISK
                       , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_DISK)
                       , visible_on_warn = False
                       , background      = WIDGET_BACKGROUND_DISK
                       , foreground      = WIDGET_FOREGROUND_DISK )
   
memory_widget = widget.Memory( fmt             = FMT_WIDGET_MEMORY
                             , format          = FORMAT_WIDGET_MEMORY
                             , font            = FONT_FAMILY_WIDGET_DEFAULT
                             , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                             , update_interval = WIDGET_UPDATE_INTERVAL_MEMORY
                             , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_MEMORY)
                             , background      = WIDGET_BACKGROUND_MEMORY
                             , foreground      = WIDGET_FOREGROUND_MEMORY )
   
net_down_widget = widget.Net( fmt             = FMT_WIDGET_NET
                            , format          = FORMAT_WIDGET_NET_DOWN
                            , font            = FONT_FAMILY_WIDGET_DEFAULT
                            , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                            , interface       = LAN_NETWORK_INTERFACE
                            , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_NET)
                            , background      = WIDGET_BACKGROUND_NET
                            , foreground      = WIDGET_FOREGROUND_NET )
   
net_up_widget = widget.Net( fmt             = FMT_WIDGET_NET
                          , format          = FORMAT_WIDGET_NET_UP
                          , font            = FONT_FAMILY_WIDGET_DEFAULT
                          , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                          , interface       = LAN_NETWORK_INTERFACE
                          , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_NET)
                          , background      = WIDGET_BACKGROUND_NET
                          , foreground      = WIDGET_FOREGROUND_NET )
   
update_pac_widget = widget.CheckUpdates( fmt                 = FMT_WIDGET_UPDATE_PAC
                                       , font                = FONT_FAMILY_WIDGET_DEFAULT
                                       , fontsize            = FONT_SIZE_WIDGET_DEFAULT
                                       , display_format      = FORMAT_WIDGET_UPDATE_PAC
                                       , distro              = LINUX_DISTRIBUTION
                                       , no_update_string    = DEFAULT_STRING_WIDGET_UPDATE_PAC
                                       , colour_have_updates = WIDGET_FOREGROUND_UPDATE
                                       , colour_no_updates   = WIDGET_FOREGROUND_UPDATE
                                       , update_interval     = WIDGET_UPDATE_INTERVAL_UPDATE
                                       , custom_command      = COMMAND_UPDATE_PAC_CHECK
                                       , mouse_callbacks     = setMouseCallbacks(CALLBACK_WIDGET_UPDATE_PAC)
                                       , background          = WIDGET_BACKGROUND_UPDATE
                                       , foreground          = WIDGET_FOREGROUND_UPDATE )
   
update_aur_widget = widget.CheckUpdates( fmt                 = FMT_WIDGET_UPDATE_AUR
                                       , font                = FONT_FAMILY_WIDGET_DEFAULT
                                       , fontsize            = FONT_SIZE_WIDGET_DEFAULT
                                       , display_format      = FORMAT_WIDGET_UPDATE_AUR
                                       , distro              = LINUX_DISTRIBUTION
                                       , no_update_string    = DEFAULT_STRING_WIDGET_UPDATE_AUR
                                       , colour_have_updates = WIDGET_FOREGROUND_UPDATE
                                       , colour_no_updates   = WIDGET_FOREGROUND_UPDATE
                                       , update_interval     = WIDGET_UPDATE_INTERVAL_UPDATE
                                       , custom_command      = COMMAND_UPDATE_AUR_CHECK
                                       , mouse_callbacks     = setMouseCallbacks(CALLBACK_WIDGET_UPDATE_AUR)
                                       , background          = WIDGET_BACKGROUND_UPDATE
                                       , foreground          = WIDGET_FOREGROUND_UPDATE )

volume_widget = widget.Volume( fmt             = FMT_WIDGET_VOLUME
                             , font            = FONT_FAMILY_WIDGET_DEFAULT
                             , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                             , volume_app      = APP_PAVUCONTROL
                             , update_interval = WIDGET_UPDATE_INTERVAL_VOLUME
                             , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_VOLUME)
                             , background      = WIDGET_BACKGROUND_VOLUME
                             , foreground      = WIDGET_FOREGROUND_VOLUME )

windows_widget = widget.WindowCount( fmt             = FMT_WIDGET_WINDOWS
                                   , font            = FONT_FAMILY_WIDGET_DEFAULT
                                   , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                   , show_zero       = False
                                   , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_WINDOWS)
                                   , background      = WIDGET_BACKGROUND_WINDOWS
                                   , foreground      = WIDGET_FOREGROUND_WINDOWS )

minimal_windows_widget = widget.WindowCount( fmt             = FMT_WIDGET_WINDOWS
                                           , font            = FONT_FAMILY_WIDGET_DEFAULT
                                           , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                           , show_zero       = False
                                           , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_WINDOWS)
                                           , background      = WIDGET_BACKGROUND_WINDOWS
                                           , foreground      = WIDGET_FOREGROUND_WINDOWS )

date_widget = widget.Clock( fmt             = FMT_WIDGET_DATE
                           , format          = FORMAT_WIDGET_DATE 
                           , font            = FONT_FAMILY_WIDGET_DEFAULT
                           , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                           , update_interval = WIDGET_UPDATE_INTERVAL_CLOCK
                           , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_CLOCK)
                           , background      = WIDGET_BACKGROUND_CLOCK
                           , foreground      = WIDGET_FOREGROUND_CLOCK )

clock_widget = widget.Clock( fmt             = FMT_WIDGET_CLOCK
                           , format          = FORMAT_WIDGET_CLOCK 
                           , font            = FONT_FAMILY_WIDGET_DEFAULT
                           , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                           , update_interval = WIDGET_UPDATE_INTERVAL_CLOCK
                           , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_CLOCK)
                           , background      = WIDGET_BACKGROUND_CLOCK
                           , foreground      = WIDGET_FOREGROUND_CLOCK )

minimal_clock_widget = widget.Clock( fmt             = FMT_WIDGET_CLOCK
                                   , format          = FORMAT_WIDGET_CLOCK
                                   , font            = FONT_FAMILY_WIDGET_DEFAULT
                                   , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                   , update_interval = WIDGET_UPDATE_INTERVAL_CLOCK
                                   , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_CLOCK)
                                   , background      = WIDGET_BACKGROUND_CLOCK
                                   , foreground      = WIDGET_FOREGROUND_CLOCK )

keyboard_widget = widget.KeyboardLayout( fmt                  = FMT_WIDGET_KEYBOARD
                                       , font                 = FONT_FAMILY_WIDGET_DEFAULT
                                       , fontsize             = FONT_SIZE_WIDGET_DEFAULT
                                       , configured_keyboards = CONFIGURED_KEYBOARDS
                                       , update_interval      = WIDGET_UPDATE_INTERVAL_KEYBOARD
                                       , mouse_callbacks      = setMouseCallbacks(CALLBACK_WIDGET_KEYBOARD)
                                       , background           = WIDGET_BACKGROUND_KEYBOARD
                                       , foreground           = WIDGET_FOREGROUND_KEYBOARD )

power_widget = widget.Image( filename        = PATH_BAR_ICONS_FORMAT.format(ICON_NAME_POWER)
                           , margin_x        = MARGIN_X_WIDGET_IMAGE_POWER
                           , margin_y        = MARGIN_Y_WIDGET_IMAGE_POWER
                           , scale           = SCALE_ICON_DEFAULT
                           , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_POWER)
                           , background      = WIDGET_BACKGROUND_POWER
                           , foreground      = WIDGET_FOREGROUND_POWER )

minimal_power_widget = widget.Image( filename        = PATH_BAR_ICONS_FORMAT.format(ICON_NAME_POWER)
                                   , margin_x        = MARGIN_X_WIDGET_IMAGE_POWER
                                   , margin_y        = MARGIN_Y_WIDGET_IMAGE_POWER
                                   , scale           = SCALE_ICON_DEFAULT
                                   , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_POWER)
                                   , background      = WIDGET_BACKGROUND_POWER
                                   , foreground      = WIDGET_FOREGROUND_POWER )

# WIFI
# widget.Wlan( interface            = WIFI_NETWORK_INTERFACE
#            , format               = "{essid} {quality}/70"
#            , disconnected_message = "disconnected" )

# ////////////////////////////////////////////////////////////////// WIDGET LAYOUT ////////////////////////////////////////////////////////////////// #

all_bar_widgets = [ BarWidget( widget_object = python_logo_widget 
                             , callback      = CALLBACK_PYTHON_LOGO ) 
                             
                  , BarWidget( widget_object = separator_widget ) 
                  
                  , BarWidget( widget_object = group_box_widget ) 

                  , BarWidget( widget_object = separator_widget )

                  , BarWidget( widget_object = window_name_widget ) 

                  , BarWidget( widget_object = systray_widget ) 

                  , BarWidget( widget_object = weather_widget
                             , callback      = CALLBACK_WIDGET_WEATHER
                             , icon_name     = ICON_NAME_WEATHER
                             , use_arrow     = True
                             , background    = WIDGET_BACKGROUND_WEATHER
                             , foreground    = WIDGET_FOREGROUND_WEATHER ) 

                  , BarWidget( widget_object = weather_temp_widget
                             , callback      = CALLBACK_WIDGET_WEATHER
                             #, icon_name     = ICON_NAME_WEATHER
                             #, use_arrow     = True
                             , background    = WIDGET_BACKGROUND_WEATHER
                             , foreground    = WIDGET_FOREGROUND_WEATHER ) 

                  , BarWidget( widget_object = temp_widget
                             , callback      = CALLBACK_WIDGET_TEMP
                             , icon_name     = ICON_NAME_TEMP
                             , use_arrow     = True
                             , background    = WIDGET_BACKGROUND_TEMP
                             , foreground    = WIDGET_FOREGROUND_TEMP ) 

                  , BarWidget( widget_object = cpu_speed_widget
                             , callback      = CALLBACK_WIDGET_CPU
                             , icon_name     = ICON_NAME_CPU_SPEED 
                             , use_arrow     = True
                             , background    = WIDGET_BACKGROUND_CPU_SPEED 
                             , foreground    = WIDGET_FOREGROUND_CPU_SPEED ) 

                  , BarWidget( widget_object = cpu_usage_widget
                             , callback      = CALLBACK_WIDGET_CPU
                             , icon_name     = ICON_NAME_CPU_USAGE 
                             , use_arrow     = True
                             , background    = WIDGET_BACKGROUND_CPU_USAGE 
                             , foreground    = WIDGET_FOREGROUND_CPU_USAGE ) 

                  , BarWidget( widget_object = disk_widget
                             , callback      = CALLBACK_WIDGET_DISK
                             , icon_name     = ICON_NAME_DISK
                             , use_arrow     = True
                             , background    = WIDGET_BACKGROUND_DISK
                             , foreground    = WIDGET_FOREGROUND_DISK ) 
                             
                  , BarWidget( widget_object = memory_widget
                             , callback      = CALLBACK_WIDGET_MEMORY
                             , icon_name     = ICON_NAME_MEMORY
                             , use_arrow     = True
                             , background    = WIDGET_BACKGROUND_MEMORY
                             , foreground    = WIDGET_FOREGROUND_MEMORY )
                              
                  , BarWidget( widget_object = update_pac_widget
                             , callback      = CALLBACK_WIDGET_UPDATE_PAC
                             , icon_name     = ICON_NAME_UPDATE
                             , use_arrow     = True
                             , background    = WIDGET_BACKGROUND_UPDATE
                             , foreground    = WIDGET_FOREGROUND_UPDATE ) 

                  , BarWidget( widget_object = update_aur_widget
                             , callback      = CALLBACK_WIDGET_UPDATE_AUR
                             , background    = WIDGET_BACKGROUND_UPDATE
                             , foreground    = WIDGET_FOREGROUND_UPDATE ) 

                  , BarWidget( widget_object = net_up_widget
                             , callback      = CALLBACK_WIDGET_NET
                             , icon_name     = ICON_NAME_NET
                             , use_arrow     = True
                             , background    = WIDGET_BACKGROUND_NET
                             , foreground    = WIDGET_FOREGROUND_NET ) 
                             
                  , BarWidget( widget_object = net_down_widget
                             , callback      = CALLBACK_WIDGET_NET
                             , background    = WIDGET_BACKGROUND_NET
                             , foreground    = WIDGET_FOREGROUND_NET )

                  , BarWidget( widget_object = date_widget
                             , callback      = CALLBACK_WIDGET_CLOCK
                             , icon_name     = ICON_NAME_CLOCK
                             , use_arrow     = True
                             , background    = WIDGET_BACKGROUND_CLOCK
                             , foreground    = WIDGET_FOREGROUND_CLOCK )

                  , BarWidget( widget_object = clock_widget
                             , callback      = CALLBACK_WIDGET_CLOCK
                             #, icon_name     = ICON_NAME_CLOCK
                             #, use_arrow     = True
                             , background    = WIDGET_BACKGROUND_CLOCK
                             , foreground    = WIDGET_FOREGROUND_CLOCK )

                  , BarWidget( widget_object = volume_widget
                             , callback      = CALLBACK_WIDGET_VOLUME
                             , icon_name     = ICON_NAME_VOLUME
                             , use_arrow     = True
                             , background    = WIDGET_BACKGROUND_VOLUME
                             , foreground    = WIDGET_FOREGROUND_VOLUME )

                  , BarWidget( widget_object = windows_widget
                             , callback      = CALLBACK_WIDGET_WINDOWS
                             , icon_name     = ICON_NAME_WINDOWS 
                             , use_arrow     = True
                             , background    = WIDGET_BACKGROUND_WINDOWS
                             , foreground    = WIDGET_FOREGROUND_WINDOWS ) 
                             
                  , BarWidget( widget_object = keyboard_widget
                             , callback      = CALLBACK_WIDGET_KEYBOARD
                             , icon_name     = ICON_NAME_KEYBOARD
                             , use_arrow     = True
                             , background    = WIDGET_BACKGROUND_KEYBOARD
                             , foreground    = WIDGET_FOREGROUND_KEYBOARD )
   
                  , BarWidget( widget_object = power_widget
                             , callback      = CALLBACK_WIDGET_POWER
                             , use_arrow     = True
                             , background    = WIDGET_BACKGROUND_POWER
                             , foreground    = WIDGET_FOREGROUND_POWER ) ]

minimal_bar_widgets = [ BarWidget( widget_object = python_logo_widget 
                                 , callback      = CALLBACK_PYTHON_LOGO ) 
                             
                      , BarWidget( widget_object = separator_widget ) 
                      
                      , BarWidget( widget_object = group_box_widget ) 
    
                      , BarWidget( widget_object = separator_widget )

                      , BarWidget( widget_object = minimal_window_name_widget )

                      , BarWidget( widget_object = minimal_clock_widget
                                 , callback      = CALLBACK_WIDGET_CLOCK
                                 , icon_name     = ICON_NAME_CLOCK
                                 , use_arrow     = True
                                 , background    = WIDGET_BACKGROUND_CLOCK
                                 , foreground    = WIDGET_FOREGROUND_CLOCK ) 

                      , BarWidget( widget_object = volume_widget
                                 , callback      = CALLBACK_WIDGET_VOLUME
                                 , icon_name     = ICON_NAME_VOLUME
                                 , use_arrow     = True
                                 , background    = WIDGET_BACKGROUND_VOLUME
                                 , foreground    = WIDGET_FOREGROUND_VOLUME )
    
                      , BarWidget( widget_object = minimal_windows_widget
                                 , callback      = CALLBACK_WIDGET_WINDOWS
                                 , icon_name     = ICON_NAME_WINDOWS
                                 , use_arrow     = True
                                 , background    = WIDGET_BACKGROUND_WINDOWS
                                 , foreground    = WIDGET_FOREGROUND_WINDOWS ) 
    
                      , BarWidget( widget_object = keyboard_widget
                                 , callback      = CALLBACK_WIDGET_KEYBOARD
                                 , icon_name     = ICON_NAME_KEYBOARD
                                 , use_arrow     = True
                                 , background    = WIDGET_BACKGROUND_KEYBOARD
                                 , foreground    = WIDGET_FOREGROUND_KEYBOARD )
                                   
                      , BarWidget( widget_object = minimal_power_widget
                                 , callback      = CALLBACK_WIDGET_POWER
                                 , use_arrow     = True
                                 , background    = WIDGET_BACKGROUND_POWER
                                 , foreground    = WIDGET_FOREGROUND_POWER ) ]

# ///////////////////////////////////////////////////////////////// SCREEN SETTINGS ///////////////////////////////////////////////////////////////// #

screen_0_bar = getBar(all_bar_widgets)
screen_1_bar = getBar(minimal_bar_widgets)

screen_0     = Screen( top = bar.Bar( screen_0_bar
                                       , BAR_SIZE
                                       , opacity    = 1
                                       , margin     = [-2, 0, 0, 0]
                                       , background = COLOR_BACKGROUND ) )

screen_1     = Screen( top    = bar.Bar( screen_1_bar
                                       , BAR_SIZE
                                       , opacity    = 1
                                       , background = COLOR_BACKGROUND ) )

screens      = [ screen_0
               , screen_1 ]

# ////////////////////////////////////////////////////////////////// STARTUP HOOKS ////////////////////////////////////////////////////////////////// #

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# ////////////////////////////////////////////////////////////////// OTHER SETTINGS ////////////////////////////////////////////////////////////////// #

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
