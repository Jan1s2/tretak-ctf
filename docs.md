# CTF server

## Description
It is a very simple CTFd-like system - it does not at the current time contain scoring or user accounts, but it does contain support for challenges and flags. The flag check works on server side and userside is displayed by javascript based on the response from the server.

## Writeups
The system allows anyone to write a writeup. Due to security constraints it only supports plaintext for now.

## Model
The system is based on the following model:
- categories with challenges
- Challenge with name, description, score, difficulty flags and writeups
- Writeup with content
- Flags with flags and hints
- At the moment users can only create, edit or delete a writeup for a challenge

## Installation

```
git clone https://github.com/jan1s2/tretak-ctf.git
cd tretak-ctf
python -m venv .venv
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata initdata.json
python manage.py runserver
```
