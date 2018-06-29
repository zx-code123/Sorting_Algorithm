#include <iostream>
#include <algorithm>
using namespace std;

void merge(int *data,int start,int end,int *result)
{
    int left_length = (end - start + 1) / 2 + 1;//左部分区间的数据元素的个数
    int left_index = start;
    int right_index = start + left_length;
    int result_index = start;
    while(left_index < start + left_length && right_index < end+1)
    {
        //对分别已经排好序的左区间和右区间进行合并
        if(data[left_index] <= data[right_index])
            result[result_index++] = data[left_index++];
        else
            result[result_index++] = data[right_index++];
    }
    while(left_index < start + left_length)
        result[result_index++] = data[left_index++];
    while(right_index < end+1)
        result[result_index++] = data[right_index++];
}
void merge_sort(int *data, int start, int end, int *result)
{
    if(1 == end - start)//如果区间中只有两个元素，则对这两个元素进行排序
    {
        if(data[start] > data[end])
        {
            int temp  = data[start];
            data[start] = data[end];
            data[end] = temp;
        }
        return;
    }
    else if(0 == end - start)//如果只有一个元素，则不用排序
        return;
    else
    {
        //继续划分子区间，分别对左右子区间进行排序
        merge_sort(data,start,(end-start+1)/2+start,result);
        merge_sort(data,(end-start+1)/2+start+1,end,result);
        //开始归并已经排好序的start到end之间的数据
        merge(data,start,end,result);
        //把排序后的区间数据复制到原始数据中去
        for(int i = start;i <= end;++i)
            data[i] = result[i];
    }
}
//归并排序
void test4()
{
    int data[] = {9,6,7,22,20,33,16,20};
    const int length = 8;
    int result[length];
    cout << "Before sorted:" << endl;
    for(int i = 0;i < length;++i)
        cout << data[i] << "  ";
    cout << endl;
    cout << "After sorted:" << endl;
    algorithm_me al;
    al.merge_sort(data,0,length-1,result);
    for(int i = 0;i < length;++i)
        cout << data[i] << "  ";
    cout << endl;
}
int main(int argc, char *argv[])
{
    test4();
    cout << "Hello World!" << endl;
    return 0;
}