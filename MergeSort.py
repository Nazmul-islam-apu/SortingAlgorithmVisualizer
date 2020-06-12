import time
def merge_sort(data,drawData,timeTick):
    merge_sort_algo(data,0,len(data)-1,drawData,timeTick)

def merge_sort_algo(data,left,right,drawData,timeTick):

    if left<right:
        mid = (left+right)//2
        merge_sort_algo(data,left,mid,drawData,timeTick)
        merge_sort_algo(data,mid+1,right,drawData,timeTick)
        merge(data,left,mid,right,drawData,timeTick)


def merge(data,left,mid,right,drawData,timeTick):
    drawData(data, gerColorArray(len(data),left,mid,right))
    time.sleep(timeTick)
    leftPart = data[left:mid+1]
    rightPart = data[mid+1:right+1]
    leftIdx=rightIndx =0
    for dataIdx in range(left,right+1):
        if leftIdx<len(leftPart) and rightIndx<len(rightPart):
            if leftPart[leftIdx]<=rightPart[rightIndx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx+=1
            else:
                data[dataIdx] = rightPart[rightIndx]
                rightIndx+=1
        elif leftIdx<len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx+=1
        else:
            data[dataIdx] = rightPart[rightIndx]
            rightIndx+=1
    drawData(data, ["skyblue" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)


def gerColorArray(length,left,mid,right):
    colorArray = []
    for i in range(length):
        if i >=left and i<=right:
            if i>=left and i <=mid:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")
    return colorArray