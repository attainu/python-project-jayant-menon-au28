import argparse

class ArgumentParser:
    """ 
    docstring
    """
    def modify_dir(infile, outfile):
        """docstring"""
        infile = "input/" + infile
        outfile = "output/" + outfile
        return infile, outfile
    
    def take_input():
        """docstring"""
        parser = argparse.ArgumentParser(description="Find a path in a rat maze.\
            Takes .txt maze input, outputs .txt solved path")

        required = parser.add_argument_group('required arguments')
        required.add_argument("-i", "--inputfile", required=True, help="input\
            filename. Please ensure file is in .input folder.")
        parser.add_argument("-o", "--outputfile", default="output.txt", help="output\
            filename. Will be generated to .output folder.")
        # parser.add_argument("-a", "--algorithm", default="BFS", help="choose\
            # an algorithm (BFS or DFS)")
        
        args = parser.parse_args()
        infile, outfile = ArgumentParser.modify_dir(args.inputfile, args.outputfile)        
        
        return infile, outfile
