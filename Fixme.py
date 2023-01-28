#!/usr/bin/python3
'''
Complete each function below so that the test cases pass.
Your solutions should use the map and filter functions,
and not for loops or list comprehensions.
'''


def evens(n):
    return list(range(0, n+1, 2))


def threes(n):
    '''
    Returns a list of all numbers from 0 to n inclusive that contain
    the digit 3.
    >>> threes(2)
    []
    >>> threes(3)
    [3]
    >>> threes(10)
    [3]
    >>> threes(20)
    [3, 13]
    >>> threes(50)
    [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43]
    '''

    var = range(0, n + 1)
    var = map(three, var)
    var = list(var)
    var = (filter(lambda item: item is not None, var))
    return list(var)


def three(n):
    if "3" in str(n):
        return n
    return


def small_words(text):
    '''
    Returns a list of all words in the input text that are less than
    4 characters long.

    HINT:
    Recall that text.split() converts the text variable into a list of words.

    >>> small_words('this is a simple test case')
    ['this', 'is', 'a', 'test', 'case']
    >>> small_words('really enormous words')
    []
    >>> small_words('')
    []
    >>> small_words('a big word is bad')
    ['a', 'big', 'word', 'is', 'bad']
    '''
    var = text.split()
    var = map(bigWord, var)
    var = list(var)
    var = list(filter(lambda item: item is not None, var))
    return var


def bigWord(string):
    if (len(string) > 4):
        return
    return string


def squares(n):
    '''
    Returns a list of all square number between 1 and n inclusive.
    Recall that the nth square number is defined to be n*n.

    >>> squares(1)
    [1]
    >>> squares(2)
    [1, 4]
    >>> squares(3)
    [1, 4, 9]
    >>> squares(10)
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    '''
    var = range(1, n + 1)
    var = map(square, var)
    return list(var)


def square(n):
    return n ** 2


def lengths(strings):
    '''
    Given a list of strings, returns a list of the lengths of the
    corresponding strings.

    >>> lengths([])
    []
    >>> lengths(['test'])
    [4]
    >>> lengths(['this','is','a','test'])
    [4, 2, 1, 4]
    '''
    words = map(lengthWord, strings)
    return list(words)


def lengthWord(word):
    return len(word)
