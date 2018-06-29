#include <iostream>
#include <algorithm>
using namespace std;

void bubbleSort(int arr[], int n)
{
    int i;
    int temp;
    for(i = 0;i<n-1;i++)
    {
        if(arr[i]>arr[i+1])
        {
            temp = arr[i];
            arr[i] = arr[i+1];
            arr[i+1] = temp;
        }
    }
}
void bubbleResult(int arr[],int n)
{
    for(int i = n;i>=1;i--)
    {
        bubbleSort(arr,n);
    }
}


//冒泡排序
void test1()
{
    int arr[] = {9,6,2,3,5,1,3};
    algorithm_me al;
    al.bubbleResult(arr,7);
    for(int i = 0;i<7;i++)
    {
        cout <<"冒泡排序"<< arr[i] << endl;
    }
}
int main(int argc, char *argv[])
{
    test1();
    cout << "Hello World!" << endl;
    return 0;
}