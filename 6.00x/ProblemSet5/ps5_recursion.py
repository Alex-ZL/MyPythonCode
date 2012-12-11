# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if aStr == "":
        return aStr
    if len(aStr)==1 or 0:
        return aStr
    else:
        return reverseString(aStr[1:])+aStr[0]

#
# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if x == "":
        return True
    if len(x) == 1:
        return True if x in word else False
    else:
        if x[0] in word:
            i = word.index(x[0])
            return x_ian(x[1:], word[i:])
        else:
            return False
#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    pos = text.rfind("\n")
    if pos == -1:
        pos = 0
    if pos+lineLength >= len(text) or " " not in text[pos:]:
        return text
    else:
        i = text[(pos+lineLength-1):].find(" ")
        if i == -1:
            return text
        i = i+pos+lineLength-1
        text = text[:i]+"\n"+text[i+1:]
        return insertNewlines(text, lineLength)

#print insertNewlines("While I expect new intellectual adventures ahead.", 15)
#print insertNewlines('Nuh-uh! We let users vote on comments and display them by number of votes. Everyone knows that makes it impossible for a few persistent voices to dominate the discussion.', 20)
#print insertNewlines('vnjes vxbialpg qkshrm nylr xtjbnwi wsed wjlutd edx yonl fhuxwvka ebrx ftrodn loiyu tdez oqydsa yvkrcsj jprb scdqar uskwfab gxqtdsio mqlfvw funxkcp fsqbojie rkqgwti inejty ergsibx thvu hfibog tyiqxmhn', 28)
print insertNewlines('tryxgc yevbxqhg xymptd prj awl dtmuo iyxkoz qkfeblpz lodva qdpuy ptysc ltsfn xai vzgs qiwsckf hrji cwb fzomnxwv hiy dhs jwdmtyv hks cnowfbqy fyhdol ths pgsrh ogspdjzi fav eurviltb gmdeyflt kivmya', 46)
