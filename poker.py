import random

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n= 5, deck=mydeck):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

def poker(hands):
    """Return a list of winning hands: poker([hand,...]) => [hand,...]"""
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    """Return a list of all items equal to the max of the iterable."""
    for item in iterable:
        print (item)
    #print ("all hands printed")
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks)) #2,3,4,5,6 returns (8,6)
    elif kind(4, ranks):
        return  (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2,ranks):
        return (6, kind(3,ranks), kind(2,ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3,ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2,ranks):
        return (1, kind(2,ranks), ranks)
    else:
        return (0, ranks)

def card_ranks(hand):
    """Return a list of the ranks, sorted with higher first"""
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    print (ranks)
    return [5,4,3,2,1] if (ranks==[14,5,4,3,2]) else ranks

def straight(ranks):
    """Return true if the ordered ranks form a 5 card straight."""
    return (max(ranks)-min(ranks)==4) and len(set(ranks))==5

def flush(hand):
    """Return true if all the cards have the same suits."""
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a tuple: (hightest, lowest);
    otherwise return None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None
def test():
    """Test cases for the functions in poker program."""
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
#    assert poker([sf, fk, fh]) == sf
    assert poker([fh]) == fh
    assert poker([sf] + 99*[fh]) == sf
    return "tests pass"

#print (test())
print (poker(deal(10)))

def hand_percentages(n=700*1000):
    """Sample n random hands and print a table of percentags for each type of hand"""
    counts = [0] * 9
    hand_names = ['High Card', 'Pair', '2 Pair', '3 kind', 'Straight', 'Flush', 'Full House', '4 kind', 'Straight Flush']
    for i in range(int(n/10)):
        for hand in deal(10, deck=mydeck):
            ranking = hand_rank(hand)[0]
            counts[ranking]+=1
    for i in reversed(range(9)):
        print ("%14s: %6.3f" %(hand_names[i], 100.*counts[i]/n))

#hand_percentages(100000) - this function works
