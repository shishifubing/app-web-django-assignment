from multiprocessing.sharedctypes import Value
from typing import Set
from django import template
from re import findall as re_findall
from .__init__ import get_word_list

register = template.Library()
word_list: Set[str] = set(get_word_list())


@register.filter(name='Censor')
def censor(value: str):
    if not isinstance(value, str):
        value = str(value)

    for word in re_findall(r'\b\S+\b', value):
        if word.lower() not in word_list:
            continue
        value = value.replace(word, '*' * len(word))

    return value
