# README #

### What is this repository for? ###

* BitBoard gives users the ability to monitor cryptocurrencies, portfolios, news, and friends
* This repository contains the code for BitBoard, which is written using the Python framework Django and is run using Docker
* Version 1.0

### How do I get set up? ###

### --- Install Docker --- ###
  * Make sure you have 'Docker Compose' installed. Download it from here, https://docs.docker.com/compose/install/
  
### --- Clone BitBoard Source Code --- ###
  * Once installed, clone the BitBoard repository using the following command:
    * git clone https://joastern@bitbucket.org/joastern/bitboard.git
  * Then, on the command line, move into the BitBoard direcotry using the following command:
    * $ cd bitboard

### --- Start Docker --- ###
  * To run BitBoard, enter the following commands:
    * $ docker-compose build
    * $ docker-compose up

  * If everything worked you should be able to succesfully go to:
    * http://localhost:8000
  * If successful, BitBoard should be working!
  
### -- Python Interpretor With Docker -- ###
  * The Python Interpretor allows developers to test Python, it is mainly used here to test the Django Models
  * Enter the following command:
    * $ docker exec -it bitboard_web_1 bash
  * then enter:
    * $ python manage.py shell

### -- Stop Docker -- ###
  * To stop BitBoard
  * Enter ^C (Control-C) to stop the localhost server
  * Then to stop docker, enter the following command:
    * $ docker-compose down

### Who do I talk to? ###

### --- Product Owner --- ###
  * joastern@ucsc.edu

### --- Developers --- ###
  * Fransico Braga -- fbraga@ucsc.edu
  * Guita Vahdatinia -- gvahdati@ucsc.edu
  * Haonan -- hxu24@ucsc.edu
  * Joshua Stern -- joastern@ucsc.edu
  * Matt Cruz -- maaucruz@ucsc.edu
