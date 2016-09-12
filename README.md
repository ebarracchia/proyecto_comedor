# proyecto_comedor #
Proyecto OpenCV.

# Links #
## Git: How to use ##
http://rogerdudler.github.io/git-guide/  

## Python & OpenCV: Edit video ##
https://solarianprogrammer.com/2015/06/04/opencv-video-editing-tutorial/  


# GIT #
## How to clone ##
user@machine:~/Desarrollos$ git clone   https://github.com/ebarracchia/proyecto_comedor.git  
Cloning into 'proyecto_comedor'...  
remote: Counting objects: 3, done.  
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0  
Unpacking objects: 100% (3/3), done.  
Checking connectivity... done.  

## How to update from github (From Server) ##
** Have some updates... **  
user@machine:~/Desarrollos/proyecto_comedor$ git pull origin master  
remote: Counting objects: 3, done.  
remote: Compressing objects: 100% (2/2), done.  
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0  
Unpacking objects: 100% (3/3), done.  
From https://github.com/ebarracchia/proyecto_comedor  
   branch            master     -> FETCH_HEAD  
   73dd393..def7f4a  master     -> origin/master  
Updating 73dd393..def7f4a  
Fast-forward  
 README.md | 8 ++++++++  
 1 file changed, 8 insertions(+)  

** No updates... **  
user@machine:~/Desarrollos/proyecto_comedor$ git pull origin master  
From https://github.com/ebarracchia/proyecto_comedor  
   branch            master     -> FETCH_HEAD  
Already up-to-date.  

## How to update into github (To Server) ##
user@machine:~/Desarrollos/proyecto_comedor$ git add README.md  
user@machine:~/Desarrollos/proyecto_comedor$ git commit -m "Remover caracteres"  
[master 53a09ac] Remover caracteres  
 1 file changed, 3 insertions(+), 3 deletions(-)  
user@machine:~/Desarrollos/proyecto_comedor$ git push origin master  
Username for 'https://github.com': ebarracchia  
Password for 'https://ebarracchia@github.com':   
Counting objects: 3, done.  
Delta compression using up to 2 threads.  
Compressing objects: 100% (2/2), done.  
Writing objects: 100% (3/3), 294 bytes | 0 bytes/s, done.  
Total 3 (delta 1), reused 0 (delta 0)  
remote: Resolving deltas: 100% (1/1), completed with 1 local objects.  
To https://github.com/ebarracchia/proyecto_comedor.git  
   e9b2480..53a09ac  master -> master  
