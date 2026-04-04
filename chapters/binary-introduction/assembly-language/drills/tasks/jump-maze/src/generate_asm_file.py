from random import choice, shuffle

REGISTERS = ['al', 'ah', 'bl', 'bh', 'cl', 'ch', 'dl', 'dh', 'dil', 'sil',
    'r8b', 'r9b', 'r10b', 'r11b', 'r12b', 'r13b', 'r14b', 'r15b']
FLAG = open('../flag', 'r').read().rstrip()

TEMPLATES = []
for i in range(1, len(FLAG) - 1):
    TEMPLATES.append(f"""
l{i}:
        mov {choice(REGISTERS)}, '{FLAG[i]}'
        jmp l{i + 1}""")
    i += 1

shuffle(TEMPLATES)

ASM_CODE = f"""section .text
        mov {choice(REGISTERS)}, '{FLAG[0]}'
        jmp l1"""

for template in TEMPLATES:
    ASM_CODE += template

ASM_CODE += f"""
l{len(FLAG) - 1}:
        mov {choice(REGISTERS)}, '{FLAG[-1]}'
        ret
"""

open('jump_maze.asm', 'w').write(ASM_CODE)
