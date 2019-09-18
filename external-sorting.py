import os
import tempfile
import heapq
import sys


class heapnode:
    """ Heapnode of a Heap (MinHeap Here)
       @params
               item        The actual value to be stored in heap
               fileHandler The filehandler of the file that stores the number"""

    def __init__(
            self,
            item,
            fileHandler,
    ):
        self.item = item
        self.fileHandler = fileHandler


class externamMergeSort:
    """ @params
           sortedTempFileHandlerList - List of all filehandlers to all temp files formed by splitting large files
    """

    def __init__(self):
        self.sortedTempFileHandlerList = []
        self.getCurrentDir()

    def getCurrentDir(self):
        self.cwd = os.getcwd()


    """ min heapify function """

    def heapify(
            self,
            arr,
            i,
            n,
    ):
        print("i", i)
        print("n", n)
        left = 2 * i + 1
        print("left value: ", left)
        right = 2 * i + 2
        print("right value: ", right)
        
        if left < n and str(arr[left].item).encode('utf-8') < str(arr[i].item).encode('utf-8'):
            print("str(arr[left].item).encode('utf-8'): ", str(arr[left].item).encode('utf-8'))
            print("str(arr[i].item).encode('utf-8'): ", str(arr[i].item).encode('utf-8'))
            smallest = left
            print("parent node bigger than left node")
        else:
            smallest = i
            print("tree complete")

        if right < n and str(arr[right].item).encode('utf-8') < str(arr[smallest].item).encode('utf-8'):
            print("str(arr[right].item).encode('utf-8'): ", str(arr[right].item).encode('utf-8'))
            print("str(arr[smallest].item).encode('utf-8'): ", str(arr[smallest].item).encode('utf-8'))
            smallest = right
            print("parent node bigger than right node")

        if i != smallest:
            print("swapping parent node and smallest node")
            (arr[i], arr[smallest]) = (arr[smallest], arr[i])
            self.heapify(arr, smallest, n)
    
    """ construct heap """

    def construct_heap(self, arr):
        l = len(arr) - 1
        mid = int(l / 2)
        while mid >= 0:
            self.heapify(arr, mid, l)
            mid -= 1

    """ low level implementation to merge k sorted small file to a larger file . Move first element of all files to a min heap . The Heap has now the smallest element .
         Mmoves  that element from heap to a file . Get the filehandler of that element .Read the next element using the  same filehandler . If next file element is empty, mark it as INT_MAX.
         Moves it to heap . Again Heapify . Continue this until all elements of heap is INT_MAX or all the smaller files have read fully """

    def mergeSortedtempFiles_low_level(self, outputFile):
        print("#2 inside of mergeSortedtempFiles")
        list = []
        sorted_output = []
        print("before going into heapnode")

        for tempFileHandler in self.sortedTempFileHandlerList:
            item = tempFileHandler.readline().strip()
            print("item retrieved: ", item)
            list.append(heapnode(item, tempFileHandler))
        
        print("after node retrieved heapnode")
        self.construct_heap(list)

        while True:
            min = list[0]
            if min.item == sys.maxsize:
                break 
            
            sorted_output.append(min.item.decode())
            print("sorted_output: ", sorted_output)
            fileHandler = min.fileHandler
            item = fileHandler.readline().strip()
            if not item:
                item = sys.maxsize
            else:
                item = item
            list[0] = heapnode(item, fileHandler)
            self.heapify(list, 0, len(list))
        f = open(outputFile, 'w')
        f.write(", ".join(sorted_output))

    """ function to Split a large files into smaller chunks , sort them and store it to temp files on disk"""

    def splitFiles(self, largeFileName, smallFileSize):
        print("#1 inside of splitFiles method")
        largeFileHandler = open(largeFileName, "rb")
        tempBuffer = []
        size = 0
        while True:
            number = largeFileHandler.readline()
            if not number:
                break
            tempBuffer.append(number)
            size += 1
            if size % smallFileSize == 0:
                tempBuffer = sorted(tempBuffer, key=lambda no: \
                    no.strip())
                tempFile = tempfile.NamedTemporaryFile(dir=self.cwd + '/temp', delete=False)
                print("tempBuffer: ", tempBuffer)
                print("type of tempBuffer: ", type(tempBuffer))
                tempFile.writelines(tempBuffer)
                tempFile.seek(0)
                self.sortedTempFileHandlerList.append(tempFile)
                tempBuffer = []


if __name__ == '__main__':
    largeFileName = 'testLargeFile'
    outputFileName = './output.txt'
    smallFileSize = 10
    obj = externamMergeSort()
    obj.splitFiles(largeFileName, smallFileSize)
    """ Useslower level functions without any python Libraries . Better to understand it """
    # print(obj.mergeSortedtempFiles_low_level(outputFileName))
  
