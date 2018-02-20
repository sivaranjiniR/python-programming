#include <stdio.h>
#include<ctype.h>

int main(void) {
	// your code goes here
int n;
scanf("%d",&n);
if(n>=1&&n<=100000)
printf("positive");
else if(n==0)
printf("zero");
else if(n<0) 
printf("negative");
else if(n>=100000)
printf("neg test case integer");
return 0;
}
