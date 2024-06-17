#! /bin/bash
# SPDX-License-Identifier: BSD-3-Clause

ps -ef
# Now scroll through the output until you see a process whose name starts with `SSS`.

# Or, if you've learnt about `|`, you can use it to ease your work:
pgrep -lf SSS
