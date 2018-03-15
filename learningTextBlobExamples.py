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

print "---------------------------------------------------------------"

b = TextBlob("I havv goood speling!")
print(b.correct())

print "---------------------------------------------------------------"

from textblob import Word
w = Word('falibility')
# returns a list of (word, confidence) tuples with spelling suggestions.
print w.spellcheck()
print w.spellcheck()[0][0]  ;# word
print w.spellcheck()[0][1]  ;# confidence

w = Word('Government')
print w.spellcheck()
print w.spellcheck()[0][0]
print w.spellcheck()[0][1]

print "---------------------------------------------------------------"

# translation between languages
en_blob = TextBlob(u'Simple is better than complex.')
print en_blob.translate(to='es')

print "---------------------------------------------------------------"

# translate from one language to another.

english_blob = TextBlob(u'Hello')
print english_blob.translate(from_lang="en", to='zh-CN')

chinese_blob = TextBlob(u"美丽优于丑陋")
print chinese_blob.translate(from_lang="zh-CN", to='en')

print "---------------------------------------------------------------"


# You can also attempt to detect a TextBlob’s language using
# Language translation and detection is powered by the Google Translate API.

b = TextBlob(u'بسيط هو أفضل من مجم')
print b.detect_language()

# Handling non-english text in Python :
# https://graduate.artsci.wustl.edu/files/graduatepages/imce/constanza/cfs_methodsworkshop_python.pdf

print "---------------------------------------------------------------"

b = TextBlob("And now for something completely different.")
print(b.parse())

print "---------------------------------------------------------------"

# You can make comparisons between TextBlobs and strings.
apple_blob = TextBlob('apples')
banana_blob = TextBlob('bananas')
print apple_blob < banana_blob
print apple_blob == 'apples'

# You can concatenate and interpolate TextBlobs and strings.
print apple_blob + ' and ' + banana_blob
print "{0} and {1}".format(apple_blob, banana_blob)


print "---------------------------------------------------------------"

# returns a list of tuples of n successive words.
blob = TextBlob("Now is better than never.")
print blob.ngrams(n=3)

print "---------------------------------------------------------------"