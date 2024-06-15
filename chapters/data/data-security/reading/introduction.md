
# Introduction

Today's session is about how we secure data in computer systems using math and algorithms.
We will understand why we need cryptography and how we can use it correctly.

## Reminders and Prerequisites

For this session, you will require:

- general understanding of what data is, as discussed in the previous session **Data Representation**.
- high school level math

## Encryption

The process of encoding information in a form that is unrecognisable by most human and can only be deciphered by a select few who posses the mean to do so is called encryption.
Given a piece of information, that from now on we'll call **plaintext**, we use the process of encryption to transform it to an unreadable form known as **ciphertext**.
The purpose of encryption is to allow only authorized parties to decipher a ciphertext back into the original plaintext.
Encryption relies on using a pseudo-random mathematically-generated secret string of characters called **cryptographic key** in order to be able to easily decipher the ciphertext.

![Encryption Example](../media/encryption.svg)

We will talk more about cryptographic keys later in this session were we'll dive deeper into the concepts of symmetric and asymmetric encryption schemes.

## Classical Ciphers

Since Greek and Roman times people needed a way to exchange information safely.
Without complex mathematics and algorithms people found intuitive ways to codify their messages.

Classical ciphers were of two types: substitution and transposition of letters.

## Caesar Cipher

One of the most known and simple classical ciphers, named after the great Roman conqueror Julius Caesar, who also used it to communicate with his crush Cleopatra, works by using the alphabet substitution of a letter by a given shift.

For example if we set our shift to +5 we can see how the cipher works in the following drawing ![Caesar Cipher Example](../media/caesar-cipher.svg)
