#!/usr/bin/python3
"""_Function to handle markdown render into a html output_
"""


def count_hashtags(line_to_check):
    """Counting # quantity"""
    line_splited = line_to_check.split('# ')
    if line_splited.__len__() == 1:
        return 0
    return line_to_check.count('#')


def transform_hashtag(line_to_check):
    """Transforms the line with # into a line with html tags"""
    hashtags = ['# ', '## ', '### ', '#### ', '##### ', '###### ']
    for hashtag in hashtags:
        if line_to_check.startswith(hashtag):
            hashtags_quantity = count_hashtags(line_to_check)
            return '<h{:n}>{}</h{:n}>\n'.\
                format(hashtags_quantity,
                       line_to_check[hashtags_quantity: -1], hashtags_quantity)
    return ''


def from_markdown_to_html():
    """_Processing terminal inputs to get an html output_
    """
    from sys import argv as arguments
    from sys import exit

    argumentsNumber = arguments.__len__()
    if argumentsNumber < 3:
        exit('Usage: ./markdown2html.py README.md README.html')
    try:
        result = ''
        with open(arguments[1], 'r') as markdown_file:
            markdown_lines = markdown_file.readlines()
            for markdown_line in markdown_lines:
                result = result + (transform_hashtag(markdown_line))
        with open('README.html', 'w') as html_file:
            html_file.write(result)

    except IOError:
        exit('Missing {}'.format(arguments[1]))


if __name__ == '__main__':
    """_Main function to render the expected_
    """
    from_markdown_to_html()
