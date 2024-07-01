# methods for strings

name = 'miguel'

print(name.upper())
print(name.lower())
print(name.title())

text = ' hello world! '

print(text.strip())
print(text.lstrip())
print(text.rstrip())

phrase = 'methods for string in python'

print('-'.join(phrase))

print(f'my name is {name} and I am running this text "{text}" with string interpolation in python!')

message = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.
"""

print(message)