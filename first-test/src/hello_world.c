#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>

int count(const char *str){
    int wc=0;
    int inside=0;
    while (*str) {
        if (isspace(*str)){
            if (inside){
                wc++;
                inside=0;
            }
        } else {
            inside=1;
        }
    str++;
    }

    if(inside){
        wc++;
    }
    return wc;
}

int main(){
    const char *str = "Hello World";
    printf("%s\n", str);
    clock_t start = clock();
    int wc=count(str);
    clock_t end = clock();
    double duration = (double)(end-start)/CLOCKS_PER_SEC;
    printf("Hello World contains %i words\n", wc);
    printf("Execution time: %f sec\n", duration);
    return 0;
}