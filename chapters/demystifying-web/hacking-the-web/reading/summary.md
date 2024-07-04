# Summary

The key takeaways from this session are:

- HTTP cookies are used to make the protocol stateful.
You can pass them with `curl` by using the `-b` parameter
- Sessions are cookies used to identify a client.
Both `curl` and Python can account for sessions:
  - `curl` does so by saving and loading them from a cookie file with the `-c` and `-c` parameters, respectively
  - Python uses a `Session` object that stores cookies internally
- In path traversal attacks hackers can access files they shouldn't be allowed to by specifying the path to them
  - A very useful tool for testing the existence of additional files is `dirb`.
- One of the most widely used repositories of lists of common names / passwords / anything is [SecLists](https://github.com/danielmiessler/SecLists).
Use it any time.
