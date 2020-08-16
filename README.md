# Instagram Bot

An Instagram bot that follows an other user followers and unfollow users who didn't follow you back.

### Prerequisites

You will need to have installed:

```
Python3
Pip
Instapy
```

## Getting Started

Rename the "config-example.py" file to "config.py" and set your credentials:
    * The "username" and "password" are from Instagram login.
    * On "users_to_follow" you should put the list of users the script will use to get new followers.
    * On the "white_list" you can put the users that don't follow your account, but you still want to follow them anyway.

To run the script:
```sh
 python -u path/to/main.py
```

## Documentation

* [Instapy](https://github.com/timgrossmann/InstaPy) - Used to connect and manage Instagram features
