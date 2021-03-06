##
# @file color_palette.py
#
# @brief Defines the color_palette class.
#
# @section author_palette Author(s)
# - Created by Jessica Dawson on 03/16/2022.

# Imports
from random import randint, choice

import pygame_gui as pgui
import pygame as pg

from modules.widget import widget
import assets

_color_palettes = {
    "Forest" : ["#323232", "#295f4e", "#6db193", "#f4e5c2"],
    "Futuristic" : ["#222831", "#393e46", "#00adb5", "#eeeeee"],
    "Sunset" : ["#f9ed69", "#f08a5d", "#b83b5e", "#6a2c70"],
    "Vintage" : ["#f85f73", "#fbe8d3", "#928a97", "#283c63"],
    "Crimson" : ["#0f1021", "#d01257", "#fb90b7", "#ffcee4"],
    "Vampire" : ["#34374c", "#2c2e3e", "#ee2b47", "#f6f6f6"],
    "Lightning" : ["#f3f3f3", "#ffdd67", "#ffcd38", "#4a4a4a"],
    "Pastel" : ["#8fcfd1", "#df5e88", "#f6ab6c", "#f6efa6"],
    "Lava" : ["#2f2519", "#4a3f35", "#fa7d09", "#ff4301"],
    "Neon" : ["#0c093c", "#df42d1", "#eea5f6", "#fad6d6"],
    "Lilac" : ["#f0e3ff", "#d89cf6", "#916dd5", "#3e206d"],
    "Soft Gray" : ["#3c4245", "#5f6769", "#719192", "#dfcdc3"],
    "Low Saturation" : ["#333644", "#84577c", "#c65f63", "#f6e1b8"],
    "Poison" : ["#151716", "#3e432e", "#616f39", "#a7d129"],
    "Spring" : ["#f9f9f9", "#ffe0ac", "#ffacb7", "#6886c5"],
    "Black & White" : ["#262626", "#595959", "#b0b0b0", "#e3e3e3"],
    "Corruption" : ["#6f4a8e", "#221f3b", "#050505", "#ebebeb"],
    "Ivy" : ["#1fab89", "#62d2a2", "#9df3c4", "#d7fbe8"],
    "Ocean" : ["#73f7dd", "#2cc4cb", "#1972a4", "#2e3a87"],
    "Royalty" : ["#fcf0c8", "#f7d098", "#911f27", "#630a10"],
    "Transit" : ["#5BCEFA", "#F5A9B8", "#FFFFFF"],
    "Lipstick" : ["#d52d00", "#ef7627", "#ff9a56", "#ffffff",
    "#D162A4", "#B55690", "#A30262"],
    "Beach" : ["#73f7dd", "#2cc4cb", "#1972a4", "#2e3a87",
    "#fcf0c8", "#f7d098", "#911f27", "#630a10"],
    "Rose" : ["#6f58c9", "#7e78d2", "#b6b8d6", "#bbdbd1", "#bdede0"],
    "Rainforest": ["#00241B", "#4e878c", "#65B891", "#93E5AB", "#B5FFE1"],
    "Spring" : ["#040926", "#251351", "#7D2E68", "#A85751", "#C97B84"],
    "Halloween" : ["#5E503F","#A9927D","#F2F4F3","#22333B","#0A0908"],
    "Autumn" : ["#C3E991","#DFCC74","#CB904D","#75485E","#51A3A3"],
    "Bright" : ["#89FC00","#008BF8","#DC0073","#F5B700","#04E762"],
    "Pistacho" : ["#3C1742","#F3FFB9","#C42021","#6C0E23","#561643"],
    "Steal Teal" : ["#492C1D","#5B5750","#6B7F82","#7C99B4","#8EB8E5"],
    "Violet Desert" : ["#18020C","#634B66","#9590A8","#BBCBCB","#E5FFDE"],
    "Verve" : ["#A2666F","#F49390","#F45866","#C45AB3","#631A86"],
    
}

class color_palette(widget):
    """! The color palette widget class.

    Provides a ui and functionality to specify the current color palette and the background color.
    """

    def __init__(self, x, y, window, ui_manager):
        """! Initializes the color palette widget.

        @param x                Horizontal position to draw the widget at on the ui.
        @param y                Vertical position to draw the widget at on the ui.
        @param window           Ui window to draw the widget to.
        @param ui_manager       Pygame_gui element manager to tie pygame_gui elements to.
        """

        self.__x = x
        self.__y = y
        self.__window = window
        self.__ui_manager = ui_manager

        ## Theme color for background
        self.color = "#2B2834"
        ## Theme color for text
        self.ui_h1_color = "#FFFFFF"

        ## Name of currently selected palette
        self.palette_name = choice(list(_color_palettes.keys()))
        ## Colors of currently selected palette
        self.palette_colors = _color_palettes[self.palette_name]
        ## The palette color selected as the background
        self.background_index = 0

        ## 1 if radomization of the palette is locked, 0 otherwise
        self.palette_lock = 0
        ## 1 if radomization of the background color is locked, 0 otherwise
        self.background_lock = 0


    def draw_ui_dynamic(self):
        """! Draws the dynamic ui elements for the color palette widget.

        Draws the text, lock icons, and color swatches.
        """

        interactables_margin = self.__x + 42
        lock_margin = self.__x + 17

        pg.draw.rect(self.__window, pg.Color(self.color), (self.__x, self.__y, 252, 135))

        if self.palette_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+35))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+35))

        if self.background_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+68))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+68))

        assets.text_to_screen(window=self.__window, text="COLOR PALETTE", color=self.ui_h1_color, pos=(interactables_margin, self.__y+15), font_size=18)
        for i, color in enumerate(self.palette_colors):
            pg.draw.rect(self.__window, assets.active_color if self.background_index == i else assets.inactive_color,
                        (interactables_margin+((i%4)*50), self.__y+65+(36*(i//4)), 26, 26))
            pg.draw.rect(self.__window, pg.Color(color), (interactables_margin+3+((i%4)*50), self.__y+68+(36*(i//4)), 20, 20))


    def change_colors(self):
        """! Change the theme colors. """
        self.color = "#AAB1B6" if self.color=="#2B2834" else "#2B2834"
        self.ui_h1_color = "#000000" if self.ui_h1_color=="#FFFFFF" else "#FFFFFF"

    def draw_ui_static(self):
        """! Draws the static ui elements for the color palette widget.

        Draws the palette dropdown, lock buttons, and color swatch buttons.
        """

        interactables_margin = self.__x + 42
        lock_margin = self.__x + 6

        cp_len = len(self.palette_colors)

        current_palette_dropdown = pgui.elements.UIDropDownMenu(options_list=_color_palettes.keys(),
                                                            starting_option=self.palette_name,
                                                            relative_rect=pg.Rect(interactables_margin, self.__y+35, 200, 22), manager=self.__ui_manager,
                                                            object_id="current_palette_dropdown")

        palette_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+42, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="palette_lock_button")
        background_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+72, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="background_lock_button")

        background_index_button_one = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+12, self.__y+65+12, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_one", visible=cp_len>0)
        background_index_button_two = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+50+12, self.__y+65+12, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_two", visible=cp_len>1)
        background_index_button_three = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+100+12, self.__y+65+12, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_three", visible=cp_len>2)
        background_index_button_four = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+150+12, self.__y+65+12, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_four", visible=cp_len>3)
        background_index_button_five = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+12, self.__y+65+12+36, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_five", visible=cp_len>4)
        background_index_button_six = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+50+12, self.__y+65+12+36, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_six", visible=cp_len>5)
        background_index_button_seven = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+100+12, self.__y+65+12+36, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_seven", visible=cp_len>6)
        background_index_button_eight = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+150+12, self.__y+65+12+36, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_eight", visible=cp_len>7)

        self.background_index_buttons = [background_index_button_one, background_index_button_two, background_index_button_three, background_index_button_four, background_index_button_five,
                        background_index_button_six, background_index_button_seven, background_index_button_eight]


    def refresh_ui_static(self):
        """! Refreshes the static ui elements for the color palette widget.

        Changes how many color swatch buttons display based on the length of the color palette.
        """

        cp_len = len(self.palette_colors)

        for i in range(8):
            if i < cp_len:
                self.background_index_buttons[i].show()
            else:
                self.background_index_buttons[i].hide()


    def randomize(self):
        """! Randomize the current color palette and background color. """

        if self.palette_lock == 0:
            self.palette_name = choice(list(_color_palettes.keys()))
            self.palette_colors = _color_palettes[self.palette_name]
            if self.background_index >= len(self.palette_colors):
                    self.background_index = randint(0, len(self.palette_colors)-1)
            self.refresh_ui_static()
        
        if self.background_lock == 0:
            self.background_index = randint(0, len(self.palette_colors)-1)


    def events(self, event):
        """! Processes pygame events for the color palette widget.
        
        Handles the palette dropdown, lock buttons, and background color buttons.

        @param event    The pygame event being processed.
        """

        if event.user_type == pgui.UI_BUTTON_PRESSED:
            if event.ui_object_id == "palette_lock_button":
                self.palette_lock = 1 if self.palette_lock == 0 else 0
            if event.ui_object_id == "background_lock_button":
                self.background_lock = 1 if self.background_lock == 0 else 0

            if event.ui_object_id == "background_index_button_one":
                self.background_index = 0
            if event.ui_object_id == "background_index_button_two":
                self.background_index = 1
            if event.ui_object_id == "background_index_button_three":
                self.background_index = 2
            if event.ui_object_id == "background_index_button_four":
                self.background_index = 3
            if event.ui_object_id == "background_index_button_five":
                self.background_index = 4
            if event.ui_object_id == "background_index_button_six":
                self.background_index = 5
            if event.ui_object_id == "background_index_button_seven":
                self.background_index = 6
            if event.ui_object_id == "background_index_button_eight":
                self.background_index = 7

        if event.user_type == pgui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_object_id == "current_palette_dropdown":
                self.palette_name = event.text
                self.palette_colors = _color_palettes[self.palette_name]
                if self.background_index >= len(self.palette_colors):
                    self.background_index = randint(0, len(self.palette_colors)-1)
                self.refresh_ui_static()

        return 0


    def get_name_of_palette(self):
        """! Get the name of the current palette. 
        
        @return The palette name.
        """
        return self.palette_name


    def get_colors_from_palette(self):
        """! Get the list of colors for the current palette in hex form. 
        
        @return A list of the palette colors.
        """
        return self.palette_colors


    def get_background_color(self):
        """! Get the background color in hex form. 
        
        @return The background color.
        """
        return self.palette_colors[self.background_index]


    def get_foreground_colors(self):
        """! Get the list of foreground colors in hex form. 
        
        @return A list of the palette colors excluding the background color.
        """
        return [c for c in self.palette_colors if c != self.palette_colors[self.background_index]]