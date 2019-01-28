from __future__ import unicode_literals

from collections import namedtuple
import random

Quote = namedtuple("Quote", ["msg", "source"])

QUOTES = [
    Quote(
        msg="As a wise Pug once said, all you need is love, kibble and a de-worming"
        " tablet every three to six months.",
        source="A Pug's Guide to Dating -  Gemma Correll",
    ),
    Quote(
        msg="An enlightened pug knows how to make the best of whatever he has to work with",
        source="A Pug's Guide to Dating -  Gemma Correll",
    ),
    Quote(
        msg="A pale belly is positively vulgar. Any opportunity to sunbathe should be immediately seized upon.",
        source="A Pug's Guide to Etiquette -  Gemma Correll",
    ),
]


def do_tell():
    quote = random.choice(QUOTES)
    return "{} - {}".format(quote.msg, quote.source)
