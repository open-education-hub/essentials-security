# Cookies

HTTP is a stateless protocol used to communicate over the internet.
This means that a request is not aware of any of the previous ones and each request is executed independently.
Given its stateless nature, simple mechanisms such as HTTP cookies were created to overcome the issue.

An HTTP cookie (also called web cookie, internet cookie, browser cookie, or simply cookie) is a small piece of data sent from a website and stored on the user's computer by the user's web browser while the user is browsing.
Cookies were designed to be a reliable mechanism for websites to remember stateful information (such as items added in the shopping cart in an online store) or to record the user's browsing activity (including clicking particular buttons, logging in, or recording which pages were visited in the past).
They can also be used to remember pieces of information that the user previously entered into form fields, such as names, addresses, passwords, and credit card numbers.

![Cookies](../media/cookies.png)

They are like ID cards for websites.
If a browser sends a certain cookie to a web server, the server deduces the identity of said client from that cookie, without requiring authentication.
This can pose problems from a security perspective.
For more details, check the section about [cookie theft and session hijacking](./further-reading.md#cookie-theft--session-hijacking).

## What are Cookies?

A cookie is a key-value pair stored in a text file on the user’s computer.
This file can be found, for example, at the following path on a Linux system using Firefox:

```bash
~/.mozilla/firefox/<some_random_characters>.default-release/cookies.sqlite
```

As the filename implies, Firefox stores cookies in an SQLite database.

An example of cookies set for a website could be:

- `username=admin`
- `cookie_consent=1`
- `theme=dark`

The first cookie stores the username, so it can be displayed to the user without querying the database.
The second one stores the choice made by the user regarding their consent to receive cookies, so the application does not continue to show that annoying message every time.
Finally, the third one stores which theme was selected (in this case, a dark theme).

Once a cookie has been set, the browser will send the cookie information in all subsequent HTTP requests until the cookie is deleted.
Cookies also have various attributes:

- `Domain` and `Path`: define the scope of the cookies.
These attributes tell the browser what website they belong to.
- `Secure`: defines that cookies should only be sent using secure channels such as HTTPS.
- `Expires`: specifies when the cookie is to be deleted.
All cookies have a maximum lifespan, after which they must be erased by the browser, for security.
That why if you haven't logged on a website for a long time, you will be logged out.
  - Alternatively, the`Max-Age` attribute can be used to state the number of seconds after the cookie is to be deleted.

## Cookies from the CLI

We're going to use our old friend `curl`.
To set a cookie we simply use the `-b` parameter like so:

```console
root@kali:~# curl -b 'something=nothing' -b 'something_else=still_nothing' $URL
```
