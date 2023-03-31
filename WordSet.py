class WordSet():
  PunctuationList = [',','!','.','\'']
  
  def __init__(self):
    self.wordset = set()
    
  def cleanText(self,text):
    for punc in WordSet.PunctuationList:
      text = text.replace('punc','')
    return text.lower()
  
  def addText(self, input_string):
    words = self.cleanText(input_string)
    for word in words.split():
      self.wordset.add()
      

my_word = WordSet()
my_word.addText("HI MY NAME IS, CHATGPT & I AM YOUR HELPER'S.")
    
    
