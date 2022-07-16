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

#include <stdio.h>
#include <unistd.h>     /* For getpagesize() */
#include <sys/mman.h>   /* For mprotect() */
#include <errno.h>

const int read_only_var = 10;

int main(void)
{
        int page_size = getpagesize();
        void *ro_addr = &read_only_var; /* Compilation warning */
        void *ro_page;
        int ret;

        printf("%d\n", *(int *)ro_addr);

        /* read_only_var = 11; - compilation error;
         * can't write to read-only variables
         */

        /* *ro_addr = 11; - segfault, trying to write in a read-only area */

        /* Align to page-size */
        ro_page = ro_addr - ((size_t)ro_addr % page_size);

        /* Make the memory zone readable and writeable */
        ret = mprotect(ro_page, page_size, PROT_READ | PROT_WRITE);
        if (ret != 0) {
                printf("mprotect failed: %d\n", errno);
                return 1;
        }

        /* Write to ex-read-only zone */
        *(int *)ro_addr = 11;

        printf("%d\n", *(int *)ro_addr);

        return 0;
}
