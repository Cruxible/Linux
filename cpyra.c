#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void function1() {
    char command[50];
    strcpy( command, "python3 app.py" );
    system(command);
}

void function2() {
    char command[50];
    strcpy( command, "./compiler" );
    system(command);
}

int main(int argc, char *argv[]) {
    char call[100];
    char s[100];
    char *p=getenv("USER");
    char command[50];
    
    if(p==NULL) return EXIT_FAILURE;
    strcpy( command, "clear" );
    system(command);
    printf(" C\n ___  _   _ ____ ____\n |__]  \\_/  |__/ |__|\n |      |   |  \\ |  |\n _______________________\n\n");
    printf("  _%s\n", getcwd(s, 100));
    printf(" (__%s__): ", p);
    scanf("%s", call);
    if (strcmp(call, "network") == 0) {
        chdir("/home/ioannes_main/pyra_env/pyra_network");
        // printing current working directory
        printf("%s\n", getcwd(s, 100));
        // after chdir is executed
        function1();
    } else if (strcmp(call, "compiler") == 0) {
        chdir("/home/ioannes_main/pyra_env/pyra_exes");
        // printing current working directory
        printf("%s\n", getcwd(s, 100));
        // after chdir is executed
        function2();
    } else {
        printf(" Invalid call\n");
    }

    return 0;
}