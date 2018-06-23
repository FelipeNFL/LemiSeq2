if [ "$1" = "build" ]
then
    docker-compose -f bioprocess/docker-compose.yml up --build & docker-compose -f auth/docker-compose.yml up --build
else
    docker-compose -f bioprocess/docker-compose.yml up & docker-compose -f auth/docker-compose.yml up
fi