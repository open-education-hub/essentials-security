// SPDX-License-Identifier: BSD-3-Clause
/*
 * Copyright 2023 University POLITEHNICA of Bucharest
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice, this
 *    list of conditions and the following disclaimer.
 *
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 *
 * 3. Neither the name of the copyright holder nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

/* read flag from a file -> place in write-only zone
 * require the students to use mprotect to make the zone readable
 *
 * require the students to use exec, to get a shell and find a flag inside a file
 *
 * require the students to open and read some files, to find a flag
 *
 * hidden flag: some base64 hidden in rodata
 */
#define _GNU_SOURCE
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <stdlib.h>
#include <errno.h>

#define FOREVER         1
#define MAX_FILE_NAME   20

#define elements(array) (sizeof(array) / sizeof(array[0]))

static const char hidden2[] = "https://youtu.be/7lwJOxN_gXc";
static const char hidden[] = "U1NTe29oX3lvdV9mb3VuZF9tZX0=";

int main(void)
{
        char command[100], real_filename[100], buffer[100];
        char *command_type, *filename, *resource, *binary, *perm;
        int fd, ret;
        char has_open_file = 0;
        static const char * const files[] = {"important.txt", "to_buy.txt", "checklist.txt", "music.txt"};
        ssize_t bytes;
        size_t pagesize = getpagesize();
        char *save_ptr;

        char *wronly = mmap(NULL, pagesize, PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);

        if (wronly == (void *)-1) {
                printf("Unexpected error %d! Bye!\n", errno);
                exit(1);
        }
        fd = open("/tmp/wronly_flag", O_RDONLY);

        if (fd != -1) {
                bytes = read(fd, wronly, 50);
                if (bytes == -1) {
                        printf("Unexpected error! Bye!\n");
                        exit(1);
                }
        }

        close(fd);

        while (FOREVER) {
                fgets(command, 100, stdin);

                command_type = strtok_r(command, " ", &save_ptr);

                if (strncmp(command_type, "open", 4) == 0) {
                        memset(real_filename, 0, 100);
                        if (has_open_file == 1) {
                                printf("You can have only one file open at the same time! Security policy\n");
                                continue;
                        }

                        filename = strtok_r(NULL, " \n", &save_ptr);

                        if (filename == NULL) {
                                printf("https://youtu.be/dQw4w9WgXcQ\n");
                                continue;
                        }

                        for (int i = 0; i < elements(files); i++) {
                                if (strncmp(filename, files[i], MAX_FILE_NAME) == 0) {
                                        strncat(real_filename, "/tmp/", 6);
                                        strncat(real_filename, filename,
                                                MAX_FILE_NAME);
                                        fd = open(real_filename, O_RDONLY);
                                        if (fd != -1)
                                                has_open_file = 1;
                                        else
                                                printf("open failed\n");
                                }
                        }
                } else if (strncmp(command_type, "close", 5) == 0) {
                        if (has_open_file == 0) {
                                printf("https://youtu.be/dKLpEb4i0Mk\n");
                                continue;
                        }

                        close(fd);
                        has_open_file = 0;
                } else if (strncmp(command_type, "read", 4) == 0) {
                        if (has_open_file == 0) {
                                printf("https://youtu.be/N7idWG9uEXc\n");
                                continue;
                        }

                        read(fd, buffer, 100);
                        printf("%s", buffer);
                } else if (strncmp(command_type, "mprotect", 8) == 0) {
                        resource = strtok_r(NULL, " ", &save_ptr);
                        if (resource == NULL) {
                                printf("https://youtu.be/zqLEO5tIuYs\n");
                                continue;
                        }

                        perm = strtok_r(NULL, " ", &save_ptr);
                        if (perm == NULL) {
                                printf("https://youtu.be/c48zG-P-EYo\n");
                                continue;
                        }

                        if (strncmp(resource, "wronly", 6) == 0 && strncmp(perm, "RW-", 3) == 0) {
                                ret = mprotect(wronly, pagesize, PROT_READ | PROT_WRITE);
                                if (ret == 0)
                                        printf("%s", wronly);
                                else
                                        printf("mprotect failed\n");
                        }
                } else if (strncmp(command_type, "exec", 4) == 0) {
                        binary = strtok_r(NULL, " \n", &save_ptr);

                        if (strncmp(binary, "/bin/bash", 7) != 0) {
                                printf("https://youtu.be/YtCPmPSyvJI\n");
                                continue;
                        }

                        execl(binary, binary, NULL);
                } else if (strncmp(command_type, "help", 4) == 0) {
                        printf("help - displays available commands\n");
                        printf("list <resource> - print the requested resource\n");
                        printf("        available resources: files, memory,  ??? lmhhir(4)\n");
                        printf("exec <binary> - start the given binary file;  path must be absolute\n");
                        printf("mprotect <memory_zone_name> <protections> - \
                                change protection of a given memory zone;\n");
                        printf("        examples of protection format: RW-, ---\n");
                        printf("open <file> - open a file; can open only the  files diplayed by list\n");
                        printf("close - close the last opened file\n");
                        printf("read - read the current open file\n");
                        printf("exit - exit the program\n");
                } else if (strncmp(command_type, "list", 4) == 0) {
                        resource = strtok_r(NULL, " ", &save_ptr);

                        if (strncmp(resource, "files", 5) == 0)
                                for (int i = 0; i < elements(files); i++)
                                        printf("%s\n", files[i]);
                        else if (strncmp(resource, "memory", 6) == 0) {
                                printf("wronly        -W-\n");
                                printf("???        R--\n");
                        } else if (strncmp(resource, "hidden", 6) == 0)
                                printf("%s\n", hidden);
                        else
                                printf("https://youtu.be/3VTkBuxU4yk\n");
                } else if (strncmp(command_type, "exit", 4) == 0)
                        break;
                else
                        printf("Unrecognized command; use \"help\" to see available commands\n");
        }

        return 0;
}
