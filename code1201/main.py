import os
import re
import copy

path1 = os.path.abspath('.')
path2 = os.path.abspath('..')

file_path = path1 + '/code1201/input.txt'

numbers = [[' _ ', '| |', '|_|'],
            ['   ', '  |', '  |'],
            [' _ ', ' _|', '|_ '],
            [' _ ', ' _|', ' _|'],
            ['   ', '|_|', '  |'],
            [' _ ', '|_ ', ' _|'],
            [' _ ', '|_ ', '|_|'],
            [' _ ', '  |', '  |'],
            [' _ ', '|_|', '|_|'],
            [' _ ', '|_|', ' _|']]


def read_lines(file_path):
    file = open(file_path)
    return file.readlines()


def analysis_data(lines):
    analysis_list = [[0] * 3 for i in range(9)]
    result = []
    status=""
    account=[]
    new_account=[]
    for index, value in enumerate(lines):
        if(index % 4 != 3):
            split = re.findall(r'.{3}', value)
            for i in range(len(split)):
                    analysis_list[i][index % 4] = split[i]
        else:
            # read blank line, check account
            status,account,new_account=check_account(analysis_list)
            print(account,status,new_account)
            # account = []
            # for value in analysis_list:
            #     if(value in numbers):
            #         account.append(numbers.index(value))
            #     else:
            #         account.append(-1)
            # result.append(account)
    # return status,account,new_account


def check_account(analysis_list):
    account = []
    error_indexs=[]
    replace = []
    for index,value in enumerate(analysis_list):
        if(value in numbers):
            account.append(numbers.index(value))
        else:
            error_indexs.append(index)
            account.append(-1)
    
    if(len(error_indexs)==1):
        # char err account
        replace = get_replace_num(analysis_list[error_indexs[0]])
        new_accounts=construct_account(account,replace,error_indexs[0])
        if(len(new_accounts)>0):
            if(len(new_accounts)==1):
                return "RIGHT",new_accounts[0],[]
            return "ABM",account,new_accounts
        else:
            return "ILL",account,[]    
        # print("----replace----")
        # print(replace)
    else:
        if(calculate(account)):
            # right
            
            return 'RIGHT',account,[]
        else:
            new_accounts=[]
            for idx,num in enumerate(account):
                replace = get_replace_num(numbers[num])
                new_accounts+=construct_account(account,replace,idx)
            if(len(new_accounts)==0):
                return "ERR",account,[]
            if(len(new_accounts)==1):
                return "RIGHT",new_accounts[0],[]
            return "ABM",account,new_accounts         


def construct_account(num_list,replace_nums,index):
    right_account=[]
    for num in replace_nums:
        account = copy.copy(num_list)
        account[index]=num
        if(calculate(account)):
            right_account.append(account)
    return right_account

def calculate(num_list):
    sum = 0
    for index,value in enumerate(num_list):
        sum += (8-index+1)*value
    return sum%11==0

def get_replace_num(decompose):
    replace=[]
    for idx,line in enumerate(decompose):
        # ' _ '
        line_to_list = list(line) # [' ',''_',' ']
        for index,value in enumerate(line_to_list):
            replace_char = [' ','_','|']
            replace_char.remove(value)
            for each_char in replace_char:
                tmp_line = copy.copy(line_to_list)
                tmp_num = copy.copy(decompose)
                tmp_line[index] = each_char
                tmp_num[idx] = ''.join(tmp_line)
                if tmp_num in numbers: replace.append(numbers.index(tmp_num))
    return replace


if __name__ == "__main__": 
    lines = read_lines(file_path)
    analysis_data(lines)
    # for each in result:
    #     print(each)


