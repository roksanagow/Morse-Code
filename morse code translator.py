#A class to implement a Node / Tree
class Node:
  def __init__(self, value, dot=None, dash=None):
    self.value = value
    self.dot = dot
    self.dash = dash
  
      
#Let's initialise our binary tree:
tree = Node("START") #The root node of our binary tree

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

#Convert Character (Find the character using a pre-order traversal of the Binary Tree
def getMorseCode(node, character, code):
  if node==None:
    return False
  elif node.value==character:
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
def lettersToCode():
  message = input("Enter a message to convert into Morse Code: (e.g. SOS)").upper()
  morseCode = ""

  #Convert the message, one character at a time!
  for character in message:
    dotsdashes = []
    getMorseCode(tree,character,dotsdashes)
    code = "".join(dotsdashes)
    morseCode = morseCode + code + " "
  
  print(morseCode)


def codeToChars():
  message = input("Enter your message in morse code").split(" ")
  letters = ""

  #Convert one char at a time!
  for character in message:
    node = tree
    for part in character:
      if part==".":
        node = node.dot
      elif part=="-":
        node = node.dash

    letters += (node.value)

  print(letters)

def main():
  whichWay = input("Morse code to alphabet - press M \n Alphabet to morse code - press A \n").upper()
  if (whichWay=="M"):
    codeToChars()
  elif (whichWay=="A"):
    lettersToCode()
  else:
    print("Type M or A")

main()
    

        
    
  
