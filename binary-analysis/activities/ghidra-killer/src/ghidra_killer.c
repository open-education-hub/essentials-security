// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main(void)
{
	char buffer[30];

	int fd = open("../src/flag", O_RDONLY);

	read(fd, buffer, 30);

	printf("Information acquired\n");

	return 0;
}
