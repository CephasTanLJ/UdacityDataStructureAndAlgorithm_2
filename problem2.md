# Problem 2: File Recursion
by Cephas Tan Li-Jie
## Assignment description
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) 
that end with ".c"

## Method of implementation
### Base Case:
Identify if the items in the path are files. 
If they are files, check if they end with .c.
If they end with .c, append them to the `target_list`.
return a `target_list` containing the files the end with .c

### Recursive cases:
Identify if the items in the path are files. 
If they are files, check if they end with .c.
If they are directories, use the 'find_files()' recursive function 
to check the contents of the directories.




   
