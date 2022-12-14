# Encrypto API and WEB APP

A flask API and Web App to generate keys, encrypting and decrypting using RSA method.

To acess the Web App, just [click here](https://encrypto-api-com.onrender.com/generate-page)!

To run locally, clone this repository, install the requirements in a virtualenv and use the command:

 ```sh
 python run.py
 ```
#### Group members:

- Thiago Ribeiro
- Donvicton Monteiro
- José Endson dos Santos
- Edeilson da Costa

## Using the API
### Generate Keys

To generate RSA keys, just send a POST request to https://encrypto-api-com.onrender.com/generate_key with a json like this:

```json
{
    "p" : "13",
    "q" : "17",
    "e" : "5"
}
```

### Encrypting

To encrypting a message, just send a POST request to https://encrypto-api-com.onrender.com/encrypting with a json like this:

```json
{
    "message" : "Ola mundo",
    "n" : "221",
    "e" : "5"
}
```
### Decrypting

To decrypting a crypted message, just send a POST request to https://encrypto-api-com.onrender.com/decrypting with a json like this:

```json
{
    "crypted" : "152 13 32 214 131 133 19 31 152",
    "p" : "13",
    "q" : "17",
    "e" : "5"
}
```

