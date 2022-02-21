from multiprocessing.sharedctypes import Value
from typing import Set
from django import template
from .__init__ import get_word_list

register = template.Library()
word_list: Set[str] = set(get_word_list())


@register.filter(name='Censor')
def censor(value: str):
    if not isinstance(value, str):
        raise ValueError(
            f'value {str(value)} must be "str", not {type(value)}')
    profanity_set = set(value.split(' ')) & word_list

    if profanity_set:
        raise ValueError(f'value contains profanity - {str(value)}')
