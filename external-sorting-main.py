import os
import tempfile
import sys 
import collections

class headNode:
    def __init__(self, letter, fileHandler):
        # letter to be stored in heap
        self.letter = letter
        # file handler for each letter
        self.fileHandler = fileHandler 

class externalSort: 
    def __init__(self): 
        self.tempFileHandlerList = []
        self.getCurrentDir()
    
    def getCurrentDir(self):
        self.cwd = os.getcwd() 

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            lefthalf = arr[:mid]
            righthalf = arr[mid:]
    
            #recursion
            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)

            i=0
            j=0
            k=0

            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    arr[k] = lefthalf[i]
                    i=i+1
                else:
                    arr[k] = righthalf[j] 
                    j=j+1
                k=k+1
            
            while i < len(lefthalf):
                arr[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                arr[k]=righthalf[j]
                j=j+1
                k=k+1

        return arr
        
    def minheap(self, arr, parentNode, arrayLength):
        left_node = 2 * parentNode + 1
        right_node = 2 * parentNode + 2
        
        if left_node < arrayLength and str(arr[left_node].letter).encode('utf-8') < str(arr[parentNode].letter).encode('utf-8'):
            # assign left node to smallest variable 
            smallest = left_node 
        else:
            #base case to stop the recursion
            smallest = parentNode 
          
        if right_node < arrayLength and str(arr[right_node].letter).encode('utf-8') < str(arr[smallest].letter).encode('utf-8'):
            smallest = right_node 
        
        if parentNode != smallest:
            # swap smallest variable and parent node
            (arr[parentNode], arr[smallest]) = (arr[smallest], arr[parentNode])
            # apply smallest variable as a parent node to minheap recursively 
            self.minheap(arr, smallest, arrayLength)

    def initializeMinheap(self, arr):
        global mid 
        if len(arr) % 2 == 0: 
            l = len(arr) - 1
        else:
            l = len(arr) 
        mid = int(l / 2)
        while mid >= 0:
            self.minheap(arr, mid, l)
            mid -= 1
          
    def mergeFiles(self, outputFile):
        file_list = []
        sorted_word = [] 

        # get the first letter from each file, instantiate headNode object and append to list
        for tempFileList in self.tempFileHandlerList:
            letter = tempFileList.readline().strip()
            letter = letter.decode("utf-8")
            file_list.append(headNode(letter, tempFileList)) 

        self.initializeMinheap(file_list)

        while True:
            min = file_list[0]
            if min.letter == sys.maxsize:
                break

            sorted_word.append(min.letter)
            # extract next letter from the file 
            fileHandler = min.fileHandler 
            new_letter = fileHandler.readline().strip()
            new_letter = new_letter.decode("utf-8")
            
            if not new_letter:
                new_letter = sys.maxsize
            else:
                new_letter = new_letter 
            file_list[0] = headNode(new_letter, fileHandler)
            self.minheap(file_list, 0, len(file_list))
        f = open(outputFile, 'w')
        for i in sorted_word:
            f.write(i+'\n')
        
        
    def splitFiles(self, fileName, partitionSize):
        fileHandler = open(fileName, "r")
        tempLine = []
        tempArray = []
        
        size = 0
        while True:
            # read each line and store into line
            line = fileHandler.readline()
          
            if not line:
                break
            
            line = line.rstrip().split(" ")
            tempArray.append(line)
    
            size += 1
            if size % partitionSize == 0:
                

                # sort each line
                for i in tempArray:
                    i = self.mergeSort(i) 

                objCollection = {}
                orderedList = []
                stringList = ""
                collection = []
 
                for line in tempArray:
                    lineObj = {}
                    lineObj = {line[0] : line} 
                    objCollection.update(lineObj) 

                objCollection = collections.OrderedDict(sorted(objCollection.items()))
               
                for k, v in objCollection.items():
                    orderedList.append(v)
                
                for line in range(len(orderedList)):
                    orderedList[line][4] = orderedList[line][4]+'\n' 

                for i in range(len(orderedList)):
                    print(orderedList[i])
                    for item in orderedList[i]:
                        print(item)
                        stringList += ' '+item 

                tempFile = tempfile.NamedTemporaryFile(mode="w+b", dir=self.cwd + "/temp", delete=False)

                tempFile.write(bytes(stringList, "utf-8"))
                tempFile.seek(0)
                # store all the file handlers to the global list
                self.tempFileHandlerList.append(tempFile)
                tempArray = [] 

    
if __name__ == '__main__':
    largeFileName = 'input.txt'
    outputFileName = 'output.txt'
    smallFileSize = 16
    obj = externalSort()
    obj.splitFiles(largeFileName, smallFileSize)
    obj.mergeFiles(outputFileName)
    
        