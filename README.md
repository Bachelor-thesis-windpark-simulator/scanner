# README

Project for the course "Geoinformatics 8: Perspectives" at the ifgi Münster.
Based mainly upon [CityScoPy](https://github.com/CityScope/CS_CityScoPy)

Currently only working on Linux machines.

## How to use
Before starting the containers check the mounted video devices with `ls /dev | grep video` and adjust the docker-compose files according to your system and set the correct cameraID for the camera you want to use in cityscopy.json  


1. Run `xhost +local:docker`
2. If a new camera is used run `docker compose -f docker-compose.calibrate.yml up` and select the corners of the grid. The run `docker compose -f docker-compose.calibrate.yml down`
3. Run `docker compose up`
4. To stop the application do a keyboard interrupt and run `docker compose down`