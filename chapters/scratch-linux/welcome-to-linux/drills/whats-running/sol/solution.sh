#! /bin/bash

ps -ef
# Now scroll through the output untill you see a process whose name starts with `SSS`.

# Or, if you've learnt about `|`, you can use it to ease your work:
ps -ef | grep SSS
