#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
   jcconv, Japanese Characters CONVerter, interconvert hiragana, katakana, half-width kana.
   This module also treat 'half/wide number', 'half/wide alphabet'.
   
   IMPOTANT: In current version, this works only with utf-8 encoding.


   Simple example of usage is followings

       >>> from jcconv import *
       >>> print hira2kata('あいうえお')   # hiragana to katakana
       アイウエオ
       >>> print kata2hira('カタカナ')     # katakana to hiragana
       かたかな
       >>> print half2hira('ﾊﾝｶｸｶﾀｶﾅ')      # half-width kana to hiragana
       はんかくかたかな       
       >>> print half2wide('hello jcconv') # half-width alphabet to wide-width
       ｈｅｌｌｏ ｊｃｃｏｎｖ
       >>> print wide2half('ＷＩＤＥ')     # wide-width alphabet to half-width
       wide
"""

__author__  = "Matsumoto Taichi (taichino@gmail.com)"
__version__ = "0.1.4"
__license__ = "MIT License"
__all__     = ['hira2kata', 'kata2hira', 'half2hira', 'hira2half', 'kata2half',
               'half2kata', 'half2wide', 'wide2half', 'convert']

import re
from jcconv import jcconv

# convert hiragana to katakana
def hira2kata(text):
  return convert(text, jcconv.HIRA, jcconv.KATA)

# convert katakana to hiragana
def kata2hira(text):
  return convert(text, jcconv.KATA, jcconv.HIRA)

# convert half-width kana to hiragana
def half2hira(text):
  return convert(text, jcconv.HALF, jcconv.HIRA)

# convert hiragana to half-width kana
def hira2half(text):
  return convert(text, jcconv.HIRA, jcconv.HALF)

# convert katakana to half-with kana
def kata2half(text):
  return convert(text, jcconv.KATA, jcconv.HALF)

# convert half-width kana to katakana
def half2kata(text):
  return convert(text, jcconv.HALF, jcconv.KATA)

# expand half width number and alphabet to wide width
def half2wide(text):
  text = convert(text, jcconv.HNUM, jcconv.WNUM)
  return convert(text, jcconv.HALP, jcconv.WALP)

# shrink wide with number and alphabet to half width
def wide2half(text):
  text = convert(text, jcconv.WNUM, jcconv.HNUM)
  return convert(text, jcconv.WALP, jcconv.HALP)

# convert 'frm' charset to 'to' charset
# input text must be unicode or str(utf-8)
# 'frm' and 'to' can be specified with (HIRA, KATA, HALF, WNUM, HNUM, WALP, HALP)
def convert(text, frm, to):
  uflag = isinstance(text, unicode)
  f_set = jcconv.char_sets[frm]
  t_set = jcconv.char_sets[to]

  text = uflag and text or text.decode('utf-8')
  if len(f_set[0].split(' ')) == len(t_set[0].split(' ')):
    for i in range(len(f_set)):
      conv_table = dict(zip(f_set[i].split(' '), t_set[i].split(' ')))
      text = _multiple_replace(text, conv_table)
    return uflag and text or text.encode('utf-8')
  else:
    raise "Invalid Parameter"

def _multiple_replace(text, dic):
  rx = re.compile('|'.join(dic))
  def proc_one(match):
    return dic[match.group(0)]
  return rx.sub(proc_one, text)


if __name__ == '__main__':
  import codecs, sys
  sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
  
  print convert(u'あいうえお', jcconv.HIRA, jcconv.HALF)
  print convert(u'ばいおりん', jcconv.HIRA, jcconv.HALF)
  print convert(u'ﾊﾞｲｵﾘﾝ', jcconv.HALF, jcconv.HIRA)
  print convert(u'12345', jcconv.HNUM, jcconv.WNUM)
