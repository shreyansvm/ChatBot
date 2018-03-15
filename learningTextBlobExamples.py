#!/usr/bin/env python
# -*- coding: utf- 8 -*-

from textblob import TextBlob

#inputString = "Python is a high-level, general-purpose programming language."
inputString = "my Name is Shreyans"
wiki = TextBlob(inputString)

print wiki.tags
print wiki.noun_phrases
print "---------------------------------------------------------------"

zen = TextBlob("Beautiful is better than ugly. "
                "Explicit is Better than implicit. "
                "Simple is better than complex.")
print zen.words
print zen.word_counts['better']
# default = False
print zen.words.count('better', case_sensitive=True)
print zen.sentences
print zen.sentences[0]
print zen.sentences[1]
print zen.sentences[2]
print zen.noun_phrases[2]

print "---------------------------------------------------------------"

sentence = TextBlob('Use 4 spaces per indentation level.')
print sentence.words
print sentence.words[2].singularize()
print sentence.words[-1].pluralize()

animals = TextBlob("cat dog octopus")
print animals.words
print animals.words.pluralize()

# TextBlobs Are Like Python Strings
print animals[0:10]

# You can use common string methods.
print animals.upper()
print animals.find('dog')

print "---------------------------------------------------------------"
from textblob import Word

w = Word("octopi")
print w.lemmatize()

w = Word("went")
print w.lemmatize("v")  # Pass in WordNet part of speech (verb)

