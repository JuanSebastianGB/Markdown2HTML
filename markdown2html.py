#!/usr/bin/python3
"""_Function to handle markdown render into a html output_
"""


def from_markdown_to_html():
    """_Processing terminal inputs to get an html output_
    """
    from sys import argv as arguments
    from sys import exit

    argumentsNumber = arguments.__len__()
    if argumentsNumber < 3:
        exit('Usage: ./markdown2html.py README.md README.html')
    try:
        with open(arguments[1]) as file:
            pass
    except IOError:
        exit('Missing {}'.format(arguments[1]))


if __name__ == '__main__':
    """_Main function to render the expected_
    """
    from_markdown_to_html()
