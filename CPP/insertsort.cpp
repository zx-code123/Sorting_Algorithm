#include <iostream>
#include <algorithm>
using namespace std;

void algorithm_me::insert(int arr[],int k)
{
    int key = arr[k];
    int i = k;
    while(key < arr[i-1])
    {
        arr[i] = arr[i-1];
        i--;
        if(i == 0)
        {
            break;
        }
    }
    arr[i] = key;
}
void algorithm_me::insertSort(int arr[],int n)
{
    int i;
    for(i = 1;i<n;i++)
    {
        insert(arr,i);
    }
}
//插入排序
void test3()
{
    int arr[] = {9,6,2,3,5,1,3};
    algorithm_me al;
    al.insertSort(arr,7);
    for(int i = 0;i<7;i++)
    {
        cout <<"插入排序"<< arr[i] << endl;
    }
}
int main(int argc, char *argv[])
{
    test3();
    cout << "Hello World!" << endl;
    return 0;
}