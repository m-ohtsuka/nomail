#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <dirent.h>
#include <errno.h>

int main(int argc, char **argv){

    DIR *dir;
    struct dirent *dirent;
    int i;

    if(argc != 4){
	fputs("usage: noqueue sleep nosend spool\n", stderr);
	exit(1);
    }

    while(1){
	if(!(dir = opendir(argv[3]))){
	    perror("Can't open directory");
	    exit(1);
	}
	for(i = 0; (dirent = readdir(dir)) != NULL ; i++)
	    ;
	closedir(dir);
	if(i != 2){
	    if(fork()){
		wait();
	    }else{
		execl(argv[2], NULL);
		perror("Can't exec nosend process");
		_exit(1);
	    }
	}
	sleep(atoi(argv[1]));
    }
}
