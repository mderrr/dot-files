import os
import subprocess
#from typing import List  # noqa: F401
from libqtile import bar, layout, widget, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# //////////////////////////////////////////////////////////// VARIABLE DECLARATIONS //////////////////////////////////////////////////////////// #

# ============= COLORS ============= #
COLOR_RED          = "#bf616a" 
COLOR_ORANGE       = "#d19a66" 
COLOR_YELLOW       = "#ebcb8b"
COLOR_GREEN        = "#a3be8c"
COLOR_CYAN         = "#88c0d0" 
COLOR_BLUE         = "#81a1c1"
COLOR_PURPLE       = "#b48ead"
COLOR_LIGHT_RED    = "#c6727a"
COLOR_LIGHT_YELLOW = "#edd198"
COLOR_DARK_WHITE   = "#abb2bf"
COLOR_WHITE        = "#e5e9f0"
COLOR_DARK_GREY    = "#3b4252"
COLOR_GREY         = "#434c5e"
COLOR_LIGHT_GREY   = "#4c566a"
COLOR_BLACK        = "#2e3440"
COLOR_LIGHT_BLACK  = "#4c566a"

COLOR_BACKGROUND   = COLOR_BLACK
COLOR_FOREGROUND   = COLOR_WHITE

# === CHARACTERS === #
CHAR_SLOPE = "\u25e2"
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

# ============= LAYOUT ============= #
LAYOUT_NAME_VERTICAL  = "verticaltile"
LAYOUT_NAME_MONADTALL = "monadtall"
LAYOUT_NAME_MAX       = "max"

# =================== CLIENT TITLES =================== #
CLIENT_TITLE_GIMP      = "GNU Image Manipulation Program"
CLIENT_TITLE_CODE      = "Visual Studio Code"
CLIENT_TITLE_FIREFOX   = "Mozilla Firefox"
CLIENT_TITLE_ALACRITTY = "Alacritty"

# =================================== GROUPS =================================== #
GROUP_NAMES = [ "MAIN", "SYS", "DEV", "WEB", "GFX", "6", "7", "8", "DOCS", "TV" ]

GROUP_LAYOUTS = { GROUP_NAMES[0]: LAYOUT_NAME_MONADTALL
                , GROUP_NAMES[1]: LAYOUT_NAME_MONADTALL
                , GROUP_NAMES[2]: LAYOUT_NAME_MONADTALL
                , GROUP_NAMES[3]: LAYOUT_NAME_MONADTALL
                , GROUP_NAMES[4]: LAYOUT_NAME_MONADTALL
                , GROUP_NAMES[5]: LAYOUT_NAME_MONADTALL
                , GROUP_NAMES[6]: LAYOUT_NAME_MONADTALL
                , GROUP_NAMES[7]: LAYOUT_NAME_MONADTALL
                , GROUP_NAMES[8]: LAYOUT_NAME_VERTICAL
                , GROUP_NAMES[9]: LAYOUT_NAME_MAX } 

GROUP_MATCHES = { GROUP_NAMES[2]: [CLIENT_TITLE_CODE]
                , GROUP_NAMES[3]: [CLIENT_TITLE_FIREFOX]
                , GROUP_NAMES[4]: [CLIENT_TITLE_GIMP] }

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
ICON_NAME_CPU       = "cpu"
ICON_NAME_DISK      = "disk"
ICON_NAME_MEMORY    = "memory"
ICON_NAME_WEATHER   = "weather"
ICON_NAME_UPDATE    = "update"
ICON_NAME_NET       = "net"
ICON_NAME_VOLUME    = "volume"
ICON_NAME_CLOCK     = "date"
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
FORMAT_WIDGET_WEATHER      = "{weather}"
FORMAT_WIDGET_WEATHER_TEMP = "{main_temp:.1f}°{units_temperature}"
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
DEFAULT_STRING_WIDGET_UPDATE_PAC = "0" # CHAR_EMPTY
DEFAULT_STRING_WIDGET_UPDATE_AUR = "0" # CHAR_EMPTY

TAG_SENSOR = "Tdie"

# ============= GROUP BOX STYLING ============= #
GROUP_BOX_FONT_COLOR_ACTIVE   = COLOR_FOREGROUND
GROUP_BOX_FONT_COLOR_INACTIVE = COLOR_LIGHT_BLACK
GROUP_BOX_HIGHLIGHT_CURRENT   = COLOR_CYAN
GROUP_BOX_HIGHLIGHT_OTHER     = COLOR_LIGHT_BLACK
GROUP_BOX_HIGHLIGHT_METHOD    = "line"
GROUP_BOX_COLOR_BACKGROUND    = COLOR_BACKGROUND
GROUP_BOX_COLOR_FOREGROUND    = COLOR_FOREGROUND

# ============== WINDOW COLORS ============== #
LAYOUT_BORDER_COLOR         = COLOR_GREY
LAYOUT_BORDER_COLOR_FOCUSED = COLOR_BACKGROUND # COLOR_CYAN

# =============== WIDGET COLORS =============== #
WIDGET_BACKGROUND_WINDOW_NAME = COLOR_BACKGROUND

WIDGET_BACKGROUND_VOLUME      = COLOR_DARK_GREY
WIDGET_BACKGROUND_WINDOWS     = COLOR_GREY
WIDGET_BACKGROUND_KEYBOARD    = COLOR_LIGHT_GREY
WIDGET_BACKGROUND_CPU         = COLOR_RED
WIDGET_BACKGROUND_DISK        = COLOR_ORANGE
WIDGET_BACKGROUND_MEMORY      = COLOR_YELLOW
WIDGET_BACKGROUND_UPDATE      = COLOR_GREEN
WIDGET_BACKGROUND_NET         = COLOR_CYAN
WIDGET_BACKGROUND_CLOCK       = COLOR_BLUE
WIDGET_BACKGROUND_WEATHER     = COLOR_PURPLE
WIDGET_BACKGROUND_POWER       = COLOR_RED

WIDGET_FOREGROUND_SEPARATOR   = COLOR_LIGHT_BLACK
WIDGET_FOREGROUND_WINDOW_NAME = COLOR_FOREGROUND
WIDGET_FOREGROUND_VOLUME      = COLOR_DARK_WHITE
WIDGET_FOREGROUND_WINDOWS     = COLOR_DARK_WHITE
WIDGET_FOREGROUND_KEYBOARD    = COLOR_DARK_WHITE
WIDGET_FOREGROUND_CPU         = COLOR_BACKGROUND
WIDGET_FOREGROUND_DISK        = COLOR_BACKGROUND
WIDGET_FOREGROUND_MEMORY      = COLOR_BACKGROUND
WIDGET_FOREGROUND_UPDATE      = COLOR_BACKGROUND
WIDGET_FOREGROUND_NET         = COLOR_BACKGROUND
WIDGET_FOREGROUND_CLOCK       = COLOR_BACKGROUND
WIDGET_FOREGROUND_WEATHER     = COLOR_BACKGROUND
WIDGET_FOREGROUND_POWER       = COLOR_FOREGROUND

WIDGET_ALERT_TEMP             = COLOR_LIGHT_RED
WIDGET_ALERT_DISK             = COLOR_LIGHT_YELLOW

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
FONT_SIZE_WIDGET_WINDOW_NAME = 14
FONT_SIZE_WIDGET_GROUP_BOX   = 10
FONT_SIZE_SLOPE_SPACER       = 31

# == WIDGET PADDING SIZES == #
PADDING_SEPARATOR          = 6 
PADDING_SEPARATOR_SECTION  = 3
PADDING_GROUP_BOX          = 3
PADDING_WIDGET_SYSTRAY     = 5
PADDING_SLOPE_SPACER       = -5
PADDING_LAYOUT_ICON        = -1

# ======= ICON SIZE ======= #
ICON_SIZE_WIDGET_SYSTRAY = 15

# ======== MARGIN SIZE ======== #
MARGIN_SIZE_LAYOUT          = 30
MARGIN_PYTHON_LOGO          = 0

MARGIN_X_GROUP_BOX          = 0
MARGIN_X_WIDGET_IMAGE       = 3
MARGIN_X_WIDGET_IMAGE_POWER = 0

MARGIN_Y_WIDGET_IMAGE       = 2
MARGIN_Y_WIDGET_IMAGE_POWER = 0
MARGIN_Y_GROUP_BOX          = 3

# ==== BORDER SIZE ==== #
BORDER_SIZE_GROUP_BOX = 2
BORDER_SIZE_LAYOUT    = 2

# ====== SEPARATOR ====== #
SIZE_PERCENT_SEPARATOR = 75
LINE_WIDTH_SEPARATOR   = 2

# ====== SCALE ====== #
ICON_SCALE_LAYOUT = 0.5

# =========== BOOLS =========== #
SWITCH_WINDOW_WHEN_MOVED = False
SCALE_ICON_DEFAULT       = True
DISABLE_DRAG_GROUP_BOX   = True
SHOW_ZERO_WINDOWS        = True

# ////////////////////////////////////////////////////////////// FUNCTION DECLARATION ////////////////////////////////////////////////////////////// #

class BarWidget:
    def __init__(self, widget_object, callback = None, icon_name = None, background = None, foreground = None, use_arrow = None):
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

def getSlopeSpacer(color, previous_color):
    return widget.TextBox( text       = CHAR_SLOPE
                         , font       = FONT_FAMILY_ARROW_SPACER
                         , fontsize   = FONT_SIZE_SLOPE_SPACER 
                         , padding    = PADDING_SLOPE_SPACER
                         , background = previous_color
                         , foreground = color )

def getBar(widget_instances_list):
    bar_widgets_array = []
    previous_color = COLOR_BACKGROUND

    for widget in widget_instances_list:
        widget.background = widget.background if widget.background is not None else COLOR_BACKGROUND
        widget.foreground = widget.foreground if widget.foreground is not None else COLOR_FOREGROUND

        if widget.use_arrow is not None: 
            bar_widgets_array.append( getSlopeSpacer(widget.background, previous_color) )

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

#        [ Mod ]         [ Key ]    [ Action ]
keys = [ Key( [KEY_MOD], KEY_H,     lazy.layout.up()    )
       , Key( [KEY_MOD], KEY_L,     lazy.layout.down()  )
       , Key( [KEY_MOD], KEY_J,     lazy.layout.left()  )
       , Key( [KEY_MOD], KEY_K,     lazy.layout.right() )
       , Key( [KEY_MOD], KEY_SPACE, lazy.layout.next()  )
       , Key( [KEY_MOD], KEY_TAB,   lazy.next_layout()  )
                       
       , Key( [KEY_MOD, KEY_SHIFT], KEY_H,      lazy.layout.shuffle_up()    )
       , Key( [KEY_MOD, KEY_SHIFT], KEY_L,      lazy.layout.shuffle_down()  )
       , Key( [KEY_MOD, KEY_SHIFT], KEY_J,      lazy.layout.shuffle_left()  )
       , Key( [KEY_MOD, KEY_SHIFT], KEY_K,      lazy.layout.shuffle_right() )
       , Key( [KEY_MOD, KEY_SHIFT], KEY_RETURN, lazy.layout.toggle_split()  )
                       
       , Key( [KEY_MOD, KEY_CTRL], KEY_J, lazy.layout.grow_left()  )
       , Key( [KEY_MOD, KEY_CTRL], KEY_K, lazy.layout.grow_right() )
       , Key( [KEY_MOD, KEY_CTRL], KEY_H, lazy.layout.grow_down()  )
       , Key( [KEY_MOD, KEY_CTRL], KEY_L, lazy.layout.grow_up()    )
       , Key( [KEY_MOD, KEY_CTRL], KEY_N, lazy.layout.normalize()  )

       # My bindings               
       , Key( [KEY_MOD], KEY_RETURN, lazy.spawn(APP_TERMINAL)      )
       , Key( [KEY_MOD], KEY_F,      lazy.spawn(APP_FILE_MANAGER)  )
       , Key( [KEY_MOD], KEY_B,      lazy.spawn(APP_WEB_BROWSER)   )
       , Key( [KEY_MOD], KEY_C,      lazy.spawn(APP_CODE_EDITOR)   )
       , Key( [KEY_MOD], KEY_V,      lazy.spawn(APP_PAVUCONTROL)   )
       , Key( [KEY_MOD], KEY_T,      lazy.window.toggle_floating() )
       , Key( [KEY_MOD], KEY_R,      lazy.spawn(APP_ROFI)          )

       , Key( [KEY_MOD, KEY_CTRL],  KEY_Q, lazy.shutdown() )
       
       , Key( [KEY_MOD, KEY_SHIFT], KEY_Q, lazy.window.kill()              )
       , Key( [KEY_MOD, KEY_SHIFT], KEY_F, lazy.window.toggle_fullscreen() )
       , Key( [KEY_MOD, KEY_SHIFT], KEY_R, lazy.restart()                  )
       
       # Sound bindings
       , Key( [], KEY_XF86_AUDIO_MUTE,  lazy.spawn(COMMAND_VOLUME_MUTE)  )
       , Key( [], KEY_XF86_AUDIO_LOWER, lazy.spawn(COMMAND_VOLUME_LOWER) )
       , Key( [], KEY_XF86_AUDIO_RAISE, lazy.spawn(COMMAND_VOLUME_RAISE) ) ]  

# ////////////////////////////////////////////////////////////////// MOUSE BINDINGS ////////////////////////////////////////////////////////////////// #

mouse = [ Drag(  [KEY_MOD], LEFT_CLICK,   lazy.window.set_position_floating(), start=lazy.window.get_position() )
        , Drag(  [KEY_MOD], RIGHT_CLICK,  lazy.window.set_size_floating(),     start=lazy.window.get_size()     )
        , Click( [KEY_MOD], MIDDLE_CLICK, lazy.window.bring_to_front()                                          ) ]

# ////////////////////////////////////////////////////////////////// GROUP SETTINGS ////////////////////////////////////////////////////////////////// #

groups = []

for i, group_name in enumerate(GROUP_NAMES):
    group_number = str( (i + 1) % 10 ) 

    groups.append( Group(group_name, layout = GROUP_LAYOUTS[group_name]) )

    keys.extend( [ Key( [KEY_MOD],            group_number, lazy.group[group_name].toscreen(toggle = False) ) 
                 , Key( [KEY_MOD, KEY_SHIFT], group_number, lazy.window.togroup(group_name, switch_group = SWITCH_WINDOW_WHEN_MOVED) ) ] )

@hook.subscribe.client_new
def func(client):
    for group_name in GROUP_MATCHES:
        for match in GROUP_MATCHES[group_name]:
            if client.name == match:
                client.togroup(group_name)
                qtile.groups_map[group_name].cmd_toscreen(toggle = False)

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

separator_widget = BarWidget( widget_object = getSeparator(LINE_WIDTH_SEPARATOR) )
   
python_logo_widget = BarWidget( callback      = CALLBACK_PYTHON_LOGO
                              , widget_object = widget.Image( filename        = PATH_LOGO_PYTHON
                                                            , mouse_callbacks = setMouseCallbacks(CALLBACK_PYTHON_LOGO)
                                                            , margin          = MARGIN_PYTHON_LOGO
                                                            , background      = COLOR_BACKGROUND ) )
   
group_box_widget = BarWidget( widget_object = widget.GroupBox( font                        = FONT_FAMILY_WIDGET_GROUP_BOX
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
                                                             , foreground                  = GROUP_BOX_COLOR_FOREGROUND ) )
   
window_name_widget = BarWidget( widget_object = widget.WindowName( font       = FONT_FAMILY_WIDGET_WINDOW_NAME
                                                                 , fontsize   = FONT_SIZE_WIDGET_WINDOW_NAME
                                                                 , background = WIDGET_BACKGROUND_WINDOW_NAME
                                                                 , foreground = WIDGET_FOREGROUND_WINDOW_NAME ) )

# Because size will change equally in both screens
window_name_widget_alt = BarWidget( widget_object = widget.WindowName( font       = FONT_FAMILY_WIDGET_WINDOW_NAME
                                                                     , fontsize   = FONT_SIZE_WIDGET_WINDOW_NAME
                                                                     , background = WIDGET_BACKGROUND_WINDOW_NAME
                                                                     , foreground = WIDGET_FOREGROUND_WINDOW_NAME ) )

systray_widget = BarWidget( widget_object = widget.Systray( padding    = PADDING_WIDGET_SYSTRAY
                                                          , icon_size  = ICON_SIZE_WIDGET_SYSTRAY
                                                          , background = COLOR_BACKGROUND
                                                          , foreground = COLOR_FOREGROUND ) ) 

temp_widget = BarWidget( callback      = CALLBACK_WIDGET_TEMP
                       , icon_name     = ICON_NAME_TEMP
                       , use_arrow     = True
                       , background    = WIDGET_BACKGROUND_CPU
                       , foreground    = WIDGET_FOREGROUND_CPU
                       , widget_object = widget.ThermalSensor( fmt              = FMT_WIDGET_TEMP
                                                             , font             = FONT_FAMILY_WIDGET_DEFAULT
                                                             , fontsize         = FONT_SIZE_WIDGET_DEFAULT
                                                             , threshold        = THRESHOLD_WIDGET_TEMP
                                                             , update_interval  = WIDGET_UPDATE_INTERVAL_TEMP
                                                             , tag_sensor       = TAG_SENSOR
                                                             , mouse_callbacks  = setMouseCallbacks(CALLBACK_WIDGET_TEMP)
                                                             , background       = WIDGET_BACKGROUND_CPU
                                                             , foreground       = WIDGET_FOREGROUND_CPU
                                                             , foreground_alert = WIDGET_ALERT_TEMP ) )

cpu_speed_widget = BarWidget( callback      = CALLBACK_WIDGET_CPU
                            , icon_name     = ICON_NAME_CPU
                            , background    = WIDGET_BACKGROUND_CPU 
                            , foreground    = WIDGET_FOREGROUND_CPU
                            , widget_object = widget.CPU( fmt             = FMT_WIDGET_CPU_SPEED 
                                                        , format          = FORMAT_WIDGET_CPU_SPEED 
                                                        , font            = FONT_FAMILY_WIDGET_DEFAULT
                                                        , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                                        , update_interval = WIDGET_UPDATE_INTERVAL_CPU 
                                                        , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_CPU)
                                                        , background      = WIDGET_BACKGROUND_CPU 
                                                        , foreground      = WIDGET_FOREGROUND_CPU ) )

cpu_usage_widget = BarWidget( callback      = CALLBACK_WIDGET_CPU
                            , background    = WIDGET_BACKGROUND_CPU 
                            , foreground    = WIDGET_FOREGROUND_CPU
                            , widget_object = widget.CPU( fmt             = FMT_WIDGET_CPU_USAGE 
                                                        , format          = FORMAT_WIDGET_CPU_USAGE
                                                        , font            = FONT_FAMILY_WIDGET_DEFAULT
                                                        , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                                        , update_interval = WIDGET_UPDATE_INTERVAL_CPU
                                                        , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_CPU)
                                                        , background      = WIDGET_BACKGROUND_CPU
                                                        , foreground      = WIDGET_FOREGROUND_CPU ) ) 

disk_widget = BarWidget( callback      = CALLBACK_WIDGET_DISK
                       , icon_name     = ICON_NAME_DISK
                       , use_arrow     = True
                       , background    = WIDGET_BACKGROUND_DISK
                       , foreground    = WIDGET_FOREGROUND_DISK 
                       , widget_object = widget.DF( fmt             = FMT_WIDGET_DISK
                                                  , format          = FORMAT_WIDGET_DISK
                                                  , font            = FONT_FAMILY_WIDGET_DEFAULT
                                                  , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                                  , warn_space      = THRESHOLD_WIDGET_DISK
                                                  , warn_color      = WIDGET_ALERT_DISK
                                                  , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_DISK)
                                                  , visible_on_warn = False
                                                  , background      = WIDGET_BACKGROUND_DISK
                                                  , foreground      = WIDGET_FOREGROUND_DISK ) )

memory_widget = BarWidget( callback      = CALLBACK_WIDGET_MEMORY
                         , icon_name     = ICON_NAME_MEMORY
                         , use_arrow     = True
                         , background    = WIDGET_BACKGROUND_MEMORY
                         , foreground    = WIDGET_FOREGROUND_MEMORY
                         , widget_object = widget.Memory( fmt             = FMT_WIDGET_MEMORY
                                                        , format          = FORMAT_WIDGET_MEMORY
                                                        , font            = FONT_FAMILY_WIDGET_DEFAULT
                                                        , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                                        , update_interval = WIDGET_UPDATE_INTERVAL_MEMORY
                                                        , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_MEMORY)
                                                        , background      = WIDGET_BACKGROUND_MEMORY
                                                        , foreground      = WIDGET_FOREGROUND_MEMORY ) )

update_pac_widget = BarWidget( callback      = CALLBACK_WIDGET_UPDATE_PAC
                             , icon_name     = ICON_NAME_UPDATE
                             , use_arrow     = True
                             , background    = WIDGET_BACKGROUND_UPDATE
                             , foreground    = WIDGET_FOREGROUND_UPDATE
                             , widget_object = widget.CheckUpdates( fmt                 = FMT_WIDGET_UPDATE_PAC
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
                                                                  , foreground          = WIDGET_FOREGROUND_UPDATE ) ) 

update_aur_widget = BarWidget( callback      = CALLBACK_WIDGET_UPDATE_AUR
                             , background    = WIDGET_BACKGROUND_UPDATE
                             , foreground    = WIDGET_FOREGROUND_UPDATE
                             , widget_object = widget.CheckUpdates( fmt                 = FMT_WIDGET_UPDATE_AUR
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
                                                                  , foreground          = WIDGET_FOREGROUND_UPDATE ) ) 

net_up_widget = BarWidget( callback      = CALLBACK_WIDGET_NET
                         , icon_name     = ICON_NAME_NET
                         , use_arrow     = True
                         , background    = WIDGET_BACKGROUND_NET
                         , foreground    = WIDGET_FOREGROUND_NET
                         , widget_object = widget.Net( fmt             = FMT_WIDGET_NET
                                                     , format          = FORMAT_WIDGET_NET_UP
                                                     , font            = FONT_FAMILY_WIDGET_DEFAULT
                                                     , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                                     , interface       = LAN_NETWORK_INTERFACE
                                                     , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_NET)
                                                     , background      = WIDGET_BACKGROUND_NET
                                                     , foreground      = WIDGET_FOREGROUND_NET ) ) 

net_down_widget = BarWidget( callback      = CALLBACK_WIDGET_NET
                           , background    = WIDGET_BACKGROUND_NET
                           , foreground    = WIDGET_FOREGROUND_NET
                           , widget_object = widget.Net( fmt             = FMT_WIDGET_NET
                                                       , format          = FORMAT_WIDGET_NET_DOWN
                                                       , font            = FONT_FAMILY_WIDGET_DEFAULT
                                                       , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                                       , interface       = LAN_NETWORK_INTERFACE
                                                       , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_NET)
                                                       , background      = WIDGET_BACKGROUND_NET
                                                       , foreground      = WIDGET_FOREGROUND_NET ) )

date_widget = BarWidget( callback      = CALLBACK_WIDGET_CLOCK
                       , icon_name     = ICON_NAME_CLOCK
                       , use_arrow     = True
                       , background    = WIDGET_BACKGROUND_CLOCK
                       , foreground    = WIDGET_FOREGROUND_CLOCK
                       , widget_object = widget.Clock( fmt             = FMT_WIDGET_DATE
                                                     , format          = FORMAT_WIDGET_DATE 
                                                     , font            = FONT_FAMILY_WIDGET_DEFAULT
                                                     , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                                     , update_interval = WIDGET_UPDATE_INTERVAL_CLOCK
                                                     , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_CLOCK)
                                                     , background      = WIDGET_BACKGROUND_CLOCK
                                                     , foreground      = WIDGET_FOREGROUND_CLOCK ) )

clock_widget = BarWidget( callback      = CALLBACK_WIDGET_CLOCK
                        , background    = WIDGET_BACKGROUND_CLOCK
                        , foreground    = WIDGET_FOREGROUND_CLOCK
                        , widget_object = widget.Clock( fmt             = FMT_WIDGET_CLOCK
                                                      , format          = FORMAT_WIDGET_CLOCK 
                                                      , font            = FONT_FAMILY_WIDGET_DEFAULT
                                                      , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                                      , update_interval = WIDGET_UPDATE_INTERVAL_CLOCK
                                                      , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_CLOCK)
                                                      , background      = WIDGET_BACKGROUND_CLOCK
                                                      , foreground      = WIDGET_FOREGROUND_CLOCK ) ) 

weather_widget = BarWidget( callback      = CALLBACK_WIDGET_WEATHER
                          , icon_name     = ICON_NAME_WEATHER
                          , use_arrow     = True
                          , background    = WIDGET_BACKGROUND_WEATHER
                          , foreground    = WIDGET_FOREGROUND_WEATHER 
                          , widget_object = widget.OpenWeather( fmt             = FMT_WIDGET_WEATHER
                                                              , format          = FORMAT_WIDGET_WEATHER
                                                              , font            = FONT_FAMILY_WIDGET_DEFAULT
                                                              , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                                              , cityid          = MEDELLIN_CITY_CODE
                                                              , update_interval = WIDGET_UPDATE_INTERVAL_WEATHER
                                                              , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_WEATHER)
                                                              , background      = WIDGET_BACKGROUND_WEATHER
                                                              , foreground      = WIDGET_FOREGROUND_WEATHER ) )
                                                              
weather_temp_widget = BarWidget( callback      = CALLBACK_WIDGET_WEATHER
                               , background    = WIDGET_BACKGROUND_WEATHER
                               , foreground    = WIDGET_FOREGROUND_WEATHER 
                               , widget_object = widget.OpenWeather( fmt             = FMT_WIDGET_WEATHER_TEMP
                                                                   , format          = FORMAT_WIDGET_WEATHER_TEMP
                                                                   , font            = FONT_FAMILY_WIDGET_DEFAULT
                                                                   , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                                                   , cityid          = MEDELLIN_CITY_CODE
                                                                   , update_interval = WIDGET_UPDATE_INTERVAL_WEATHER
                                                                   , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_WEATHER)
                                                                   , background      = WIDGET_BACKGROUND_WEATHER
                                                                   , foreground      = WIDGET_FOREGROUND_WEATHER ) )   

volume_widget = BarWidget( callback      = CALLBACK_WIDGET_VOLUME
                         , icon_name     = ICON_NAME_VOLUME
                         , use_arrow     = True
                         , background    = WIDGET_BACKGROUND_VOLUME
                         , foreground    = WIDGET_FOREGROUND_VOLUME
                         , widget_object = widget.Volume( fmt             = FMT_WIDGET_VOLUME
                                                        , font            = FONT_FAMILY_WIDGET_DEFAULT
                                                        , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                                        , volume_app      = APP_PAVUCONTROL
                                                        , update_interval = WIDGET_UPDATE_INTERVAL_VOLUME
                                                        , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_VOLUME)
                                                        , background      = WIDGET_BACKGROUND_VOLUME
                                                        , foreground      = WIDGET_FOREGROUND_VOLUME ) )

windows_widget = BarWidget( callback      = CALLBACK_WIDGET_WINDOWS
                          , use_arrow     = True
                          , background    = WIDGET_BACKGROUND_WINDOWS
                          , foreground    = WIDGET_FOREGROUND_WINDOWS
                          , widget_object = widget.WindowCount( fmt             = FMT_WIDGET_WINDOWS
                                                              , font            = FONT_FAMILY_WIDGET_DEFAULT
                                                              , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                                              , show_zero       = SHOW_ZERO_WINDOWS
                                                              , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_WINDOWS)
                                                              , background      = WIDGET_BACKGROUND_WINDOWS
                                                              , foreground      = WIDGET_FOREGROUND_WINDOWS ) )

layout_name_widget = BarWidget( callback      = CALLBACK_WIDGET_WINDOWS
                              , background    = WIDGET_BACKGROUND_WINDOWS
                              , foreground    = WIDGET_FOREGROUND_WINDOWS
                              , widget_object = widget.CurrentLayoutIcon( fmt             = FMT_WIDGET_WINDOWS
                                                                        , font            = FONT_FAMILY_WIDGET_DEFAULT
                                                                        , fontsize        = FONT_SIZE_WIDGET_DEFAULT
                                                                        , scale           = ICON_SCALE_LAYOUT
                                                                        , padding         = PADDING_LAYOUT_ICON
                                                                        , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_WINDOWS)
                                                                        , background      = WIDGET_BACKGROUND_WINDOWS
                                                                        , foreground      = WIDGET_FOREGROUND_WINDOWS ) )

keyboard_widget = BarWidget( callback      = CALLBACK_WIDGET_KEYBOARD
                           , icon_name     = ICON_NAME_KEYBOARD
                           , use_arrow     = True
                           , background    = WIDGET_BACKGROUND_KEYBOARD
                           , foreground    = WIDGET_FOREGROUND_KEYBOARD
                           , widget_object = widget.KeyboardLayout( fmt                  = FMT_WIDGET_KEYBOARD
                                                                  , font                 = FONT_FAMILY_WIDGET_DEFAULT
                                                                  , fontsize             = FONT_SIZE_WIDGET_DEFAULT
                                                                  , configured_keyboards = CONFIGURED_KEYBOARDS
                                                                  , update_interval      = WIDGET_UPDATE_INTERVAL_KEYBOARD
                                                                  , mouse_callbacks      = setMouseCallbacks(CALLBACK_WIDGET_KEYBOARD)
                                                                  , background           = WIDGET_BACKGROUND_KEYBOARD
                                                                  , foreground           = WIDGET_FOREGROUND_KEYBOARD ) )

power_widget = BarWidget( callback      = CALLBACK_WIDGET_POWER
                        , use_arrow     = True
                        , background    = WIDGET_BACKGROUND_POWER
                        , foreground    = WIDGET_FOREGROUND_POWER
                        , widget_object = widget.Image( filename        = PATH_BAR_ICONS_FORMAT.format(ICON_NAME_POWER)
                                                      , margin_x        = MARGIN_X_WIDGET_IMAGE_POWER
                                                      , margin_y        = MARGIN_Y_WIDGET_IMAGE_POWER
                                                      , scale           = SCALE_ICON_DEFAULT
                                                      , mouse_callbacks = setMouseCallbacks(CALLBACK_WIDGET_POWER)
                                                      , background      = WIDGET_BACKGROUND_POWER
                                                      , foreground      = WIDGET_FOREGROUND_POWER ) )

# ////////////////////////////////////////////////////////////////// WIDGET LAYOUT ////////////////////////////////////////////////////////////////// #

screen_0_bar_widgets = [ python_logo_widget     
                  , separator_widget
                  , group_box_widget
                  , separator_widget
                  , window_name_widget
                  , systray_widget
                  , volume_widget
                  , windows_widget
                  , layout_name_widget
                  , keyboard_widget
                  , temp_widget
                  , cpu_speed_widget
                  , cpu_usage_widget
                  , disk_widget
                  , memory_widget
                  , update_pac_widget
                  , update_aur_widget
                  , net_up_widget
                  , net_down_widget
                  , date_widget
                  , clock_widget
                  , weather_widget
                  , weather_temp_widget
                  , power_widget ]

screen_1_bar_widgets = [ python_logo_widget 
                      , separator_widget
                      , group_box_widget
                      , separator_widget
                      , window_name_widget_alt
                      , date_widget
                      , clock_widget
                      , volume_widget
                      , windows_widget
                      , layout_name_widget
                      , keyboard_widget
                      , power_widget ]

# ///////////////////////////////////////////////////////////////// SCREEN SETTINGS ///////////////////////////////////////////////////////////////// #

screen_0_bar = getBar(screen_0_bar_widgets)
screen_1_bar = getBar(screen_1_bar_widgets)

screen_0 = Screen( top = bar.Bar( screen_0_bar
                                , BAR_SIZE
                                , opacity    = 1
                                , background = COLOR_BACKGROUND ) )

screen_1 = Screen( top = bar.Bar( screen_1_bar
                                , BAR_SIZE
                                , opacity    = 1
                                , background = COLOR_BACKGROUND ) )

screens = [ screen_0, screen_1 ]

# ////////////////////////////////////////////////////////////////// STARTUP HOOKS ////////////////////////////////////////////////////////////////// #

@hook.subscribe.startup_once
def autostart():
    # Make windows appear on proper monitors
    qtile.cmd_to_screen(2)
    qtile.groups_map[ GROUP_NAMES[9] ].cmd_toscreen(toggle = False)

    qtile.cmd_to_screen(1)
    qtile.groups_map[ GROUP_NAMES[8] ].cmd_toscreen(toggle = False)

    qtile.cmd_to_screen(0)

    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# ////////////////////////////////////////////////////////////////// OTHER SETTINGS ////////////////////////////////////////////////////////////////// #

#dgroups_key_binder         = None
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
