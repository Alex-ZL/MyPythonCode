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

SqList GenSqList(int arg[], int length){
	SqList w;
	w.length = length;
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
int Partition(SqList L, int low, int high){
	int pivotkey = L.r[low].key;
	while(low<high){
		while(low<high && L.r[high].key>=pivotkey) high--;
		L.r[low].key = L.r[high].key;
		while(low<high && L.r[low].key<=pivotkey) low++;
		L.r[high].key = L.r[low].key;
	}
	L.r[low].key = pivotkey;
	return low;
}

void QSort(SqList L, int low, int high){
	if (low<high){
		int pivotloc = Partition(L, low, high);
		QSort(L, low, pivotloc-1);
		QSort(L, pivotloc+1, high);
	}
}

void QuickSort(SqList L){
	QSort(L, 0, L.length-1);
}

int main(int argc, char *argv[]){
	int t[6] = {4, 3, 2, 34, 12, 2};
	SqList L = GenSqList(t, 6);
	QuickSort(L);
	RepresentSqList(L);
}
