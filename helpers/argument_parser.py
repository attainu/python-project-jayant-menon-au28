import argparse

class ArgumentParser:
    """ 
    docstring
    """
    def take_input():
        parser = argparse.ArgumentParser(description="Find a path in a rat maze.\
            Takes .txt maze input, outputs .txt solved path")

        required = parser.add_argument_group('required arguments')
        required.add_argument("-i", "--inputfile", required=True, help="input\
            filename. Please ensure file is in .input folder.")
        
        parser.add_argument("-o", "--outputfile", default="output.txt", help="output\
            filename. Will be generated to .output folder.", action="store_true")

        args = parser.parse_args()

        # args.inputfile = "input/" + args.inputfile
        # args.outputfile = "output/" + args.inputfile
        return args
    
    def modify_dir(infile, outfile):
        """ docstring """
        infile = "input/" + infile
        outfile = "output/" + outfile