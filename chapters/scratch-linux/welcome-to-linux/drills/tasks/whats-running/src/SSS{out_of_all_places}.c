#include <unistd.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
	int rc = unlink(argv[0]);

	if (rc == -1) {
		perror("unlink");
		return 1;
	}

	while (1)
		;	

	return 0;
}
