# Data, Data Everywhere

Up until now, we've learnt that our application (or program) is made out of data and code.
While the code is the engine of the process, as it obviously tells the processor the work that it should do, data is the most interesting (and dangerous) part when it comes to changing the execution of an app.
Why, you might ask?
Well, because it's modifiable;
the majority of the data contained by your program lays around in the `.stack`, `.heap` or `.data` sections of the executable, which makes it **writable**.
And therefore, even more appealing to the attackers.

Attacks on `.rodata` variables are rarely possible due to the protections enforced by the permissions, or lack thereof.
Even though less protected, the `.text` section also gets fewer attacks, as the `W ^ X` security feature becomes the norm.

The gate remains open for malicious endeavours on the `.stack`, `.heap` and `.data` sections, and, today, we'll discuss the most prolific one: the stack.
