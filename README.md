# Python - CLI Print Tool
Improve the readability and appearance of your print statements.

---

## How to get started
1. Import the `CLIPrintTool` class from `cli_print_tool.py`
```python
from cli_print_tool import CLIPrintTool
```
(Optional) Import the `TextAlignment` class from `cli_print_tool.py` to change the text alignment (by default left-aligned).
```python
from cli_print_tool import CLIPrintTool, TextAlignment
```

2. Create a `CLIPrintTool` object.
```python
CLIPrintTool()
```
(Optional) Specify the maximum line length for your content (by default 100 characters).
```python
CLIPrintTool(120)  # custom max length of 120 characters
```

3. Use the [public methods](#list-of-public-methods) from `CLIPrintTool` to print your formatted text content.
```python
CLIPrintTool().textbox("Hello World!")
```

---

## List of public methods
1. [Textbox](#textbox)
2. [Heading](#heading)

---

## Textbox
Takes two parameters and print text inside a box.

### Parameters
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Required</th>
            <th>Default Value</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>text</td>
            <td>String</td>
            <td>Yes</td>
            <td>None</td>
        </tr>
        <tr>
            <td>alignment</td>
            <td>TextAlignment</td>
            <td>No</td>
            <td>TextAlignment.left</td>
        </tr>
    </tbody>
</table>

### Examples
#### Example 1
Print text inside a box and aligned to the left.
```python
CLIPrintTool().textbox("The quick, brown fox jumps over a lazy dog.")
```
![Screenshot of the console output from the example above.](./examples/textbox-example-1.png)
#### Example 2
Print centered text inside a box.
```python
CLIPrintTool().textbox("The quick, brown fox jumps over a lazy dog.", TextAlignment.center)
```
![Screenshot of the console output from the example above.](./examples/textbox-example-2.png)
#### Example 3
Print text inside a box and aligned to the right.
```python
CLIPrintTool().textbox("The quick, brown fox jumps over a lazy dog.", TextAlignment.right)
```
![Screenshot of the console output from the example above.](./examples/textbox-example-3.png)

---

## Heading
Takes three parameters and print two texts vertically separated by a line (divider).

### Parameters
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Required</th>
            <th>Default Value</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>title</td>
            <td>String</td>
            <td>Yes</td>
            <td>None</td>
        </tr>
        <tr>
            <td>subtitle</td>
            <td>String</td>
            <td>Yes</td>
            <td>None</td>
        </tr>
        <tr>
            <td>alignment</td>
            <td>TextAlignment</td>
            <td>No</td>
            <td>TextAlignment.left</td>
        </tr>
    </tbody>
</table>

### Examples
#### Example 1
Print two texts vertically separated by a line (divider) and aligned to the left.
```python
CLIPrintTool().heading("This is a Title", "This is a Subtitle")
```
![Screenshot of the console output from the example above.](./examples/heading-example-1.png)
#### Example 2
Print two texts vertically separated by a line (divider) and centered.
```python
CLIPrintTool().heading("This is a Title", "This is a Subtitle", TextAlignment.center)
```
![Screenshot of the console output from the example above.](./examples/heading-example-2.png)
#### Example 3
Print two texts vertically separated by a line (divider) and aligned to the right.
```python
CLIPrintTool().heading("This is a Title", "This is a Subtitle", TextAlignment.right)
```
![Screenshot of the console output from the example above.](./examples/heading-example-3.png)