#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def ascii_swap(prestrip):
  """
  This function is used to pre process the strings by removing specified ASCII characters

  Parameters
  ----------
  prestrip : strings without preparation

  Returns
  -------
  poststrip : String with specified ASCII characters removed

  """
  asciiDict = {
    33: 32,
    41: 32,
    44: 32,
    63: 32,
    }
  poststrip = prestrip.translate(asciiDict)
  return poststrip


def word_finder(prestrip, words):
  """
  This function is used to extract the specified date and time words from a string

  Parameters
  ----------
  prestrip : String to be analyzed
  words : List of words to keep in the string

  Returns
  -------
  poststrip : Strings with only the specified words included

  """
  list1 = []
  list2 = []
  list1 = prestrip.split()
  for i in list1:
    if i in words:
      list2.append(i)
  poststrip = " ".join(list2)
  return (poststrip)


def string_cleaning(prestrip):
  """
  This function is used to remove identified special characters using ASCII keys 

  Parameters
  ----------
  prestrip : Strings

  Returns
  -------
  poststrip : Strings with specified ASCII characters removed

  """
  stringcleaner = {
    40: 32,
    41: 32,
    46: 32,
    91: 32,
    93: 32,
    97: 32,
    100: 32,
    101: 32,
    105: 32,
    109: 32,
    116: 32
    }
  poststrip = prestrip.translate(stringcleaner)
  poststrip = poststrip.strip()
  return poststrip

