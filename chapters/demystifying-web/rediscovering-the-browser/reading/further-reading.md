# Further Reading

## Access Control Types

Access control is one part of authorisation.
Below are the 3 main access control types, each with a brief description.
For a more in-depth look at these 3, check out [this link](https://www.twingate.com/blog/access-control-models/).
They are not necessarily disjoint.
Most applications and operating systems use all 3 types at once for different things.

### Discretionary Access Control (DAC)

This is the type of model employed by Linux file permissions.
Each user can decide what permissions to give to other users.
It's easy to implement, but can lead to vulnerabilities because it relies on the fact that users are knowledgeable about security, which is often a far-fetched assumption.

### Mandatory Access Control (MAC)

While DAC is distributed (every user is free to do as they please with their resources), MAC is the opposite: it involves a third party called **resource monitor** (e.g.: the OS) that decides who can do what.

This is the case with sandboxing of iOS/Android apps.
The OS verifies each attempt to access a resource and decides whether to allow it or not.
This model is more complex as it requires a very secure resource monitor, but ensures better security than DAC as it makes fewer assumptions.

### Role-Based Access Control (RBAC)

In this role, the subjects (users) may assume different roles and are granted privileges according to their roles rather than according to their user IDs.

Imagine a student logging onto his school's/university's website.
If they log as a student, they can't access teachers' exam solutions.
But if they could somehow obtain the role of teacher (while using the same account as before), they could view those solutions.

![RBAC](../media/rbac.svg)

This sort of attack is called a **privilege escalation attack** because the student has managed to _elevate_ his default privileges (as a student) to those of a teacher.
