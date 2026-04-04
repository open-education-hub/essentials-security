#include <stdio.h>
#include <stdlib.h>

void get_flag_part(int task)
{
	const int start_offset = 5;
	const int seed = 42; 

	/* Here goes the obfuscated flag output by obfuscate.c */
	char *flag = "__TEMPLATE__";
	int i = 0;
	int iflag = 0;
	int garbage;
	int start, end;
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

	switch (task) {
	case 1:
		start = 0;
		end = 9;
		break;
	
	case 2:
		start = 9;
		end = 19;
		break;

	case 3:
		start = 19;
		end = 32;
		break;
	default:
		exit(-1);
	}

	res[end] = 0;
	puts(res + start);
}
