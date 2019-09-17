import os
import tempfile
import sys 

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
        l = len(arr) - 1
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
            file_list.append(headNode(letter, tempFileList)) 

        self.initializeMinheap(file_list)

        while True:
            min = file_list[0]
            if min.letter == sys.maxsize:
                break

            sorted_word.append(min.letter.decode())
            # extract next letter from the file 
            fileHandler = min.fileHandler 
            new_letter = fileHandler.readline().strip()
            if not new_letter:
                new_letter = sys.maxsize
            else:
                new_letter = new_letter 
            file_list[0] = headNode(new_letter, fileHandler)
            self.minheap(file_list, 0, len(file_list))
        f = open(outputFile, 'w')
        f.writelines(", ".join(sorted_word))
        
        
    def splitFiles(self, fileName, partitionSize):
        fileHandler = open(fileName, "rb")
        tempArray = []
        size = 0
        while True:
            letter = fileHandler.readline()
            if not letter:
                break
            tempArray.append(letter)
            size += 1
            if size % partitionSize == 0:
                # sort scoped words
                tempArray = sorted(tempArray, key=lambda word: word.strip())
                # create a new file under the temp directory
                tempFile = tempfile.NamedTemporaryFile(dir=self.cwd + "/temp", delete=False)
                # store sorted words to the created file
                tempFile.writelines(tempArray)
                tempFile.seek(0)
                # store all the file handlers to the global list
                self.tempFileHandlerList.append(tempFile)
                tempArray = [] 


if __name__ == '__main__':
    largeFileName = 'largefile'
    outputFileName = 'output.txt'
    smallFileSize = 10
    obj = externalSort()
    obj.splitFiles(largeFileName, smallFileSize)
    obj.mergeFiles(outputFileName)
        