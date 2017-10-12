# README #

### What is this repository for? ###

* BitBoard gives users the ability to monitor their favorite cryptocurrencies, portfolio, news, and friends
* This repository is the code for BitBoard, which is written using the Python framework Django and is run using Docker
* Version 1.0


### How do I get set up? ###

### -- Installing Docker -- ###
  * Make sure you have 'Docker Compose' installed. Download it from here, https://docs.docker.com/compose/install/
  * Once installed, clone the BitBoard repository by the following command,
    * git clone https://joastern@bitbucket.org/joastern/bitboard.git
  * Then, on the command line
    * $ cd bitboard

### -- To Start Docker -- ###
  * Run,
    * $ docker-compose build
    * $ docker-compose up

  * If everything worked you should be able to succesfully go to,
    * http://localhost:8000
  * BitBoard should be working if successful
  
### -- To Use Python Interpretor With Docker -- ###
  * Enter on the command line,
    * $ docker exec -it bitboard_web_1 bash
  * then enter, 
    * $ python manage.py shell


### -- To Stop Docker -- ###
  * Enter ^C (Control-C) to stop the localhost server
  * Then to stop docker, enter
    * $ docker-compose down

### Who do I talk to? ###

### Product Owner ###
  * joastern@ucsc.edu

### Developers ###
  * Matt Email
  * Guita Email
  * Haonan Email
  * Fransico Email
  * joastern@ucsc.edu
