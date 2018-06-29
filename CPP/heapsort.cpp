#include <iostream>
#include <algorithm>
using namespace std;

void heap(int arr[],int len,int index)
{
    int left = 2*index +1;
    int right = 2*index +2;
    int maxId = index;
    if(left<len && arr[left]>arr[maxId])
    {
        maxId = left;
    }
    if(right<len && arr[right]>arr[maxId])
    {
        maxId = right;
    }
    if(maxId != index)
    {
        int temp = arr[maxId];
        arr[maxId] = arr[index];
        arr[index] = temp;
//        swap(arr[maxId], arr[index]);
        heap(arr,len,maxId);
    }
}
void heap_sort(int arr[],int len)
{
    for(int i=len/2 - 1; i >= 0; i--)  // 对每一个非叶结点进行堆调整(从最后一个非叶结点开始)
        {
            heap(arr, len, i);
        }
    for(int i = len - 1; i >= 1; i--)
    {
//        swap(arr[0], arr[i]);           // 将当前最大的放置到数组末尾
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        heap(arr, i, 0);              // 将未完成排序的部分继续进行堆排序
    }
}

//堆排序
void test5()
{
    int arr[] = {9,6,7,22,20,33,16,20};
    int length = 8;
    cout << "Before sorted:" << endl;
    for(int i = 0;i < length;i++)
        cout << arr[i] << "  ";
    cout << endl;
    cout << "After sorted:" << endl;
    algorithm_me al;
    al.heap_sort(arr,8);
    for(int i = 0;i < length;i++)
        cout << arr[i] << "  ";
    cout << endl;
}
int main(int argc, char *argv[])
{
    test5();
    cout << "Hello World!" << endl;
    return 0;
}