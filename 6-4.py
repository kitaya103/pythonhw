glossary = {
  'string': 'A series of characters that can be printed as text.',
  'integer': 'A whole number, positive or negative, excluding decimals.',
  'float': 'A number with a decimal point.',
  'boolean': 'A data type with only two possible values: True or False.',
  'list': 'A collection of items in a specific order, enclosed in square brackets.',
  'dictionary': 'A collection of key-value pairs, enclosed in curly braces.',
  'loop': 'A programming structure that allows you to execute a code block repeatedly.',
  'function': 'A block of code designed to perform a specific task.',
  'conditional statement': 'A statement that controls the flow of execution based on a condition being true or false.',
  'f-string': 'A formatted string literal that allows you to embed expressions directly inside the string.'
}

# Looping through the glossary
for word, definition in glossary.items():
  print(f"\n{word.title()}: {definition}")

print("\nFive new Python terms added to the glossary!")
