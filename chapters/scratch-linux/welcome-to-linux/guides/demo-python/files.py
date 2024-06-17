# SPDX-License-Identifier: BSD-3-Clause

fin = open("../../README.md")  # Use the default mode: rt = read + text

# Use the readline function to, well... read one line from the opened file.
line = fin.readline()
print(line, end="")  # The line we've just read already contains a trailing \n.

# The file object (f) maintains an internal cursor, which is an offset from the
# beginning of the file, where the next operation (read/write) will take place.
# For this reason, the next calls to readline return the correct lines in the
# file.
print(fin.readline(), end="")  # Second line is empty
print(fin.readline(), end="")  # Third line

# There are situations where it is necessary to move the cursor ourselves.
# For this, we have the the seek function.
# First, let's see where our cursor is now.
print(f"fin cursor is initially at {fin.tell()} bytes")

# The seek function takes 2 parameters:
#    - offset: The number of bytes to move the cursor. Can be negative to move the cursor back
#    - whence: From where to move the cursor. Can take the following values:
#        - 0: from the beginning of the file
#        - 1: from the cursor's current position
#        - 2: from the end of the file.
fin.seek(0, 0)  # Move the cursor to the beginning of the file
print(f"after fin.seek(0, 0), fin cursor is at {fin.tell()} bytes")
# Let's try to read a line and see if it truly is the first.
print("First line of README.md:", fin.readline(), end="")  # It is.

# The other modes are available only when opening the file in binary mode.
# We will do this in the next section.

# It's good practice to close a file when you no longer use it.
fin.close()

fout = open("output.txt", "w")  # Open output.txt for writing text
# Unlike print, write does not add a \n character at the end of our text.
fout.write("This is the first line in output.txt\n")
fout.write("SSS Rulz!\n")

fout.close()
