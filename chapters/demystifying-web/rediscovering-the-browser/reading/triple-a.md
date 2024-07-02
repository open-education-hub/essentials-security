# AAA

We say there are 3 A's when it comes to web security (and not only web security):

- Authentication
- Authorisation
- Accounting

## Authentication

Authorisation refers to verifying the client's identity.
It's usually done via requiring the client to submit some credentials such as username and password.
Simply put, authentication takes place whenever you are required to **login** to a website.
The purpose of authentication is obvious: to prevent attackers from **impersonating** legitimate users.

So authentication means answering the question: "Who are you?"
Authentication on its own is not _that_ powerful.
It might allow the server admin to specify which users are allowed to login to a system, but not _what they can do_ once they're logged on that system.

## Authorisation

In order to have a finer access control, such as specifying that a given user may read some files from the server while others can't, authentication is not enough.
We need a means to **enforce** some security policies like, for example, UNIX-like permissions on the file system.
Authentication helps us identify the user, but we need another "A", called **Authorisation** in order to decide what that user may or may not do.

In short, authorisation answers the question: "What can you do?".
It means defining a set of **policies** by which to grant users various kinds of access to different resources.
You can read about the 3 large types of access control types, from which policies derive, [at the end of this session](./further-reading.md#access-control-types).

## Accounting

Accounting refers to logging as a means to audit a system.
Logs provide a chronological view of the events that took place on a system / web server.
Using them we can trace and understand attackers better and protect from them in the future.
