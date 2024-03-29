# Linux Basics

Linux is an open-source operating system that offers a wide array of tools and commands for managing systems, networking, and programming. Below is an expanded list of essential Linux commands, including file manipulation, system information, networking tools, and a brief introduction to bash scripting.

## Everything Is a File

In Linux, the philosophy that everything is a file simplifies interaction with the system. Files can represent hardware devices, system information, and even running processes. This approach allows users to manipulate almost everything in the system using file-based operations.

## Why Use Linux?

- **Security:** Linux is considered to be a very secure operating system.
- **Stability:** Linux is known for its stability and reliability.
- **Free and Open Source:** You can use and modify Linux without any restrictions.

### File and Text Manipulation

- `cut` - removes sections from each line of files.
- `tr` - translates or deletes characters.
- `zip`/`unzip` - compresses files into zip format or extracts them.
- `head` - outputs the first part of files.
- `tail` - outputs the last part of files.
- `less` - view the contents of a file one page at a time.
- `find` - searches for files in a directory hierarchy.
- `chmod` - changes the file mode (permissions).
- `chown` - changes file owner and group.
- `strip` - discards symbols from object files.
- `shred` - overwrite a file to hide its contents.
- `cmp` - compares two files byte by byte.
- `diff` - compares files line by line.
- `sort` - sorts lines of text files.
- `locate` - finds files by name.
- `grep` - searches for patterns in files.
- `awk` - pattern scanning and processing language.
- `wc` - prints the byte, word, and newline counts for each file.
- `uniq` - filters or reports repeated lines in a file.

### System and Process Management

- `whoami` - prints the current user's name.
- `sudo` - execute a command as another user.
- `passwd` - updates a user's authentication tokens.
- `man` - an interface to the system reference manuals.
- `clear` - clears the terminal screen.
- `useradd`/`adduser` - create a new user or update default new user information.
- `su` - change user ID or become superuser.
- `exit` - exits the shell.
- `systemctl` - controls the systemd system and service manager.
- `history` - displays the command history.
- `reboot` - reboots the system.
- `shutdown` - shuts down the machine.

### Networking and Internet

- `ssh` - secure shell for logging into a remote machine.
- `curl` - transfers data from or to a server. Are primarily HTTP clients used for downloading files from the internet
- `wget` - non-interactive network downloader. Are primarily HTTP clients used for downloading files from the internet
- `ifconfig` - configure a network interface.
- `ip address` - show/update IP addresses.
- `ping` - send ICMP ECHO_REQUEST to network hosts.
- `netstat` - prints network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.
- `ss` - utility to investigate sockets. Is a modern alternative to netstat, it is used to dump socket statistics and displays information in a similar fashion.
- `iptables` - administration tool for IPv4/IPv6 packet filtering and NAT.
- `ip` is a newer replacement for ifconfig, used for showing/updating routing, devices, policy routing, and tunnels.
- `ufw` - Uncomplicated Firewall, a frontend for `iptables`.
- `resolvectl status` - query or change system DNS settings.
  
### Monitoring and Hardware Information

- `uname` - print system information.
- `neofetch` - shows system information with an image.
- `cal` - displays a calendar.
- `free` - displays the amount of free and used memory in the system.
- `df` - report file system disk space usage.
- `htop` - interactive process viewer.
- `kill`/`pkill` - send a signal to a process.

### System Performance Monitoring

- `sar` - collects, reports, or saves system activity information.
- `iostat` - provides statistics for CPU utilization and I/O statistics for devices and partitions.
  
### Package Management

- `apt` - command-line interface for the package management system.
  
### User Information and Help

- `finger` - user information lookup program.
- `whatis` - display one-line manual page descriptions.

## Basic Bash Scripting

Bash scripting allows you to automate tasks in Linux. A bash script is a file containing a series of commands that the bash shell can execute.

### Simple Bash Script Example

```bash
#!/bin/bash
# This is a comment
echo "Hello, World!" # This prints out "Hello, World!"
```
Variables: Used to store information that can be referenced and manipulated.
```bash
name="Linux"
echo $name
```
Control Structures: Such as if-else statements and loops (for, while).
```bash
if [ condition ]; then ... fi
for var in list; do ... done
```
Functions: Reusable pieces of code.
```bash
function name() { ... }
```
User Input: Reading input from the user.
```bash
read varname
```
File Operations: Such as reading from or writing to files.
```bash
echo "text" > file.txt
```
Executing Commands: Use backticks **(`)** or **$()** to execute commands and store their output

## Learning Resources
- **[Linux Documentation](https://linux.die.net/)** - an extensive knowledge base and documentation for Linux, offering detailed manuals for many tools and commands.
- **[Linux File System Explained!](https://www.youtube.com/watch?v=bbmWOjuFmgA)** - a YouTube video explaining the structure and principles of the Linux file system, perfect for visual learners.
- **[60 Linux Commands you NEED to know (in 10 minutes)](https://www.youtube.com/watch?v=gd7BXuUQ91w)** - a quick video course showcasing 60 essential Linux commands that every user should know.