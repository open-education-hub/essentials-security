# SPDX-License-Identifier: BSD-3-Clause

# Let's start with some string operations.
# We've already seen concatenation.
print(f'aaa + bbb = {"aaa" + "bbb"}')

# But we can do a lot more.

# We can split strings into lists of tokens.
# split's default separator is ' ', meaning that it splits sentences into words.
sentence = "This is a sentence saying that SSS rulz!"
print(f"split sentence = {sentence.split()}")

# We can replace characters using replace.
print(f'replacing " " with "-": {sentence.replace(" ", ".")}')

# Searching for a substring in a string is also easy.
# The find function returns the index of the first occurence of the substring in
# the string, or 0 if it's missing.
print(f'The position of "SSS" in "{sentence}" is: {sentence.find("SSS")}')
print(f'The position of "bananas" in "{sentence}" is: {sentence.find("bananas")}')

# Byte arrays share the same function, but be careful to also give them byte
# parameters, not strings.
byte_sentence = b"This is a byte array saying that SSS rulz!"
print(f"\nsplit byte sentence = {byte_sentence.split()}")
print(f'replacing b" " with b"-": {byte_sentence.replace(b" ", b".")}')
print(f'The position of b"SSS" in "{byte_sentence} is: {byte_sentence.find(b"SSS")}')
print(
    f'The position of b"bananas" in {byte_sentence} is: {byte_sentence.find(b"bananas")}'
)

# Now let's convert bytes into strings and vice-versa.
converted_byte_sentence = sentence.encode()
print(converted_byte_sentence)

converted_string_sentence = byte_sentence.decode()
print(converted_string_sentence)

# Let's use bytes for their intended purpose: to handle file data.
fin = open("output.txt", "rb")  # Notice the b here. It stands for bytes

# When opening a file with the 'b' mode, functions return bytes instead of
# strings.
# Notice the difference between the string and the bytes output.
# The \n characters now appear explicitly, for instance.
print(fin.read())
fin.seek(0, 0)
print(fin.readline())

# Files opened in binary mode also support seeking from the current or end
# positions.
fin.seek(-20, 1)  # Move the cursor 4 bytes back from where it is.
print(fin.readline())

fin.seek(-3, 2)  # Move the cursor 3 bytes back from the end of the file.
print(fin.read())
