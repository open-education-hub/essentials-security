#include <stdio.h>
#include <stdlib.h>

static void get_flag(void)
{
	const int start_offset = 5;
	const int seed = 42; 

	/* Here goes the obfuscated flag output by obfuscate.c */
	char *flag = "__TEMPLATE__";
	int i = 0;
	int iflag = 0;
	int garbage;
	char *res = malloc(128);

	srand(seed);
	while (flag[iflag]) {
		garbage = rand() % 5;
		while (garbage--) {
			rand();
			++iflag;
		}
		res[i++] = (flag[iflag] - 1) ^ ((start_offset + iflag) % 128)
			^ (rand() % 128);
		++iflag;
	}
	res[i] = 0;

        puts(res);
}

int main(void)
{
        return 0;
}
