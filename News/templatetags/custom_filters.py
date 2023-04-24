from django import template


register = template.Library()

ERROR_WORDS = [
    'Pig',
    'Silly',
    'Foolish',
]


@register.filter()
def censor(word):
    if isinstance(word, str):
        for i in word.split():
            if i.capitalize() in ERROR_WORDS:
                word = word.replace(i, i[0] + '*' * len(i))
    else:
        raise ValueError('Wrong format')
    return word

