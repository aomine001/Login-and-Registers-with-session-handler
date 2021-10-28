How to use programs:

-register.py - Type in login, password and confirmation password to create new user in users.db, the passwords will be hashed!
-login.py - Type here login and password to get access to your personal account, there can be option where you are banned and your user will not be useable.
-CommitShell.py - Here you can send commands like:
{
  ban [user] - Bans user
  unban [user] - Unbans user
  check-user [user] - checks user if he is banned and gives you his username and his ban status.
  exit - Exists program
}
-resetdbs.py - resets all the databases, the columns will stay unchanged but users and sessions in it will dissapear.


REQUIRE PIP INSTALLS:

-requests - newest
-uuid - newest
-hashlib - newest
-sqlite3 - newest
