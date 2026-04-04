#include <stdio.h>
#include <stdlib.h>

void print_flag(void);
void king_kong(void);
void godzilla(void);
int main(void);

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
        long x;
        long *ret = (long*)((char*)&x + 64);

        if (*ret >= (long)king_kong) {
                puts("Use print_flag() to call me!");
                exit(1);
        }

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

void print_flag(void)
{
        long x;
        long *ret = (long*)((char*)&x + 32);

        if (*ret >= (long)godzilla) {
                puts("I only answer to King Kong!");
                exit(2);
        }

        get_flag();
}

void king_kong(void)
{
        long x;
        long *ret = (long*)((char*)&x + 32);

        if (*ret >= (long)main) {
                puts("Godzilla's got nothing on me!");
                exit(3);
        }

        print_flag();

}

void godzilla(void)
{
        king_kong();
}

int main(void)
{
        long x;
        void (*fptr)(void);

        printf("Give me an address to call!\n");
        scanf("%ld", (long*)&fptr);

        fptr();

        return 0;
}

