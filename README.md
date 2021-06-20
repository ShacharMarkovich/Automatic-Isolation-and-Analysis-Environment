# Automatic Isolation and Analysis Environment
## Where am I now...? What is in this project?
Today, in the security world we often deal with files that we are not sure if they are malicious or not. Until this day, in order to analysis and research those kinds of files, we would set up a virtual machine, usually slow and nerve-wracking, in which we would install the software and research it. We were developed a much more effective method to do this – with an isolated Docker.
In this article we aim to answer our research questions:
1)	What is Docker and how it is different from Virtual Machine?
2)	What are files' dependencies and how to discover them?
3)	How to set up an isolated Docker environment which give the opportunity of safe malware research in an efficient way?
4)	Why Docker is more efficient from a Virtual Machine?
 
## How to use

For instructions type: <br>
<code>python3 scripts/run.py -h</code><br>
Exmaple:<br>
<code>python3 scripts/run.py scripts/exmaple/malware1 "nano gcc radare2 gbd" exmapleDockerImag</code><br>
We are suggest to use <code>nano gcc radare2 gbd</code> utilities in in your Docker in order to enable easy files creation, compiling, debugging and decompling, respectively.<br>
Running <code>run.py</code> will do all the job for you.

## Folders
In <code>documents</code> you will find:
- Project's report with full details.
- Project's presentaion.

In <code>scripts</code> you will find:
- <code>run.py</code> - the main and only script for create the Isolation & Analysis Environment.
- In <code>exmaple & helpful</code> sub-folder: read their <i>README</i> file for more help.
