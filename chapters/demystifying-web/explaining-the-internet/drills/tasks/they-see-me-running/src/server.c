#include <stdio.h>
#include <string.h>

static char *flags[] = {
	"SSS{secure_your_shells}",
	"SSS{bytes_not_bits}",
	"SSS{layer_upon_layer_upon_layer}",
	"SSS{you_chose_your_path}",
	"SSS{datagrams_not_packets}"
};

static char *answers[] = {
	"TCP",
	"32",
	"3",
	"essentials/explaining-the-internet",
	"UDP"
};

static void print_welcome_message()
{
	printf("Welcome to the recap/quiz server!\n");
	printf("I have 5 quizzes for you:\n");
	printf("1. What transport-layer protocol does SSH use?\n");
	printf("2. How many bits is an IPv4 address made of?\n");
	printf("3. At what level of the network stack does ping operate?\n");
	printf("4. What is the path in the following URL: https://security-summer-school.github.io/essentials/explaining-the-internet/#a-general-overview-of-the-internet?\n");
	printf("5. What transport-layer protocol does DNS use?\n");
	printf("First type the number of a question, followed by the answe on a separate line\n");
}

static void handle_connection()
{
	unsigned int question;
	char answer_buff[128];

	scanf("%u\n", &question);
	if (question && question < 6) {
		fgets(answer_buff, sizeof(answer_buff), stdin);
		answer_buff[strlen(answer_buff) - 1] = '\0';

		if (!strcmp(answer_buff, answers[question - 1]))
			puts(flags[question - 1]);
	}
}

int main(void)
{
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);

	while (1) {
		print_welcome_message();
		handle_connection();
	}

	return 0;
}
