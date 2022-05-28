


extern "C" {

#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <stdarg.h>
//#include <values.h> // obsolete
// https://stackoverflow.com/questions/21878684/hot-to-install-values-h-header-c-c-on-cygwin
#include <float.h> // trocar values.h por float.h
#include <string.h>
#include <math.h>
#include <malloc.h>


int decomp(int n, int *w, int *x, int c);

long decompL(int n, long *w, int *x, long c);
}
