from cli_print_tool import CLIPrintTool, TextAlignment  # 1) import the classes

if __name__ == '__main__':
    # 2) define the maximum line length for the content
    # i.e. 100 characters
    cli_print_tool = CLIPrintTool(100)

    # 3) use the CLIPrintTool methods to display content to the user
    # i.e. display a title inside a box
    cli_print_tool.textbox("Hello World!")  # text align left
    cli_print_tool.textbox("Hello World!", TextAlignment.center)  # center
    cli_print_tool.textbox("Hello World!", TextAlignment.right)  # text align right

    # i.e. display a long text inside a box
    paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent venenatis feugiat auctor. Praesent" \
                " aliquet enim volutpat felis sagittis facilisis. Proin vitae pulvinar sapien. Morbi leo nunc, " \
                "commodo sed hendrerit nec, pretium sed ligula. Pellentesque sit amet vulputate nibh. Fusce iaculis " \
                "elementum feugiat. Curabitur dignissim, magna id suscipit mattis, ante urna consectetur justo, vel " \
                "pretium est nulla at augue. Aliquam rhoncus ullamcorper mauris, lacinia luctus urna interdum ac. " \
                "Donec sollicitudin turpis eu eleifend tristique."
    cli_print_tool.textbox(paragraph)  # text align left
    cli_print_tool.textbox(paragraph, TextAlignment.center)  # center
    cli_print_tool.textbox(paragraph, TextAlignment.right)  # text align right

    # i.e. display a list of options
    options = ["Option One", "Option Two", "Option Three"]
    cli_print_tool.list(options)

    # i.e. create a list with a title
    cli_print_tool.list(options, "Main Menu")
