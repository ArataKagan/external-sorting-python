# Very Large File Sorting 

## How to run the file
1) Unzip/clone the folder 
2) Change your directory to the external-sorting folder
3) Execute 'python external-sorting-main.py' 
4) Open the output.txt folder  

## File contents 

external-sorting-main.py : The main file for all the code<br/>
large-input.txt : The original large file<br/>
small-input.txt : The small text file<br/>
output.txt : The output file<br/>
random-words-generator.py : Includes code for generating random words 
 
## Choice of Technology 

Python 3.6.1

## Choice of Merge Methods 

### Merge Sort
Merge sort is used to sort each line alphabetically. I chose merge sort among many other sorting algorithms due to its faster runtime and its efficiency and ease of implementation. 

### Min Heap Sort 
Min heap sort is used to sort each line from sub files. 

## How I solved the problem 

### Step 1: Break down the large file into temporary files 
As a first step of external sorting, the large file is divided into small chunks of files. I have used Python's tempfile module to generate sub files from the large text file. 

### Step 2: Sort each line 
Among each sub file, each line is sorted alphabetically. The order of each line is sorted from top to bottom. 

### Step 3: Merge lines from each sub file
Each line of temporary file is merged to the output file and alphabetically sorted with other temporary files. Heap node is created for every line and sorted with min-heap. 


