extern get_flag_part
extern exit
global f2

section .text

f2:
        mov rax, 1
        add rax, rbx
        inc rax
        sub rax, r9
        shl rax, 3
        shr rax, 2

        cmp rax, 100
        jb l1
        cmp rax, 200
        ja l1

        jmp l2

l1:
        mov rdi, -1
        call exit

l2:
	mov rdi, 2
	call get_flag_part
        ret
