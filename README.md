Some notes on how a real project would be improved in no particular order:

## 1. .env file shouldn't be committed into git.
Configuration files with secrets should never be committed, as they pose a security risk.
Instead, we should use an example.env and instruct the user to copy it and enter their credentials manually. 
This also allows each user to have their own credentials, which can be revoked if necessary.

## 2. Don't expose the DB outside the docker network. 
