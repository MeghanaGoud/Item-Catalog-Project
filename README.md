# Item-Catalog
 An application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items. 
## Prerequisites
Install virtual machine(vagrant)
### Installation and Execution
This project makes use of the Linux-based virtual machine (VM). This will give you the PostgreSQL database and support software needed for this project, use tools called Vagrant and VirtualBox to install and manage the VM. VirtualBox is the software that actually runs the virtual machine download it https://www.virtualbox.org/wiki/Downloads
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem download it https://www.vagrantup.com/downloads.html
After the successful installation of vagrant run 
```
Vagrant --version
Vagrant 1.9.8
```
* Usage
after that download the VM configuration and navigate to your vagrant directory using `cd`. Inside the vagrant directory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. 
When `vagrant up` is finished running, run `vagrant ssh` to log in to your newly installed Linux VM!
```
The shared directory is located at /vagrant
To access your shared files: cd /vagrant
Last login: Thu Sep 28 05:50:54 2017 from 10.0.2.2
vagrant@vagrant:~$
``` 
navigate to your vagrant by `cd /vagrant` you'll get the command line like
```
vagrant@vagrant:~$ cd /vagrant
vagrant@vagrant:/vagrant$
```
after that install the required python libraries. To install pip package in ubuntu try the given commands
```
sudo easy_install pip
	or
sudo apt-get install python-pip
```
Install your required packages for your python file 
### Execution
Maintain all the html pages in the templates folder and css files in static folder
#### Project main files
* dbtables.py-caintains the database tables
* catitems.py-contains the items and categories
* project.py- main python file
#### Run the application 
Open your project folder and launch virtual machine as shown above and type `python project.py` and in your browser url place `http://localhost:5000 or http://localhost:5000/categories` your main page will be loaded.The homepage displays all current categories with the latest added items.
Select a specific category, it shows you all the items available for that category.
Selecting a specific item shows you specific information about that item.

Inorder to add, update, or delete item information user have to login `http://localhost:5000/login`. Users are able to modify only those items that are created by themselves.the users can log in by using their google account or facebook.
