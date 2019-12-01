import copy


class checker:
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
    
#    [[' _ ', ' _|', '|_ '],
#     [' _ ', ' _|', ' _|'],
#     ['   ', '|_|', '  |'],
#     [' _ ', '|_ ', ' _|'],
#     [' _ ', '|_ ', '|_|']]
    def check_account(self,analysis_list):
        account = []
        error_indexs=[]
        replace = []
        for index,value in enumerate(analysis_list):  # [' _ ', ' _|', '|_ ']
            if(value in self.numbers):  # if current value is 0~9
                account.append(self.numbers.index(value)) # add this number
            else:
                error_indexs.append(index) # record this error index
                account.append(-1)
        
        if(len(error_indexs)==1):
            # char err account
            replace = self.get_replace_num(analysis_list[error_indexs[0]])
            new_accounts=self.construct_account(account,replace,error_indexs[0])
            if(len(new_accounts)>0):
                if(len(new_accounts)==1):
                    return "RIGHT",new_accounts[0],[]
                return "ABM",account,new_accounts
            else:
                return "ILL",account,[]    
            # print("----replace----")
            # print(replace)
        else:
            if(self.calculate(account)):
                # right
                
                return 'RIGHT',account,[]
            else:
                new_accounts=[]
                for idx,num in enumerate(account):
                    replace = self.get_replace_num(self.numbers[num])
                    new_accounts+=self.construct_account(account,replace,idx)
                if(len(new_accounts)==0):
                    return "ERR",account,[]
                if(len(new_accounts)==1):
                    return "RIGHT",new_accounts[0],[]
                return "ABM",account,new_accounts         


    def construct_account(self,num_list,replace_nums,index):
        right_account=[]
        for num in replace_nums:
            account = copy.copy(num_list)
            account[index]=num
            if(self.calculate(account)):
                right_account.append(account)
        return right_account

    def calculate(self,num_list):
        sum = 0
        for index,value in enumerate(num_list):
            sum += (8-index+1)*value
        return sum%11==0

    def get_replace_num(self,decompose):
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
                    if tmp_num in self.numbers: replace.append(self.numbers.index(tmp_num))
        return replace