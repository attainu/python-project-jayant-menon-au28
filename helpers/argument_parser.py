import argparse

class ArgumentParser:
    """ 
    docstring
    """
    def take_input():
        parser = argparse.ArgumentParser(description="Find a path in a rat maze.\
            Takes .txt maze input, outputs .txt solved path")

        parser.add_argument("-i", "-inputfile", metavar="", required=True, help="input\
            filename. Please ensure file is in .input folder.")
        parser.add_argument("-o", "--outputfile", metavar="", default="output.txt", help="output\
            filename. Will be generated to .output folder.", action="store_true")

        args = parser.parse_args()
        return args