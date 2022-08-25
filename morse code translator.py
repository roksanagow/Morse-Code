#Lines up to 87 are adapted from: https://www.101computing.net/morse-code-using-a-binary-tree/
#A class to implement a Node / Tree
class Node:
  def __init__(self, value, dot=None, dash=None):
    self.value = value
    self.dot = dot
    self.dash = dash
  
      
#Let's initialise our binary tree:
tree = Node(" ") #The root node of our binary tree

# 1st Level
tree.dot = Node("E")
tree.dash = Node("T")

# 2nd Level
tree.dot.dot = Node("I")
tree.dot.dash = Node("A")
tree.dash.dot = Node("N")
tree.dash.dash = Node("M")

# 3rd Level
tree.dot.dot.dot = Node("S")
tree.dot.dot.dash = Node("U")
tree.dot.dash.dot = Node("R")
tree.dot.dash.dash = Node("W")

tree.dash.dot.dot = Node("D")
tree.dash.dot.dash = Node("K")
tree.dash.dash.dot = Node("G")
tree.dash.dash.dash = Node("O")

# 4th Level
tree.dot.dot.dot.dot = Node("H")
tree.dot.dot.dot.dash = Node("V")
tree.dot.dot.dash.dot = Node("F")
tree.dot.dot.dash.dash = Node("")
tree.dot.dash.dot.dot = Node("L")
tree.dot.dash.dot.dash = Node("")
tree.dot.dash.dash.dot = Node("P")
tree.dot.dash.dash.dash = Node("J")

tree.dash.dot.dot.dot = Node("B")
tree.dash.dot.dot.dash = Node("X")
tree.dash.dot.dash.dot = Node("C")
tree.dash.dot.dash.dash = Node("Y")
tree.dash.dash.dot.dot = Node("Z")
tree.dash.dash.dot.dash = Node("Q")
tree.dash.dash.dash.dot = Node("")
tree.dash.dash.dash.dash = Node("")

# 5th level
#I don't know if I have to hard-code all the empty nodes with "", as they have above
tree.dot.dot.dot.dot.dot = Node("5")
tree.dot.dot.dot.dot.dash = Node("4")

tree.dot.dot.dot.dash.dash = Node("3")
tree.dot.dot.dash.dash.dash = Node("2")

tree.dot.dash.dot.dash.dot = Node("+")

tree.dot.dash.dash.dash.dash = Node("1")

tree.dash.dot.dot.dot.dot = Node("6")
tree.dash.dot.dot.dot.dash = Node("=")
tree.dash.dot.dot.dash.dot = Node("/")

tree.dash.dash.dot.dot.dot = Node("7")
tree.dash.dash.dash.dot.dot = Node("8")
tree.dash.dash.dash.dash.dot = Node("9")



#Convert Character (Find the character using a pre-order traversal of the Binary Tree
def getMorseCode(node, character, code):
  if node==None:
    return False
  elif node.value==character.upper():
    return True
  else:  
    if getMorseCode(node.dot,character,code)==True:
      code.insert(0,".")
      return True
    elif getMorseCode(node.dash,character,code)==True:
      code.insert(0,"-")
      return True

    
# The only way to use the tree to translate from characters to morse code would be tree traversal
#Message Input
#TODO - doesnt work for multiple spaces, or any other exceptions

def lettersToCode(message):
  morseCode = ""

  #Convert the message, one character at a time!
  for character in message:
    if character == ' ':
      morseCode = morseCode + ' ' + " " #problem: with multiple spaces, the translation doubles it
    else:
      dotsdashes = []
      getMorseCode(tree,character,dotsdashes)
      code = "".join(dotsdashes)
      morseCode = morseCode + code + " "
  return morseCode


#TODO problem: spaces get translated as START
def codeToChars(message):
  letters = ""

  #Convert one char at a time!
  for character in message.split(" "):
    node = tree
    for part in character:
      if (part not in (' ', '-', '.')):
        pass #Simply don't translate that character
      elif (not node):
        return "One or more of the continuous dots and dashes are not a letter"
      else:
        if part==".":
          node = node.dot
        elif part=="-":
          node = node.dash
    letters += (node.value)
  return letters

def main(lang, text):
  translated = ""
  if (lang=='M'):
    translated = codeToChars(text)
  elif (lang=='A'):
    translated = lettersToCode(text)
  else:
    print("Somehow lang is neither A nor M :(")
  return translated



#-----
#GUI
#-----
import tkinter as tk
import tkinter.font as font

lang = 'A' #The default is A to M

def changeLang():
  global lang
  if (lang == 'A'):
    lang = 'M'
    changeButton["text"] = "Morse code to Alphabet"
  elif (lang == 'M'):
    lang = 'A'
    changeButton["text"] = "Alphabet to Morse code"

def closeWindow():
  window.destroy() #to close the window - when button 'x' is pressed

def translate():
  global lang
  message = text_box.get("1.0", tk.END)
  translatedBox["text"] = "" #first make sure it's empty
  translated = main(lang, message) #lang is specified at start and changed with changeButton
  translatedBox["text"] = translated


window = tk.Tk()
window.title("Morse Code Translator")
frame = tk.Frame(relief = tk.SUNKEN)
frame.pack()

xButton = tk.Button(master=frame, relief = tk.RAISED, text = 'x', width = 5, height = 5, fg = "red", command = closeWindow)
xButton.pack(side = tk.RIGHT) #Specify top right corner of frame here

text_box = tk.Text( #change size by putting it in a frame, forcing the frame to a fixed size...
  #fix it like this guy:  https://stackoverflow.com/questions/14887610/specify-the-dimensions-of-a-tkinter-text-box-in-pixels
  frame,
  fg = "blue")
text_box.pack(side = tk.BOTTOM)

changeButton = tk.Button(master=frame, relief = tk.RAISED, borderwidth=5,
                         text = "Alphabet to Morse code", command = changeLang)
changeButton["font"] = font.Font(family = "Helvetica")

changeButton.pack()

translatedBox = tk.Label(master=frame, text = "Translation will appear here!")
translatedBox.pack(side=tk.BOTTOM, fill = tk.BOTH)

translateButton = tk.Button(master=frame, relief = tk.RAISED, borderwidth = 5, text = "Translate",
                            bg = "blue2", fg = "azure",
                            command = translate)
translateButton["font"] = font.Font(family = "Helvetica")
translateButton.pack()

def func(event):
  translate()
window.bind('<Return>', func)
translatedBox["text"] ="Translation will appear here"

translatedBox["font"] = font.Font(family = "Helvetica")

window.mainloop() #this listebs for tk events, such as button presses, blocks code until you close the window


        
    
  
