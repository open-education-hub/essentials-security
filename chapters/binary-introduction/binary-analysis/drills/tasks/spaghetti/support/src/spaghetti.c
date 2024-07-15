// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

void fn1(void);
void fn2(void);
void fn3(void);
void fn4(void);
void fn5(void);
void fn6(void);
void fn7(void);
void fn8(void);
void fn9(void);
void fn10(void);
void fn11(void);
void fn12(void);
void fn13(void);
void fn14(void);
void fn15(void);
void fn16(void);
void fn17(void);
void fn18(void);
void fn19(void);
void fn20(void);
void fn21(void);
void fn22(void);
void fn23(void);
void fn24(void);
void fn25(void);
void fn26(void);
void fn27(void);
void fn28(void);
void fn29(void);
void fn30(void);
void fn31(void);
void fn32(void);
void fn33(void);
void fn34(void);
void fn35(void);
void fn36(void);
void fn37(void);
void fn38(void);
void fn39(void);
void fn40(void);

void fn1(void)
{
	int i = 0;

	i += 0;
}

void fn2(void)
{
	sleep(10);
}

void fn3(void)
{
	int number;

	for (int i = 0; i < 9999; i++)
		number = number * i % 1337;
}

void fn4(void)
{
	fn5();
	fn6();
	fn7();
}

void fn5(void)
{
	fn8();
	fn9();
	fn10();
}

void fn6(void)
{
	fn12();
	fn13();
	fn14();
}

void fn7(void)
{
	fn15();
	fn16();
	fn17();
}

void fn8(void)
{
	sleep(1000);
}

void fn9(void)
{
	while (1)
		fork();
}

void fn10(void)
{
	int number;

	for (int i = 0; i < 9999; i++)
		number = number * i % 1337;
}

void fn11(void)
{
	int fd;
	char buffer[100] = { 0 };

	fd = open("../src/flag", O_RDONLY);
	read(fd, buffer, 100);
	puts(buffer);
}

void fn12(void)
{
	int fd;
	char buffer[100];

	fd = open("/dev/urandom", O_RDONLY);

	while (1)
		read(fd, buffer, 100);
}

void fn13(void)
{
	printf("Hello");
}

void fn14(void)
{
	int i = 1 / 0;
}

void fn15(void)
{
	printf("%08x%08x%08x%08x\n");
}

void fn16(void)
{
	fn4();
}

void fn17(void)
{
	int i = 0;

	i += 0;
}

void fn18(void)
{
	fn18();
}

void fn19(void)
{
	fn20();
}

void fn20(void)
{
	fn21();
}

void fn21(void)
{
	fn22();
}

void fn22(void)
{
	fn23();
}

void fn23(void)
{
	fn25();
}

void fn24(void)
{
	fn26();
}

void fn25(void)
{
	fn24();
}

void fn26(void)
{
	fn27();
}

void fn27(void)
{
	fn29();
}

void fn28(void)
{
	fn30();
}

void fn29(void)
{
	fn31();
	fn32();
	fn33();
	fn34();
	fn35();
	fn36();
}

void fn30(void)
{
	fn11();
}

void fn31(void)
{
	int i = 0;

	i += 0;
}

void fn32(void)
{
	int i = 0;

	i += 0;
}

void fn33(void)
{
	int i = 0;

	i += 0;
}

void fn34(void)
{
	fn30();
}

void fn35(void)
{
	int number;

	for (int i = 0; i < 9999; i++)
		number = number * i % 1337;
}

void fn36(void)
{
	int number;

	for (int i = 0; i < 9999; i++)
		number = number * i % 1337;
}

void fn37(void)
{
	int number;

	for (int i = 0; i < 9999; i++)
		number = number * i % 1337;
	fn28();
}

void fn38(void)
{
	int number;

	for (int i = 0; i < 9999; i++)
		number = number * i % 1337;

	fn40();
}

void fn39(void)
{
	int number;

	for (int i = 0; i < 9999; i++)
		number = number * i % 1337;
	fn35();
}

void fn40(void)
{
	int number;

	for (int i = 0; i < 9999; i++)
		number = number * i % 1337;

	fn39();
}

int main(void)
{
	int fnnumber;

	printf("Give me a number\n");
	scanf("%d", &fnnumber);

	switch (fnnumber) {
	case 1:
		fn1();
		break;
	case 2:
		fn2();
		break;
	case 3:
		fn3();
		break;
	case 4:
		fn4();
		break;
	case 5:
		fn5();
		break;
	case 6:
		fn6();
		break;
	case 7:
		fn7();
		break;
	case 8:
		fn8();
		break;
	case 9:
		fn9();
		break;
	case 10:
		fn10();
		break;
	case 11:
		fn10();
		break;
	case 12:
		fn12();
		break;
	case 13:
		fn13();
		break;
	case 14:
		fn14();
		break;
	case 15:
		fn15();
		break;
	case 16:
		fn16();
		break;
	case 17:
		fn17();
		break;
	case 18:
		fn18();
		break;
	case 19:
		fn19();
		break;
	case 20:
		fn20();
		break;
	case 21:
		fn21();
		break;
	case 22:
		fn22();
		break;
	case 23:
		fn23();
		break;
	case 24:
		fn24();
		break;
	case 25:
		fn25();
		break;
	case 26:
		fn26();
		break;
	case 27:
		fn27();
		break;
	case 28:
		fn28();
		break;
	case 29:
		fn29();
		break;
	case 30:
		fn30();
		break;
	case 31:
		fn31();
		break;
	case 32:
		fn32();
		break;
	case 33:
		fn33();
		break;
	case 34:
		fn34();
		break;
	case 35:
		fn35();
		break;
	case 36:
		fn36();
		break;
	case 37:
		fn7();
		break;
	case 38:
		fn37();
		break;
	case 39:
		fn39();
		break;
	case 40:
		fn1();
		break;

	default:
		fn1();
		break;
	}
}
