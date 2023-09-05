MySQL is a relational database management system based on the Structured Query Language, for accessing and managing records in the database

#MySQl-WHAT YOU NEED TO KNOW:
What is a primary-replica cluster
MySQL primary replica setup
How to Build a robust database backup strategy

#LEARNING OOBJECTIVES
What is the main role of a database
What is a database replica
What is the purpose of a database replica
Why database backups need to be stored in different physical locations
What operation should you regularly perform to make sure that your database backup strategy actually works

#mysql5.7 installation guide:
visit https://dev.mysql.com and copy the PGP PUBLIC KEY to your clipboard
create a new file in your terminal with a .key extension and paste the PGP PUBLIC KEY and save.
then;
$sudo apt-key add name_of_file.key 
OK
# adding it to the apt repo
$ sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'

# updating the apt repo to add the url i added earlier
$ sudo apt-get update

# check your available versions
$ sudo apt-cache policy mysql-server
mysql-server:
  Installed: (none)
  Candidate: 8.0.31-0ubuntu0.20.04.2
  Version table:
     8.0.31-0ubuntu0.20.04.2 500
        500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages
     8.0.31-0ubuntu0.20.04.1 500
        500 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages
     8.0.19-0ubuntu5 500
        500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 Packages
     5.7.40-1ubuntu18.04 500
        500 http://repo.mysql.com/apt/ubuntu bionic/mysql-5.7 amd64 Packages

# Now install mysql 5.7.*
$ sudo apt-get install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7* -y

#project task
#creating a user and granting priviliges in mysql
'''mysql
$sudo mysql -u root -p
password:

mysql> CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

mysql>GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

mysql>FLUSH PRIVILEGES;'''

##Creating database, Tables and adding Data to the Tables

mysql> CREATE DATABASE db_name_;

--verify if database is created
mysql> SHOW DATABASES;

mysql> USE db_name;

mysql> CREATE TABLE table_name(
->col_1 data_type,
->col_2 data_type,
->col_3 data_type,
->col_4 data_type,
->);

mysql> INSERT INTO table_name VALUES (val_1, val_2);

mysql> GRANT SELECT ON db_name.tb_name TO 'user_name'@'host_name';

mysql> FLUSH PRIVILIGES

--verify if data was added successfully

mysql> USE db_name;

mysql>SELECT * FROM table_name;
'''

#Setting up mysql REplication

-create replication user and grant replication privilige

mysql> CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_user_pwd';

mysql> GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

mysql> GRANT SELECT ON mysql.user TO 'user_name'@'host_name';

mysql> FLUSH PRIVILEGES;

mysql> exit

navigate to sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf and comment the bind address and add these lines

#By default we only accept connections from localhost
#bind-address = 127.0.0.1

server-id = 1
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = db_name

-restart mysql
sudo service mysql restart

#next log into mysql server to retrieve the binary log file name and position on the primary server web-01 

$sudo mysql -u root -p
password:

mysql> SHOW MASTER STATUS;

+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000001 |      154 | db_name      |                  |                   |
+------------------+----------+--------------+------------------+-------------------+

--store this binary log to later configure the replica

#log into the replica server web-02 and edit the config file
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf

server-id = 2
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = db_name_from_master_mysql-server
relay_log = /var/log/mysql/mysql-relay-bin.log

$sudo service mysql restart

-login to mysql server in replica to configure replication

$sudo mysql -u root -p

mysql> CHANGE MASTER TO
MASTER_HOST='source_host_name',
MASTER_USER='replication_user_name',
MASTER_PASSWORD='replication_password',
MASTER_LOG_FILE='recorded_log_file_name',
MASTER_LOG_POS=recorded_log_position;

mysql> START SLAVE;

mysql> exit

- enable incoming connection to port 3306 and restart mysql server

$ sudo ufw allow 3306
$ sudo service mysql restart
       
