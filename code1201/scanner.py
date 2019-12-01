import re

class scanner:
    def read_lines(self,file_path):
        file = open(file_path)
        return file.readlines()
    
    
    # return:
    # result = [[' _ ', '| |', '|_|'],
    #         ['   ', '  |', '  |'],
    #         [' _ ', ' _|', '|_ '],
    #         [' _ ', ' _|', ' _|'],
    #         ['   ', '|_|', '  |'],
    #         [' _ ', '|_ ', ' _|'],
    #         [' _ ', '|_ ', '|_|'],
    #         [' _ ', '  |', '  |'],
    #         [' _ ', '|_|', '|_|'],
    #         [' _ ', '|_|', ' _|']]
    def scan_lines(self,lines):
        analysis_list = [[0] * 3 for i in range(9)]
        result = []
        for index, value in enumerate(lines):
            if(index % 4 != 3):
                split = re.findall(r'.{3}', value)
                for i in range(len(split)):
                        analysis_list[i][index % 4] = split[i]
            else:
                result.append = analysis_list
        return result