# Logs Analysis Project

  This project is to provide an answers to three questions:
### What are the most popular three articles of all time?
### Who are the most popular article authors of all time?
### On which days did more than 1% of requests lead to errors?

---
## Tools needed to run this project
  [python 3.7](https://www.python.org/downloads/), [Vagrant 2.2.0](https://www.vagrantup.com/), [VirtualBox5.1.38](https://www.virtualbox.org/).

### How to setup & run vagrant
  To setup the vagrant clone this repository: [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)
  then using the terminal inside the vagrant subdirectory, run the command `vagrant up` to intall the Linux VM.
  then run `vagrant ssh` to access the LinuxVM.
  to access vagrant subdirectory after Runing `vagrant ssh` change directory to `cd /vagrant`.

---
## Runing the Datebase
  First you need to download the database for this project [newsdata.db](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) unzip this file then Put it into the vagrant directory.
  We are using `PostgreSQL` in this project, To load the data run `psql -d news -f newsdata.sql` inside vagrant VM.


---
## **NOTE:**
### Source code written by python3 named 'logs-analysis.py'.
### an example of the output 'output.txt' file.
### README.md file.
you need to download the database [newsdata.db](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
