#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <fcntl.h>

#define MAX 200

void read_command(char str []){
      fgets(str, MAX, stdin);
}

char* parse_get_program(char *cmd){
      return strtok(cmd, " \n"); 
}

char* parse_get_in (char *cmd){
      strtok(cmd, "<");
      return strtok(NULL, " \n"); 
}

char* parse_get_out (char *cmd){
      strtok(cmd, ">");
      return strtok(NULL, " \n"); 
}

void parse_get_args(char *args []){
      char *curr;
      int i = 1;
      curr = strtok(NULL , " \n");
      while (curr != NULL){
            if (strcmp(curr, "<") == 0 || strcmp(curr, ">") == 0){
                  break;
            }
            args[i] = curr;
            curr = strtok(NULL , " \n");
            i++;
      }
      args[i] = NULL;
}


int main(){

      for(;;) {
            int id;


            char cmd [MAX];
            char cmdIn [MAX];
            char cmdOut [MAX];
            char *prog;
            char *in;
            char *out;
            char *args [MAX];


            read_command(cmd);
            strcpy(cmdIn,cmd);
            strcpy(cmdOut,cmd);

            prog = parse_get_program(cmd);
            args[0] = prog;
            parse_get_args(args);

            in = parse_get_in(cmdIn);
            out = parse_get_out(cmdOut);

            if (strcmp(prog, "exit") == 0)
                  exit(0);
            
            id = fork();

            if (id != 0){
                  wait(NULL);
            }
            else{
                  if(out){
                        int fd = open(out,"w");
                        dup2(fd, STDOUT_FILENO);
                  }
                  execv(prog, args);
                  exit(0);
            }

        }
            // if (malformed cmd) {
            //       continue
            // }

            // if (prog == 'exit') {
            //       break
            // }

            // parent = fork()

            // if (parent) {
            //       wait()
            // } else {
            //       redirect(in)
            //       redirect(out)
            //       exec(prog, args)
            // }
      return 0;
}





