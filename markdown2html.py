#!/usr/bin/python3
"""_Function to handle markdown render into a html output_
"""


def process_markdown_line(line_to_check, document_lines):
    """Transforms the line with # into a line with html tags
    and append to a list by reference"""

    line_splited = line_to_check.split(' ')
    left_word_part = line_splited[0]
    right_word_part = ' '.join(line_splited[1:]).replace('\n', '')
    if left_word_part[0] == '#':
        document_lines.append(
            '<h{0}>{1}</h{0}>\n'.format(left_word_part.__len__(), right_word_part))


def from_markdown_to_html():
    """_Processing terminal inputs to get an html output_
    """
    from sys import argv as arguments
    from sys import exit

    argumentsNumber = arguments.__len__()
    if argumentsNumber < 3:
        exit('Usage: ./markdown2html.py README.md README.html')
    try:
        document_lines = []
        with open(arguments[1], 'r') as markdown_file:
            markdown_lines = markdown_file.readlines()
            for markdown_line in markdown_lines:
                process_markdown_line(markdown_line, document_lines)
        with open(arguments[2], 'w') as html_file:
            html_file.writelines(document_lines)

    except IOError:
        exit('Missing {}'.format(arguments[1]))


if __name__ == '__main__':
    """_Main function to render the expected_
    """
    from_markdown_to_html()
