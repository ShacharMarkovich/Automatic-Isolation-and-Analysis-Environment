#create dockerfile
#build dockerfile image
sudo docker build -t dockerfile .

#run image and detach
sudo docker run -dit --name debug_container dockerfile

#attach to container
sudo docker attach debug_container

#start the container
sudo docker start debug_container


###
#get all dependencies from executable file linux
readelf -d ./test | grep 'NEEDED'

#get arch of executable file
file "path_to_file"