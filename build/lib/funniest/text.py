from __future__ import print_function

from pkg_resources import resource_string
from markdown import markdown

joke_text = resource_string(__name__, 'data/joke.txt')

def joke():
    return markdown(joke_text)
