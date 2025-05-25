# Establish authentication with BMW-Github API

1. Create a new ssh key in the local environment
$ ssh-keygen -t rsa
The command abobe will generate a new ssh key-pair: id_rsa and id_rsa.pub in the folder /home/<user-name>/.ssh/

2. Copy the id_rsa.pub content. You can use the 'cat' command to reveal it in the terminal
$ cat /home/<user-name>/.ssh/id_rsa.pub

3. In the BMW-Github account:
- go in 'Settings'
- then in 'SSH and GPG keys'
- 'New SSH key'
- Give a title/name and then paste the contents of id_rsa.pub in the field 'Key'.
- 'Add SSH key'

4. LocalPCAccess Token: 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
