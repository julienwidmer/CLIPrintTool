# CLIPrintTool
# Basic usage example with left-aligned text.
#
# Coded by Julien Widmer and made available on GitHub.
# https://github.com/julienwidmer/CLIPrintTool

# import the class
from cli_print_tool import CLIPrintTool

# display a textbox
CLIPrintTool().textbox("Welcome to CLIPrintTool!")
print()  # blank line

# display a list
elements = [
    "Display text inside a box",
    "Display headings (text with a title and subtitle",
    "Display elements as a numbered list with or without title",
    "Change the text alignment for any of these features"
]

CLIPrintTool().list(elements, "What can I do with CLIPrintTool?")
print()  # blank line

# display heading
CLIPrintTool().heading("Thank you for using CLIPrintTool!",
                       "More details are also available inside the \"README.md\" document.")
