#include <stdio.h>
#include <stdlib.h>
#define MAXC 1000

const int start_offset = 5;
const int seed = 42;

static unsigned char *obfuscate(const char *s)
{
	int i = 0;
	int garbage;
	unsigned char *res = malloc(10 * MAXC);

	srand(seed);
	while (*s) {
		garbage = rand() % 5;
		while (garbage--)
			res[i++] = rand() % 127 + 1;
		res[i] = ((*s) ^ ((start_offset + i) % 128) ^ (rand() % 128))
			+ 1;
		++i;
		++s;
	}
	res[i] = 0;

	return res;
}

int main(int argc, char const *argv[])
{
	unsigned char *sObfuscated = obfuscate(argv[1]);
	unsigned char *p = sObfuscated;

	while (*p) {
		printf("\\\\x%02x", *p);
		++p;
	}

	free(sObfuscated);

	return 0;
}
