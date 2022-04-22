# CLIPrintTool
#
# Coded by Julien Widmer and made available on GitHub.
# https://github.com/julienwidmer/CLIPrintTool

from enum import Enum


# Creating enumerations using class
class Border(Enum):
    # Enum could be replaced by boolean instead but was created to improve code readability
    # INFO: used inside CLIPrintTool.__print_box_border to print either a top or bottom box border
    top = True
    bottom = False


class TextAlignment(Enum):
    # Enum required for text alignments conditions in CLIPrintTool
    # INFO: The values attributed here do not matter, only the names
    left = 0
    right = 1
    center = 2


class CLIPrintTool:
    # Constructor
    def __init__(self, max_line_length=100):
        self.__max_length = max_line_length  # print statements longer than this value will be wrapped automatically

        self.__border_top_left = "┌"
        self.__border_top_right = "┐"

        self.__border_bottom_left = "└"
        self.__border_bottom_right = "┘"

        self.__border_middle_left = "├"
        self.__border_middle_right = "┤"

        self.__border_vertical = "│"
        self.__border_horizontal = "─"

    # Private Methods
    def __format_text_length(self, text: str, with_borders=False) -> [str]:
        maximum_length = self.__max_length

        if with_borders:
            maximum_length = self.__max_length - 4

        # replace \n with custom string to preserve line return while using text.split() to wrap the text
        custom_line_return = " CLIPrintTool_line_return "
        text = text.replace("\n", custom_line_return)

        # wrap the text if needed
        if len(text) > maximum_length or custom_line_return in text:
            # text too long to be displayed on a single line or contains line return --> split text into a list of words
            words = text.split()  # i.e. "Hello World!" --> ["Hello", "World!"]

            # create text lines respecting the maximum line length
            result_text_lines = []
            text_line = ""
            word_index = 0
            for word in words:
                if text_line == "":
                    # first word of the text or new word after a line return
                    edited_text_line = word  # add word
                else:
                    edited_text_line = text_line + " " + word  # add blank space and word

                if word == custom_line_return.strip():
                    # line return
                    result_text_lines.append(text_line)  # save line
                    edited_text_line = ""  # create new empty line
                elif len(edited_text_line) > maximum_length:
                    # maximum length reached
                    result_text_lines.append(text_line)  # save line without new word
                    edited_text_line = word  # create new line

                word_index += 1  # increment index for next loop
                if word_index == len(words):
                    # current word is the last one in the list
                    result_text_lines.append(edited_text_line)  # save last line
                    return result_text_lines  # return array of formatted text lines
                else:
                    text_line = edited_text_line  # update line
        else:
            # text short enough to be returned without formatting
            return [text]

    # Box border
    # top ┌───┐
    # bottom └───┘
    def __print_box_border(self, border_top: Border):
        length = self.__max_length - 2  # max length minus border left and right characters (1 character each = 2)

        border = self.__border_top_left if border_top.value else self.__border_bottom_left  # add left border
        border += str().ljust(length, self.__border_horizontal)  # create empty string of given length filled with dash
        border += self.__border_top_right if border_top.value else self.__border_bottom_right  # add right border

        print(border)

    # Box content
    # │ Text │
    def __print_box_content(self, text: str, alignment=TextAlignment.left):
        length = self.__max_length - 2 - 2  # max length minus borders and spaces

        box_content = self.__border_vertical + " "  # left border

        if alignment.value == TextAlignment.center.value:
            box_content += text.center(length, " ")  # create an empty string of max length with blanks
        elif alignment.value == TextAlignment.right.value:
            box_content += text.rjust(length, " ")  # create an empty string of max length with blanks
        else:
            box_content += text.ljust(length, " ")  # create an empty string of max length with blanks

        box_content += " " + self.__border_vertical  # left border

        print(box_content)

    # Box divider
    # ├───┤
    def __print_box_divider(self):
        length = self.__max_length - 2  # max length minus border middle left and right

        box_divider = self.__border_middle_left  # right divider
        box_divider += str().ljust(length, self.__border_horizontal)  # create an empty string of max length with blanks
        box_divider += self.__border_middle_right  # left divider

        print(box_divider)

    # Public Method
    def text(self, text: str, alignment=TextAlignment.left):
        text_lines = self.__format_text_length(text)

        for line in text_lines:
            if alignment.value == TextAlignment.center.value:
                print(line.center(self.__max_length, " "))  # centered
            elif alignment.value == TextAlignment.right.value:
                print(line.rjust(self.__max_length, " "))  # right-aligned
            else:
                print(line.ljust(self.__max_length, " "))  # left-aligned (default)

    # Text box
    # ┌──────┐
    # │ Text │
    # └──────┘
    def textbox(self, text: str, alignment=TextAlignment.left):
        text_lines = self.__format_text_length(text, True)

        self.__print_box_border(Border.top)

        for line in text_lines:
            self.__print_box_content(line, alignment)

        self.__print_box_border(Border.bottom)

    # Heading
    # ┌──────────┐
    # │ Title    │
    # ├──────────┤
    # │ Subtitle │
    # └──────────┘
    def heading(self, title: str, subtitle: str, alignment=TextAlignment.left):
        self.__print_box_border(Border.top)

        for title_line in self.__format_text_length(title, True):
            self.__print_box_content(title_line, alignment)

        self.__print_box_divider()

        for subtitle_line in self.__format_text_length(subtitle, True):
            self.__print_box_content(subtitle_line, alignment)

        self.__print_box_border(Border.bottom)

    # List
    # ┌───────────────────────┐
    # │ List Title (Optional) │
    # ├───────────────────────┤
    # │ 1. Element            │
    # │ 2. Element            │
    # └───────────────────────┘
    def list(self, elements: [str], title="", alignment=TextAlignment.left):
        self.__print_box_border(Border.top)

        if title != "":
            # print list title
            self.__print_box_content(title, alignment)
            self.__print_box_divider()

        index = 1
        for element in elements:
            # print list element
            self.__print_box_content(str(index) + ". " + element, alignment)
            index += 1

        self.__print_box_border(Border.bottom)
