# Logs Analysis
## Project Description

This Project contains analysis of news database and code has been written in language python3 and postgresql database. 

To describe it slightly deeper, this project gives three different analysis result on news database. Project aims to analyse news database and display result of following:
1. The most popular three articles of all time
2. The most popular article authors of all time
3. Days on which more than 1% of requests led to errors

**Requirements:**
Virtual machine environment:
1. Vagrant
2. Virtualbox
Virtual machine can be run using [Vagrant](https://www.vagrantup.com/downloads.html "Vagrant") and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1 "VirtualBox") which you can download and install from here. Find the version for your operating system. Also, VirtualBox does not require launch because Vagrant will do that. After successful installation, running a command **vagrant up** will start virtual machine and once you are up with virtual machin you can log in using **vagrant ssh**.

Or enviornment of your choice with following:
1. Python3
2. PostgreSQL
3. psycopg2

**Set-up the news database:**
* User can follow this steps while using Vagrant:
from psql console create news database by typing
CREATE DATABASE news;
Also get the newsdata.sql file with the database schema and data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip "Get News database Zip file").
Unzip this file after downloading. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
* User can follow above steps for getting news database ready while using their choosen environment.

After that run this log_analysis.py and you will get result on the terminal.
