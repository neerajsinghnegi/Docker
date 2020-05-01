import os
import getpass

print("""-------------------------------------------------------------  Password Protected !! -----------------------------------------------------------------
""")

apass = "neeraj"
count=0


while count < 3:
	passwd = getpass.getpass("								Enter Password : ")
	if apass != passwd:
		print("Try Again!!")
		count+=1
	else:
		while True:	
			os.system("clear")

			print("""
							   Welcome to Docker Menu
							  ________________________

								  Images
								  ------
			1 Docker Install		2 Docker Images			2 Download Docker Images		3 Create Image		4 Remove Image

								 Containers
								 ----------
 			4 Show Running Containers	5 Attach Container 			6 Detach Container 	
			7 All Containers		8 Launch Container			9 Stop Container Service		
			10 Start Container Service	11 Delete Container 			12 Show Container IP

								Infrastructure
								--------------
			13 Launch Pre-created Infrastructure					14 Create your own Infrastructure

								   Volume
								   ------
			15 Create Volume			16 See Volumes			
								
								  Settings
								  --------
			17 Yum Configuration 			18 Monitor Docker CPU			19 Active Ports
			
			20 Exit""")

			ch=int(input("Enter your choice. "))
#install docker
			if ch == 1:
				docker_images()
				continue				
			elif ch == 2:
				docker_pull()
				continue
			elif ch == 3:
				docker_create_image()
				continue
#remove
			elif ch == 4:
				docker_remove_image()
				continue
			elif ch == 4:
				docker_running_con()
				continue			
			elif ch == 5:
				docker_attach()
				continue
			elif ch == 6:
				docker_detch()
				continue
			elif ch == 7:
				docker_all_con()
				continue
			elif ch == 8:
				new_con()
				continue
			elif ch == 9:
				docker_stop()
				continue
			elif ch == 10:
				docker_start()
				continue
			elif ch == 11:
				remove_con()
				continue
			elif ch == 12:
				con_ip()
				continue
			elif ch == 13:
				pre_infrastructure()
				continue
			elif ch == 14:
				#own infra
				continue
			elif ch == 15:
				create_vol()
				continue
			elif ch == 16:				
				show_vol()
				continue
			elif ch == 17:
				yum_configure()
				continue
			elif ch == 18:
				docker_cpu()
				continue			
			elif ch == 19:
				##active port
			elif ch == 20:
				break
else:
	print("Try again !", end="")
	x=input("Enter to exit...")

def :
def docker_install():	
def :
def :
def :
def :
def :
def :
def docker_start():
def :
def docker_terminate():
def :
def :
def :
def :
def remove_all_con():
def :
def :
def :
def :
def :




def yum_configure():
	os.system("cp epel.repo dock.repo  epel-playground.repo epel-testing.repo root.repo rpmfusion-free-updates.repo rpmfusion-free-updates-testing.repo /etc/yum.repos.d/ ")
	print("Your yum is configured now check it by 'yum repolist' command.")
	x=input("Enter to continue...")

def docker_install():
	os.system("yum install docker-ce --nobest -y")
	os.system("systemctl start docker")
	os.system("systemctl enable docker")
	os.system("firewall-cmd --zone=public --add-masquerade --permanent")
	os.system("firewall-cmd --zone=public --add-port=80/tcp")
	os.system("firewall-cmd --zone=public --add-port=443/tcp")
	os.system("firewall-cmd --reload")
	os.system("systemctl restart docker")
	os.system("yum install httpd")
	os.system("systemctl enable httpd")
	print("Docker-CE successfully installed.")
	x=input("Enter to continue...")
def docker_pull():
	imgname=input("Enter image with version. for ex- centos:7")
	os.system("docker pull {}".format(imgname))
	print("{} image downloaded successfully.".format(imgname))
	x=input("Enter to continue...")

def docker_images():
	os.system("docker images ls")
	x=input("Enter to continue...")

def docker_create_image():
	own_image = input("Give name to your own image with version. for ex- myimage:v1")
	which_image = input("Enter name of your container.")
	os.system("docker commit {0}{1}".format(which_image,own_image))	
	x=input("Enter to continue...")

def docker_remove_image():
	rimage = input("Image name with version. for ex- myimage:v1")
	os.system("docker rmi {}".format(rimage))
	print("{} image successfully removed.".format(rimage))
	x=input("Enter to continue...")

def docker_running_con():
	os.system("docker ps")

def docker_all_con():
	os.system("docker ps -a")
	x=input("Enter to continue...")

def docker_start():
	start = input("Container Name : ")
	os.system("docker start {}".format(start))
	print("{} container start successfully.".format(start))
	x=input("Enter to continue...")

def docker_stop():
	stop = input("Container Name : ")
	os.system("docker stop {}".format(stop))
	print("{} container stopped successfully.".format(stop))
	x=input("Enter to continue...")

def docker_terminate():
	terminate = input("Container Name : ")
	os.system("docker stop {}".format(terminate))
	print("{} container terminated successfully.".format(terminate))
	x=input("Enter to continue...")

def new_con():
	cname=input('Give Name to Your New Container.')
	iname = input('Enter image name with version. for ex- centos:7')
	os.system("docker run -dit --name {} {}".format(cname,iname))
	print("{} container created successfully.".format(cname))
	x=input("Enter to continue...")

def docker_attach():
	attach = input("Container name to attach.")
	os.system("docker attach {}".format(attach))
	x=input("Enter to continue...")

def docker_detch():
	print("HEllo")

def remove_con():
	remove = input("Container Name : ")
	os.system("docker rm -f {}".format(remove))
	print("{} container removed successfully.".format(remove))
	x=input("Enter to continue...")

def remove_all_con():
	print("Warning not recommended.")
	os.system("docker -f rm $(docker ps -a)")
	print("successfully removed all containers.")
	x=input("Enter to continue...")

def show_vol():
	os.system("docker volume ls")
	x=input("Enter to continue...")

def create_vol:
	vol=input("volume name.")
	os.system("docker create volume {}".format(vol))
	print("successfully created volume. {}".format(vol))
	x=input("Enter to continue...")
	
def con_ip():
	con_name=input("Container name.")
	os.system("docker inspect --format {{.NetworkSteetings.IPAddress}} {}".format(con_name))
	x=input("Enter to continue...")

def docker_cpu():
	os.system("watch -n 1 free -m")
	x=input("Enter to continue...")

def pre_infrastructure():
	os.system(' curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
	os.system("chmod +x /usr/local/bin/docker-compose")
	os.system("cp docker-compose.yml /") 
	os.system("cd / ")
	os.system("mkdir /infrastructure")
	os.system("cd /infrastructure/")
	os.system("pwd")
	os.system("mv ../docker-compose.yml .")
	os.system("docker-compose up -d")
	print("your wordpress site is ready to use. for ex- 192.168.43.139:8080")
	x=input(""""

Details :
	MYSQL_ROOT_PASSWORD : rootpass
	MYSQL_USER : neeraj
	MYSQL_PASSWORD : redhat
	MYSQL_DATABASE : db

	Container : neeraj
	Image : mysql:5.7

Press Enter to continue..."""")

"Hello"





