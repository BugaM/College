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

void parse_get_pipe_args(char *args [][MAX], int current){
      char *curr;
      int i = 1;
      curr = strtok(NULL , " \n");
      while (curr != NULL){
            // get arguments untill redirections
            if (strcmp(curr, "<") == 0 || strcmp(curr, ">") == 0 || strcmp(curr, "|") == 0){
                  break;
            }
            args[current][i] = curr;
            curr = strtok(NULL , " \n");
            i++;
      }
      // last element must be NULL
      args[current][i] = NULL;
}

int parse_pipe(char *cmd, char *pipe_progs [], char *args_pipe[][MAX]){
      char *curr;
      int i = 0;
      curr = parse_get_pipe(cmd);
      while (curr != NULL){
            // get arguments untill redirections
            if (strcmp(curr, "<") == 0 || strcmp(curr, ">") == 0 || strcmp(curr, "|") == 0){
                  break;
            }
            pipe_progs[i] = curr;
            parse_get_pipe_args(args_pipe, i);
            args_pipe[i][0] = curr;
            curr = strtok(NULL , " \n");
            i++;
      }
      // last element must be NULL
      pipe_progs[i] = NULL;
      return i - 1;
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
      char *pipe_progs[MAX];
      char *args [MAX];
      char *args_pipe [MAX][MAX];

      int pipe_fd [MAX];
      int pipe_number;

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
            pipe_number = parse_pipe(cmdPipe, pipe_progs, args_pipe);

            
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
                  int i;
                  if (pipe_progs[0]){
                        pipe(pipe_fd);
                        id = fork();
                        if (id == 0){ // child
                              dup2(pipe_fd[1], STDOUT_FILENO);
                              // close(pipe_fd[0]);
                              execv(prog, args);
                              exit(0);
                        }
                        dup2(pipe_fd[0], 0);
                        close(pipe_fd[1]);
                        for(i=0; i< pipe_number; i++)
                        {
                              pipe(pipe_fd);
                              id = fork();
                              if (id == 0) {
                                    dup2(pipe_fd[1], STDOUT_FILENO); // remap output back to parent
                                    execv(pipe_progs[i], args_pipe[i]);
                                    exit(0);
                              }

                              // remap output from previous child to input
                              dup2(pipe_fd[0], STDIN_FILENO);
                              close(pipe_fd[1]);
                        }
                        execv(pipe_progs[i], args_pipe[i]);
                        exit(0);
                  }
                  else{
                        execv(prog, args);
                        exit(0);
                  }
            }
        }

      return 0;
}





