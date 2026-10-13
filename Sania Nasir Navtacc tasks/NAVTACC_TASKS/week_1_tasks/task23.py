# Multiline string
message = """To avoid pain, they avoid pleasure.
To avoid death, they avoid life."""

print(message)

model = 'ChatGPT'

# Access the first character
print(model[0])    # Output: C

# Access the fifth character
print(model[4])    # Output: G

model = 'ChatGPT'

# Access the last character
print(model[-1])   # Output: T

# Access the fourth last character
print(model[-4])   # Output: t

#model = 'ChatGPT'
#print(model[8])       # IndexError

model = 'ChatGPT'

# Access characters from index 0 up to (but not including) 4
print(model[0:4])   # Output: Chat

model = 'ChatGPT'

model[0] = 'W'
print(model)

model = 'Opus'
version = '5'

model = model + " " + version
print(model)    # Opus 5

text = "ChatGPT is great."

# Replace "ChatGPT" with "Claude"
new_text = text.replace("ChatGPT", "Claude")

print(new_text)  # Output: Claude is great.

print('Chat' in 'ChatGPT')        # True
print('Claude' not in 'ChatGPT')  # True

model = 'Opus'

for c in model:
    print(c)

model = 'Opus'

# Count the number of characters
print(len(model))   # Output: 4

example = "He said, "What's there?""

print(example) # Error

# escape double quotes
example = "He said, \"What's there?\""

# escape single quotes
example = 'He said, "What\'s there?"'

print(example)

# Output: He said, "What's there?"

company = 'Google'
field = 'AI'

message = f'{company} is an {field} company.'
print(message)