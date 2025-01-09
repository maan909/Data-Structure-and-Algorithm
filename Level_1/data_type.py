#def data_type(str):

string = "heloo"
print(type(string))

integer = 23 
print(type(integer))


def dataTypeSize(input):
      if isinstance(input, str):
          return "Input is a string"
      elif isinstance(input, int):
          return "Input is an integer"
      else:
          return "Invalid Input"

dataTypeSize("h")