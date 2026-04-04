extern get_flag_part
extern exit
global f1

section .text

f1:
	shl rdi, 4
	sub rdi, 5
	test rdi, 2
	jne l1

	mov rdi, -1
	call exit

l1:
	mov rsi, 74
	cmp rdi, rsi
	jg l2

	mov rdi, -1
	call exit

l2:
	mov rdi, 1
	call get_flag_part
	ret
