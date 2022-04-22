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
    "Display and automatically perform line-wrapping for long texts",
    "Display texts inside boxes",
    "Display headings (texts with a title and subtitle)",
    "Display elements as a numbered list with or without title",
    "Change text alignment (supported by any of these features)"
]

CLIPrintTool().list(elements, "What can I do with CLIPrintTool?")
print()  # blank line

# display long text without borders
long_text = """CLIPrintTool will automatically wrap your text to respect the maximum line length (by default 100 \
characters) and preserve line returns.

The text below is a complete \"Lorem Ipsum\" paragraph:

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras quis sollicitudin ante. Etiam ultricies cursus ligula, \
et vulputate tortor elementum sed. Nunc et ante interdum, imperdiet turpis sed, egestas sem. Nunc ipsum risus, rutrum \
a sodales a, mattis quis nunc. Nunc placerat leo elit, at iaculis nulla porta a. Sed condimentum ante at suscipit \
facilisis. Nulla et iaculis augue. Vivamus consequat metus odio, ac fringilla justo porttitor a. In nisi velit, \
vulputate eu consequat sed, pellentesque nec est. Nulla facilisi. Pellentesque semper diam ac tempor finibus. In id \
pulvinar risus. Morbi placerat tellus et vehicula rutrum. Nulla euismod scelerisque est."""

CLIPrintTool().text(long_text)
print()  # blank line

# display heading
CLIPrintTool().heading("Thank you for using CLIPrintTool!",
                       "More details are also available inside the \"README.md\" document.")
