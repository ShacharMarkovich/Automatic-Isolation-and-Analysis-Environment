#install docker-ce:
#First, update existing list of packages
sudo apt-get update;

#install a few prerequisite packages which let apt use packages over HTTPS
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common;

#Then add the GPG key for the official Docker repository to your system:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -;

#Add the Docker repository to APT sources:
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable";

#update existing list of packages again
sudo apt update;

#Make sure you are about to install from the Docker repo instead of the default Ubuntu repo:
apt-cache policy docker-ce;

#install docker from docker repo
sudo apt install docker-ce;

#check if daemon started:
sudo service docker start;
#END of install docker-ce


#install additional packages for the project:
sudo apt-get install -y apt-file;
