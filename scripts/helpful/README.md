# Automatic-Isolation-and-Analysis-Environment
## Helpful Utilities' Script

<br></br>
Three helpful Docker scripts:
- <code>installDocker.sh</code> - install Docker dependencies.<br>
Please copy & paste those command in your environment terminal in order to install Docker.

- <code>createDockerFile.sh</code> - create a Docker Image. Note that you need to have a <code>dockerfile</code>.

- <code>stopDocker.sh</code> - commands to stop runnings Dockers. Fill the script with the fit <code><CONTAINER_ID></code> and <code><IMAGE_ID></code> which you want to stop.<br>
You can find those IDs by running the following commands:<br>
<code>sudo docker ps -a</code><br>
<code>sudo docker image list</code>

