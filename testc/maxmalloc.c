#include <stdlib.h>
#include <stdio.h>

#define NN 274500

int main(){

		int n = NN;
		int *ptr;
		ptr=malloc(n*n*sizeof(int));
		fprintf(stderr,"\nDone with malloc n=%d (%d) size %lu \t %p \n",n,NN,sizeof(ptr),ptr);
		long sub=10;
		fprintf(stderr,"ptr[%l] = %d",sub,ptr[sub]);
		/* int array[NN][NN]; */
		/* memset (ptr,0,n*n*sizeof(int)); */
		long i,j,k;
		for (i=0;i<NN;++i)
				for (j = 0;j<NN;++j){
						k=i*NN+j;
						ptr[(i)*NN+j]=-1;
				}
		return 0;
}
