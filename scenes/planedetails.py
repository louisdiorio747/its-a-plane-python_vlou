from rgbmatrix import graphics

from utilities.animator import Animator
from setup import colours, fonts, screen

# Setup
PLANE_DETAILS_COLOUR = colours.PINK
PLANE_DISTANCE_FROM_TOP = 30
PLANE_TEXT_HEIGHT = 9
SCROLL_STOP_POSITION = 0 #33
PLANE_FONT = fonts.small


class PlaneDetailsScene(object):
    def __init__(self):
        super().__init__()
        self.plane_position = screen.WIDTH
        self._data_all_looped = False

    @Animator.KeyFrame.add(1)
    def plane_details(self, count):

        # Guard against no data
        if len(self._data) == 0:
            return

        plane = f'{self._data[self._data_index]["delay"]}' + " " + f'{self._data[self._data_index]["plane"]}'
        # plane = f'{self._data[self._data_index]["delay"]}'

        # Draw background
        self.draw_square(
            SCROLL_STOP_POSITION,
            PLANE_DISTANCE_FROM_TOP - PLANE_TEXT_HEIGHT,
            screen.WIDTH + 40,
            screen.HEIGHT,
            colours.BLACK,
        )

        # Draw text
        text_length = graphics.DrawText(
            self.canvas,
            PLANE_FONT,
            self.plane_position,
            PLANE_DISTANCE_FROM_TOP,
            PLANE_DETAILS_COLOUR,
            plane,
        )
        print(self.canvas)
        # Handle scrolling
        self.plane_position -= 1
        if self.plane_position + text_length < SCROLL_STOP_POSITION + text_length:
            self.plane_position = screen.WIDTH
            if len(self._data) > 1:
                self._data_index = (self._data_index + 1) % len(self._data)
                self._data_all_looped = (not self._data_index) or self._data_all_looped
                self.reset_scene()

    @Animator.KeyFrame.add(0)
    def reset_scrolling(self):
        self.plane_position = screen.WIDTH - SCROLL_STOP_POSITION
