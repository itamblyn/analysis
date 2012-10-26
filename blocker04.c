/* Blocking analysis written by B. Militzer - to compile, type "gcc -lm blocker04.c"
*/ 

#include <stdio.h> 
#include <stdlib.h> 
#include <math.h> 
#include <string.h>

#define length 1000
#define list_max 100000
char parameter_filename[length];

double x[list_max];

void readin( int argn, char *arg[],int *n) {
   FILE* tmp;
   char ss[length];
   char *sc;
   int ic,is,il,col;

   if (argn < 2 || argn > 3) {
     printf("Use blocker filename [column default=1]\n\n");
     exit(1);
   } 

   strcpy(parameter_filename,arg[1]);
   col = 1;
   if (argn==3) {
     col = atoi(arg[2]);
   }

   tmp=fopen(parameter_filename,"r");
   if (tmp==NULL) {
      printf("Cannot open the parameter file %s!\n\n",
             parameter_filename);
      exit(1);
   }

   il = 1;
   is = 0;
   while ((fgets(ss,length-1,tmp) != NULL) && (is<list_max)) {
     if (ss[0] != '#' ) {
       sc=strtok(ss," ");
       /*       printf("%d %s\n",is,sc); */

       ic=1;
       while (ic<col && sc!=NULL) {
	 sc=strtok(NULL," ");
	 /*	 printf("%d %d %s\n",is,ic,sc); */
	 ic++;
       }
       /*       ii=sscanf(ss,"%d%d%d%lf",&i1,&i2,&i3,&(x[is]));  */
       /*       ii=sscanf(ss,"%d%lf",&i1,&(x[is]));              */
       if (sc==NULL) {
	 printf("Not enough columns in line %d. Line skipped\n",il);
       } else {
	 sscanf(sc,"%lf",&(x[is]));
	 /*	 printf("Data value loaded %d %.10lf\n",is+1,x[is]);*/
	 is++;
       }
     }
     il++;
   }  
   fclose(tmp);
   *n=is;
}

int main( int argn, char *arg[]) {
  int i,n,n0,nn,l;
  double sx,sx2,err,sx1,sd;

  readin(argn,arg,&n);
  
  printf("Read %d lines\n",n);
  /*  printf("Leave out how many points at the beginning (put e.g. 0): "); */
  /*  scanf("%d",&n0); */
  n0=0;
  
  for(i=n0;i<n;i++) 
    x[i-n0]=x[i];
  n -=n0;

  nn = n;
  l=1;
  do {
    sx=0.0;
    sx2=0.0;
    for(i=0;i<nn;i++) {
      sx += x[i];
      sx2 += x[i]*x[i];
    }
    sx  /= (double)nn;
    if (l==1) sx1=sx;
    sx2 /= (double)nn;
    err = (sx2-sx*sx)/(double) (nn-1) ;
    sd  = sqrt(sx2-sx*sx);
    err *= (double)(l*nn)/(double) n;
    err = sqrt(err);
    printf("block_length= %3d  block_number= %4d <x>= %f std dev.= %f err= %f\n",
	   l,nn,sx,sd,err);
    nn /= 2;
    l  *= 2;
    for(i=0;i<nn;i++) {
      x[i] = (x[2*i]+x[2*i+1])*0.5;
    }
  }  while ( nn>=9);

  printf("Final result <x>= %lf +- %lf\n\n",sx1,err);

  return 0;
}
