#! /usr/bin/python

file = open('../public/not-doge.pnm', 'rb')
data = file.read()
file.close()

# The height is located at an offest of 7 bytes inside the header.
new_data = data[:7] + b'688' + data[10:]

out_file = open('not-doge.pnm', 'wb')
out_file.write(new_data)
out_file.close()
