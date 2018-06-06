#!/bin/bash

# using a remote system
ssh <username>@<host>                  # opens a CL session on <host>
scp <username>@<host>:/path/to/file .  # copies a remote file in the current directory
scp file <username>@<host>:/path/      # copies local file into remote directory

# pipes
ls -l /directory | wc -l               # the pipe character (|) sends the output of a command into another
cat file | grep pattern 

# groups of commands
mkdir dir && cd dir                    # && concatenates commands (executed if all previous ones succeed)

# execute tasks in the background
long_running_command &                 # a single & sends the command to a background thread
nohup long_running_command &           # add nohup if you want to keep a log of stdout/stderr