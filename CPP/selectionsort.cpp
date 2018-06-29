#include <iostream>
#include <algorithm>
using namespace std;

int findMaxPos(int arr[],int n)
{
    int i;
    int pos = 0;
    int max = arr[0];
    for(i = 1;i<n;i++)
    {
        if(arr[i]>max)
        {
            max = arr[i];
            pos = i;
        }
    }
    return pos;

}
void selectionSort(int arr[],int n)
{
    int temp;
    for(int i = n;i>1;i--)
    {
        int pos = findMaxPos(arr,i);
        temp = arr[pos];
        arr[pos] = arr[i-1];
        arr[i-1] = temp;
    }
}

//选择排序
void test2()
{
    int arr[] = {9,6,2,3,5,1,3};
    algorithm_me al;
    al.selectionSort(arr,7);
    for(int i = 0;i<7;i++)
    {
        cout <<"选择排序"<< arr[i] << endl;
    }
}
int main(int argc, char *argv[])
{
    test2();
    cout << "Hello World!" << endl;
    return 0;
}