#include <stdio.h>
#define MAXSIZE 20

typedef int KeyType;

typedef struct{
	KeyType key;
}RedType;

typedef struct{
	RedType r[MAXSIZE+1];
	int length;
}SqList;

void repr(SqList L){
	printf ("\n %d \n", L.r[0].key);
}

SqList GenSqList(int arg[], int length){
	SqList w;
	w.length = length;
	printf("length in Gen is %d\n", length);
	int i;
	for (i=0; i<length; i++){
		KeyType value = arg[i];
		RedType red;
		red.key = value;
		w.r[i] = red;
	}
	return w;
}

void RepresentSqList(SqList L){
	int i;
	printf("SqList length is: %d\n", L.length);
	for(i=0; i<L.length; i++){
		printf("%d, ", L.r[i].key);
	}
	printf("\n");
}

int main()
{
	int a, *x;
	a = 1;
	x = &a;
	printf ("%d\n", *x);
	printf ("hello, C programme eventally.\n");

	KeyType u = 22;
	RedType v;
	v.key = u;
	SqList w;
	w.r[0] = v;
	w.r[1] = v;
	w.length = 10;

	printf ("a element in SqList: %d\n", w.r[1].key);
	printf ("length of SqList is : %d\n", w.length);
	int t[3] = {1, 2, 3};
	printf("before Gen sizeof arg is %d\n", sizeof(t));
	printf("before Gen sizeof arg[0] is %d\n", sizeof(t[0]));
	printf ("before Gen sizeof result is %d\n", sizeof(t)/sizeof(t[0]));
	SqList L = GenSqList(t, 3);
	RepresentSqList(L);
}
