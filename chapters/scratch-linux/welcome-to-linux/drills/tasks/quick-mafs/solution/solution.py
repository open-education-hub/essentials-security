# SPDX-License-Identifier: BSD-3-Clause

num = 1337
flag = "SSS{" + str(num)

for i in range(1, 10):
    num = (num**3 * 67 + 31) % 2000
    flag += str(num)

print(flag + "}")
