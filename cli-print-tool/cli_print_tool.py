class CLIPrintTool:
    # Constructor
    def __init__(self, max_line_length):
        self.__max_length = max_line_length  # print statements longer than this value will be wrapped automatically

        self.__border_top_left = "┌"
        self.__border_top_right = "┐"

        self.__border_bottom_left = "└"
        self.__border_bottom_right = "┘"

        self.__border_vertical = "│"
        self.__border_horizontal = "─"

    # Private Methods
    def __format_text_length(self, text: str, with_borders=False) -> [str]:
        maximum_length = self.__max_length

        if with_borders:
            maximum_length = self.__max_length - 4

        if len(text) > maximum_length:
            # text too long to be displayed on a single line --> split text into a list of words
            words = text.split()  # i.e. "Hello World!" --> ["Hello", "World!"]

            # create text lines respecting the maximum line length
            result_text_lines = []
            text_line = ""
            word_index = 0
            for word in words:
                if word_index == 0:
                    edited_text_line = word  # add word
                else:
                    edited_text_line = text_line + " " + word  # add blank space and word
                word_index += 1

                if len(edited_text_line) > maximum_length:
                    # maximum length reached
                    result_text_lines.append(text_line)  # save line without new word
                    edited_text_line = word  # create new line

                if word_index == len(words) - 1:
                    result_text_lines.append(edited_text_line)  # save last line

                text_line = edited_text_line  # update line
            return result_text_lines  # return array of formatted text lines
        else:
            # text short enough to be returned without formatting
            return [text]

    def __print_box_top(self):
        # Box top --> ┌───┐
        length = self.__max_length - 2  # max length minus border top left and right

        box_top = self.__border_top_left
        box_top += str().ljust(length, self.__border_horizontal)  # create an empty string of max length with a dash
        box_top += self.__border_top_right

        print(box_top)

    def __print_box_bottom(self):
        # Box bottom --> └───┘
        length = self.__max_length - 2  # max length minus border top left and right

        box_bottom = self.__border_bottom_left
        box_bottom += str().ljust(length, self.__border_horizontal)  # create an empty string of max length with a dash
        box_bottom += self.__border_bottom_right

        print(box_bottom)

    def __print_box_content(self, text: str):
        # Box bottom --> │ Text │
        length = self.__max_length - 2 - 2  # max length minus borders and spaces

        box_content = self.__border_vertical + " "  # left border
        box_content += text.ljust(length, " ")  # create an empty string of max length with a dash
        box_content += " " + self.__border_vertical  # left border

        print(box_content)

    # Public Method
    def textbox(self, text: str):
        # Text box
        # ┌──────┐
        # │ Text │
        # └──────┘
        text_lines = self.__format_text_length(text, True)

        self.__print_box_top()

        for line in text_lines:
            self.__print_box_content(line)

        self.__print_box_bottom()
