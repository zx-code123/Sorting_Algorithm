#include <iostream>
#include <algorithm>
using namespace std;

void shell_sort(int arr[],int len){
    int step = len / 2;      //初始增量
    while(step > 0){
        //无序部分
        for(int i = step; i < len; i++){
            int temp = arr[i];
            int j;
            //子序列中的插入排序,这是有序部分
            for(j = i-step; j>=0 && temp < arr[j]; j=j-step)
                //在找到当前元素合适位置前，元素后移
                arr[j+step]=arr[j];
            arr[j+step]=temp;
        }
        step /= 2;
    }
}
//希尔排序
void test6()
{
    int arr[] = {9,6,7,22,20,33,16,20};
    int length = 8;
    cout << "Before sorted:" << endl;
    for(int i = 0;i < length;i++)
        cout << arr[i] << "  ";
    cout << endl;
    cout << "After sorted:" << endl;
    algorithm_me al;
    al.shell_sort(arr,8);
    for(int i = 0;i < length;i++)
        cout << arr[i] << "  ";
    cout << endl;
}
int main(int argc, char *argv[])
{
    test6();
    cout << "Hello World!" << endl;
    return 0;
}