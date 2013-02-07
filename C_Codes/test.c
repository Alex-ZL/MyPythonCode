#include <stdio.h>

void foo(int t[]){
	printf("size inside is %d\n", sizeof(t));
}

int main(){
	int arr[8] = {1, 2, 3, 4, 5, 6, 7};
	printf ("size outside is %d\n", sizeof(arr));
	foo(arr);
}

