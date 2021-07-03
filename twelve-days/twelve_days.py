import unittest

DAYS = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
        'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

GIFTS = [ "and a Partridge in a Pear Tree.",
        "two Turtle Doves,",
        "three French Hens,",
        "four Calling Birds,",
        "five Gold Rings,",
         "six Geese-a-Laying,",
         "seven Swans-a-Swimming,",
         "eight Maids-a-Milking,",
         "nine Ladies Dancing,",
         "ten Lords-a-Leaping,",
         "eleven Pipers Piping,",
         "twelve Drummers Drumming,"
]

verse_format = "On the {} day of Christmas my true love gave to me: "

def one_verse(n: int) -> str:
    if n==0:
        return verse_format.format(DAYS[n])+ "a Partridge in a Pear Tree."
    return verse_format.format(DAYS[n])+" ".join(GIFTS[n::-1])


def recite(start: int, finish: int) -> list:
    return [one_verse(i) for i in range(start-1,finish)]
