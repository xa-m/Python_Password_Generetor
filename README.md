# SHA-256 Password Password Generetor in Python

## Description
This is a simple password generator in python, it uses the SHA-256 algorithm to generate a password with a length of 20 characters instead of the 64 characters that the algorithm generates. That's because the in some social media platforms there is a limit lenght for the password. The password includes numbers, letters with lower case and the capital M for the bypass the capital case requirement of the platforms. All of the passwords start with the question mark(?) symbol and continue with the capital M, then the actual encrypted password itself comes.

## How to use?
<mark>You need to run main.py</mark>

In order to use this program you need to have an <mark>encryption key</mark> which will be used in sha-256 algorythm. And you need an <mark>passkey</mark> to access your encryiption key because it is not something that you want to store in a file.

Then you can generate your password with the keyword (netflix, disneyplus, amazon, steam, ea, etc...).
The keyword is used to generate a unique password for each platform.
The capital case in keyword is not matter but in encryption key it is.
When you generate your password it'll be automaticly copied to your clipboard.

## Requirements
The only libraries I used in this project is <mark>hashlib</mark> for the sha-256 algorithm and <mark>cryptography</mark> for encrypting the encryption key.

- hashlib
- cryptography



## Contact
You can contact me via [midaskaya@outlook.com](mailto:midaskaya@outlook.com)