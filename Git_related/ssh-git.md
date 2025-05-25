# SSH Configuration for Git

-   Go in
    * Linux/Mac:    .ssh/.config
    * Windows:      %USERPROFILE%\.ssh\config

-   To set up a host specific configuration in your SSH configuration file, add a section:

```cmd
Host github.com
    IdentutyFile ~/.ssh/my_key_rsa
```

-   This tells SSH to use the my_key_rsa key when connecting to 'github.com'. Its possible to replace 'github.com' with the hostname of the Git server you are connecting to.

-   In case GitHub or BitBucket are used, you may not need to set up any SSH configuration, as these services often use a default SSH key associated with each account.

-   To add a specific SSH key to your agent, you can use the 'ssh-add' command, followed by the path to the private key file:

```cmd
ssh-add ~/.ssh/my_key_rsa
```

This will add the key to SSH agent, which will then be used by Git.

-   It is possible to define a specific SSH key for a specific Git repository by configuring your SSH client to use a different SSH key for that repository. One way to do this, is by creating a new SSH config file entry for the repository and specifying the identity file to use for that repository:
    1. Create a new SSH key pair using 'ssh-keygen', i.e.
```cmd
ssh-keygen -t rsa -b 4096 -C "my_repo_key" -f ~/.ssh/my_repo_key
```
    2. Add the public key '~/.ssh/my_repo_key.pub' to the repository's list of authorized keys. ?????
    3. Create a new SSH config file entry for the repository in '~/.ssh/config'
```cmd
Host <Hostname or IP address of the repository>
    Hostname <Hostname or IP address of the Git Server>
    User git
    IdentutyFile ~/.ssh/my_repo_key
```
    If the repository uses a different port that the default SSH port (22), you can add a 'Port' field to the entry as well.
    4. Clone the repository using the 'ssh' protocol, specifying the repository's hostname in the URL:
```cmd
git clone ssh://my_repo.example.com/path/to/repository
```