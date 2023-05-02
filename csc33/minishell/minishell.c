#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>


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

int valid_cmd(char* prog){
      if (prog == NULL){
            return 0;
      }
      if (strcmp(prog, "exit") == 0)
            exit(0);
      if (prog[0] != '.' && prog[0] != '/'){
            return 0;
      }
      return 1;
}

int main(){

      for(;;) {
            int id;
            int in_fd;
            int out_fd;

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

            
            if (!valid_cmd(prog))
                  continue;

            id = fork();

            if (id != 0){
                  wait(NULL);
            }
            else{
                  if (in){
                        in_fd = open(in, O_RDONLY);
                        dup2(in_fd, STDIN_FILENO);
                        close(in_fd);
                  }
                  if(out){
                        out_fd = open(out, O_CREAT | O_WRONLY, 0666);
                        dup2(out_fd, STDOUT_FILENO);
                        close(out_fd);
                  }
                  execv(prog, args);
                  exit(0);
            }

        }
      
      return 0;
}





