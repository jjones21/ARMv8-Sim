# ARMv8-Sim
A simulator for LEGv8 in Python 2.7
Made by Julian Jones with assistance from Md Billah
provide binary input in a txt file and this script will read it as ARMv8 LEG instructions and run them.

This project can be run from the command line with the following parameters:

    team5_project3.py -i <inputFileName> -o <outputFileName>

For example, on my computer i run the project like so:

    team5_project3.py -i "C:\Users\Julian\PycharmProjects\Project1\test_bin.txt" -o "team5_out"

Example input and output has been provided in the "sample" folder.
The output txt files are formatted with the intention of being viewed within Pycharm, they will look misspaced anywhere else.
The outputfile with the extention "\_dis.txt" is the result of the decoder reading the binary input file.
Binary lines are shown on the left and the LEGv8 instructions they result in are displayed to the right.
The outputfile with the extention "\_sim.txt" displays the values of the regesters and Memory after each instruction.
