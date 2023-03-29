#include <string.h>
#include <stdio.h>

#define MAX 200

void read_command(char str []){
      fgets(str, MAX, stdin);
}

char* parse_get_program(char *cmd){
      return strtok(cmd, " "); 
}

char* parse_get_in (){
      return strtok(NULL, "< "); 
}

char* parse_get_out (){
      return strtok(NULL, "> "); 
}

void parse_get_args(char *args []){
      char *curr;
      int i = 0;
      curr = strtok(NULL , " ");
      while (curr != NULL){
            args[i] = curr;
            curr = strtok(NULL , " ");
            i++;
      }
}


int main(){

      for(;;) {
            char cmd [MAX];
            char *prog;
            char *in;
            char *out;
            char *args [MAX];
            read_command(cmd);
            prog = parse_get_program(cmd);
            printf("%s \n", prog);
            in = parse_get_in();
            printf("%s\n", in);
            out = parse_get_out();
            printf("%s\n", out);
            parse_get_args(args);
            printf("%s%s\n", args[0], args[1]);

            // in = parse_get_stdin(cmd);
            // out = parse_get_stdout(cmd)

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
      }
      return 0;
}





