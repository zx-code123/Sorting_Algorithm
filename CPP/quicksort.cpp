#include <iostream>

using namespace std;

void quicksort(int arr[],int L,int R)
{
	int i = L;
	int j = R;
	int pivot = arr[(L+R)/2];
	while(i<=j)
	{
		while(arr[i]<pivot)
		{
			i++;
		}
		while(arr[j]>pivot)
		{
			j--;
		}
		if(i<=j)
		{
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
			i++;
			j--;
		}
	}
	if(L<j)
	{
		quicksort(arr,L,j);
	}
	if(i<R)
	{
		quicksort(arr,i,R);
	}
}
int main()
{
	int arr[] = {3,4,2,9,7,1,5,8,0,6};
	quicksort(arr,0,9);
	for(int i = 0;i<10;i++)
	{
		printf("%d\n",arr[i]);
	}
}





