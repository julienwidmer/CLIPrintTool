from cli_print_tool import CLIPrintTool  # 1) import the class

if __name__ == '__main__':
    # 2) define the maximum line length for the content
    # i.e. 100 characters
    cli_print_tool = CLIPrintTool(80)

    # 3) use the CLIPrintTool methods to display content to the user
    # i.e. display a title inside a box
    cli_print_tool.textbox("Hello World!")  # text align left
    cli_print_tool.textbox("Hello World!", True)  # center
    cli_print_tool.textbox("Hello World!", False, True)  # text align right

    # i.e. display a long text inside a box
    paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent venenatis feugiat auctor. Praesent" \
                " aliquet enim volutpat felis sagittis facilisis. Proin vitae pulvinar sapien. Morbi leo nunc, " \
                "commodo sed hendrerit nec, pretium sed ligula. Pellentesque sit amet vulputate nibh. Fusce iaculis " \
                "elementum feugiat. Curabitur dignissim, magna id suscipit mattis, ante urna consectetur justo, vel " \
                "pretium est nulla at augue. Aliquam rhoncus ullamcorper mauris, lacinia luctus urna interdum ac. " \
                "Donec sollicitudin turpis eu eleifend tristique."
    cli_print_tool.textbox(paragraph)  # text align left
    cli_print_tool.textbox(paragraph, True)  # center
    cli_print_tool.textbox(paragraph, False, True)  # text align right
    cli_print_tool.print_box_divider()
