import argparse

class ArgumentParser:
    """ 
    A class to parse command line arguments 
    """
    def modify_dir(infile, outfile):
        """appends working directories to user input"""
        infile_path = "input/" + infile
        outfile_path = "output/" + outfile
        return infile_path, outfile_path
    
    def take_input():
        """takes and returns input, output and algo arguments from the user"""
        parser = argparse.ArgumentParser(description="Find a path in a rat maze.\
            Takes .txt maze input, outputs .txt solved path")

        required = parser.add_argument_group('required arguments')
        required.add_argument("-i", "--inputfile", required=True, help="input\
            filename. Please ensure file is in .input folder.")
        parser.add_argument("-o", "--outputfile", default="output.txt", help="output\
            filename. Will be generated to .output folder.")
        parser.add_argument("-a", "--algorithm", default="BFS", help="choose\
            an algorithm (BFS or DFS)")
        
        args = parser.parse_args()
        infile_path, outfile_path = ArgumentParser.modify_dir(args.inputfile, args.outputfile)        
        
        return infile_path, outfile_path, args.algorithm