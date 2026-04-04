FLAG = open('../flag', 'r').read().rstrip()

C_FILE = """static int verify_flag(const char *flag)
{
"""
for i in range(len(FLAG)):
        C_FILE += f"    if ((flag[{i}] << 1) + 1 != {ord(FLAG[i]) * 2 + 1}) return 1;\n"
C_FILE += """    return 0;
}

int main(int argc, const char* argv[])
{
    return(verify_flag(argv[1]));
}
"""

open('plain.c', 'w').write(C_FILE)
