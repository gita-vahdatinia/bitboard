# README #

### What is this repository for? ###

* BitBoard gives users the ability to monitor cryptocurrencies, portfolios, news, and friends
* This repository contains the code for BitBoard, which is written using the Python framework Django and is run using Docker
* Version 1.0

### How do I get set up? ###

### --- Installing Docker --- ###
  * Make sure you have 'Docker Compose' installed. Download it from here, https://docs.docker.com/compose/install/
  * Once installed, clone the BitBoard repository using the following command:
    * git clone https://joastern@bitbucket.org/joastern/bitboard.git
  * Then, on the command line, move into the BitBoard direcotry using the following command:
    * $ cd bitboard

### --- To Start Docker --- ###
  * To run BitBoard, enter the following commands:
    * $ docker-compose build
    * $ docker-compose up

  * If everything worked you should be able to succesfully go to:
    * http://localhost:8000
  * If successful, BitBoard should be working!
  
### -- To Use Python Interpretor With Docker -- ###
  * The Python Interpretor allows developers to test Python, it is mainly used here to test the Django Models
  * Enter the following command:
    * $ docker exec -it bitboard_web_1 bash
  * then enter:
    * $ python manage.py shell


### -- To Stop Docker -- ###
  * To stop BitBoard
  * Enter ^C (Control-C) to stop the localhost server
  * Then to stop docker, enter the following command:
    * $ docker-compose down

### Who do I talk to? ###

### --- Product Owner --- ###
  * joastern@ucsc.edu

### --- Developers --- ###
  * Matt Email
  * Guita Email
  * Haonan Email
  * Fransico Email
  * joastern@ucsc.edu
