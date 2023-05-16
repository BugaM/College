#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>


#define MAX 200

// Function to read input from the user
void read_command(char str []){
      fgets(str, MAX, stdin);
}

// Tokenize program part of input
char* parse_get_program(char *cmd){
      return strtok(cmd, " \n"); 
}

// Tokenize input redirection target of input
char* parse_get_in (char *cmd){
      strtok(cmd, "<");
      return strtok(NULL, " \n"); 
}

// Tokenize output redirection target of input
char* parse_get_out (char *cmd){
      strtok(cmd, ">");
      return strtok(NULL, " \n"); 
}

char* parse_get_pipe (char *cmd){
      strtok(cmd, "|");
      return strtok(NULL, " \n"); 
}

// Tokenize program arguments of input
void parse_get_args(char *args []){
      char *curr;
      int i = 1;
      curr = strtok(NULL , " \n");
      while (curr != NULL){
            // get arguments untill redirections
            if (strcmp(curr, "<") == 0 || strcmp(curr, ">") == 0 || strcmp(curr, "|") == 0){
                  break;
            }
            args[i] = curr;
            curr = strtok(NULL , " \n");
            i++;
      }
      // last element must be NULL
      args[i] = NULL;
}

// Check if valid program
int valid_cmd(char* prog){
      if (prog == NULL){
            return 0;
      }
      return 1;
}

// Check if should exit minishell
int should_exit(char * prog){
      if (strcmp(prog, "exit") == 0)
            return 1;
      return 0;
}

void print_starting_message(){
      printf("Running minishell project\n");
      printf("Developed by Marcelo Buga Martins da Silva - ITA COMP 24\n");
}

void print_cmd(){
      printf("cmd> ");
}

int main(){
      // process id
      int id;

      // in and out folders
      int in_fd;
      int out_fd;

      // cmd and cmd copies
      char cmd [MAX];
      char cmdIn [MAX];
      char cmdOut [MAX];
      char cmdPipe [MAX];

      // tokenized parts of cmd
      char *prog;
      char *in;
      char *out;
      char *pipe_prog;
      char *args [MAX];
      char *args_pipe [MAX];

      int pipe_fd [2];

      print_starting_message();

      for(;;) {
            print_cmd();            

            read_command(cmd);
            strcpy(cmdIn,cmd);
            strcpy(cmdOut,cmd);
            strcpy(cmdPipe,cmd);

            prog = parse_get_program(cmd);
            // add prog as first argument
            args[0] = prog;
            parse_get_args(args);

            in = parse_get_in(cmdIn);
            out = parse_get_out(cmdOut);
            pipe_prog = parse_get_pipe(cmdPipe);
            args_pipe[0] = pipe_prog;
            parse_get_args(args_pipe);

            
            if (!valid_cmd(prog))
                  continue;
            
            if (should_exit(cmd))
                  exit(0);
            
            id = fork();

            if (id != 0){
                  // wait for child to end
                  wait(NULL);
            }
            else{
                  // child process

                  // redirect input
                  if (in){
                        in_fd = open(in, O_RDONLY); // read only
                        dup2(in_fd, STDIN_FILENO);
                        close(in_fd);
                  }
                  // redirect output
                  if(out){
                        out_fd = open(out, O_CREAT | O_WRONLY | O_TRUNC, 0666); // create if needed, write, overwrite
                        dup2(out_fd, STDOUT_FILENO);
                        close(out_fd);
                  }
                  if (pipe_prog){
                        pipe(pipe_fd);
                        id = fork();
                        if (id == 0){ // child
                              close(pipe_fd[0]);
                              dup2(pipe_fd[1], STDOUT_FILENO);
                              execv(prog, args);
                              exit(0);
                        }
                        else{
                              wait(NULL);
                              close(pipe_fd[1]);
                              dup2(pipe_fd[0], STDIN_FILENO);
                              execv(pipe_prog, args_pipe);
                        }

                  }
                  else{
                        execv(prog, args);
                        exit(0);
                  }
            }
        }

      return 0;
}





