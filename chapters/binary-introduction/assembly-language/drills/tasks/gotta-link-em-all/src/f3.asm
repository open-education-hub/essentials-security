extern get_flag_part
extern exit
global f3

section .text

f3:
        mov rcx, 10
        test r8, r8
        jz l3

l1:
        mov rax, 1
        shl rax, cl

        test cl, 1
        jnz l2

        test rax, r8
        jz l2

l3:
        mov rdi, -1
        call exit

l2:
        dec cl
        jnz l1

	mov rdi, 3
	call get_flag_part
        ret
