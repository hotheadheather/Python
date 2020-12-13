#!/usr/bin/python

import random

print 

"""
        ~~  Mad Dibs  ~~

Mad Dibs- Whats for Dinner

Please enter the described words and additionals words will be chosen at random to fill in your story. 

Lets get started!

     
      """

nounList = [
    'sponges',
    'rubber gloves',
    'hair dryer',
    'fluff-ball',
    'dim sum',
    'octopus'
    ]

adjList = [
    'sloppy',
    'stringy',
    'airy',
    'fluffy',
    'sticky',
    'hairy'
    ]

personInRoom = input("Choose a person's name in the room: ")
verb1 = input('Enter a verb- present/single tense: ')
partOfBodyPlural = input('Enter a part of body - Plural: ')
#adj1 = input('Enter an adjective: ')
pluralNoun1 = input('Enter a plural noun: ')
typeOfLiquid = input('Enter a type of liquid: ')
#adj2 = input('Enter another adjective: ')
#adj3 = input('Enter another adjective: ')
pluralNoun2 = input('Enter a plural noun: ')
personInRoom2 = input("Choose another person's name in the room: ")
noun5 = input('Enter another noun ')
partOfBodyPlural2 = input('Enter another part of body - Plural: ')

print 
"""
        ~~ Thanksgiving  ~~
     
 """


def main():

 print 
 ""


print 
'  It was Thanksgiving and the scent of succulent roast ' \
    + random.choice(nounList) + ' wafted through the house.'

print 
personInRoom + " it's time to " + verb1 \
    + ", my mother called. I couldn't wait to get my " \
    + partOfBodyPlural + ' on that ' + random.choice(adjList) + ' Thanksgiving meal.'

print 
'  My family sat around the dining room ' \
    + random.choice(nounList) \
    + '. The table was laid out with every kind of' \
    + random.choice(nounList) \
    + ' imaginable.  There was a basket of hot buttered ' + pluralNoun1 \
    + ' and glasses of sparkling ' + typeOfLiquid + '.'

print 
'  The ' + random.choice(adjList) + ' turkey sat, steaming, next to a boat of ' \
    + random.choice(adjList) + ' gravy.  A bowl of ruby red ' + random.choice(nounList) \
    + ' sauce, a sweet-' + random.choice(nounList) \
    + ' and a dish of mashed ' + pluralNoun2 + ' tempted my taste buds.'

print 
' But the dish I looked forward to the most was Grandma ' \
    + personInRoom2 + "'s famous " + noun5 \
    + ' pie.  Thanksgiving is my favorite holiday ' + partOfBodyPlural2 \
    + ' down.'


main()
