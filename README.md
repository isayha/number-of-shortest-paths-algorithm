# number-of-shortest-paths-algorithm
A Python implementation of a modified Dijkstra's algorithm. This algorithm determines both the length *and* the number of the shortest (distinct) paths between the specified source and destination nodes for a specified graph (given in the form of an adjacency matrix). The algorithm achieves this by allowing for (and keeping track of the number of) repeated visits from the source node to the destination node where said visits originate from distinct paths and said distinct paths are all of the same (shortest possible) length.

## Instructions
### How to run
- To run the program, simply run `assignment3_part2_cpsc482_isayharaposo.py`, either using the command `python` on the command line (while in the same directory as the source files), or the IDE of your choice
    - For reference, this program was written in Python 3.8.6
    - The program will ask for the name of a desired input data file during execution unless a name is specified as an argument on the command line when running the program:
        - e.g., `python assignment3_part2_cpsc482_isayharaposo.py example1_data.txt` will run the program with the first given set of example data (see **Pseudocode and Examples**) specified
        - Note that the file extension must be specified when specifying input data file names
        - Also note that the input data files must be in the same directory as the program itself
### Pseudocode and Examples
- A document containing equivalent pseudocode can be found under the file name `assignment3_part1_cpsc482_isayharaposo.txt`
- Two sets of example data (inputs) are found under the file names:
    - `example1_data.txt`
    - `example2_data.txt`
- A document containing images of said inputs, diagrammatic depictions of the adjacency matrices found within each input, and images of the outputs corresponding to each input, can be found under the file name `assignment3_part3_cpsc482_isayharaposo.pdf`
### How to format input data
- For data input, this program accepts a single, particularly formatted text file
    - Said file must be formatted correctly, otherwise the program will either catch data formatting issue(s) and exit,
    output incorrect results, or simply crash
    - All data is numeric; nodes are referred to via distinct numbers incremented from (and including) zero
- The correct formatting of input data files is as follows:
    - The first line of an input data file should include both the desired source node and the desired destination node (in that order) separated by a comma followed by a space (`, `)
    - Every line following the first line of an input data file should specify a single row of the desired adjacency matrix (the second line of an input data file should specify which node(s) node 0 is adjacent to, the third line of an input data file should specify which node(s) node 1 is adjacent to, et cetera). Within each row, a value of 0 indicates non-adjacency, and a value of 1 indicates adjacency. The first value within each row corresponds to adjacency with node 0, the second value within each row corresponds to adjacency with node 1, et cetera. Each of said values must be separated by a space (` `)
    - The adjacency matrix MUST be of size (n x n) where n = the number of nodes within the graph the adjacency matrix represents (as per the definition of an adjacency matrix)
