import torch as nn
import time
#8的8次方进行遍历
start_time = time.time()
to_num = 0
board_size = 8
bs = board_size
board = nn.zeros(bs,bs)
address = [0,0,0,0,0,0,0,0]  #用一个列向量来表示各个行上，皇后所在的列的位置

##检测棋盘的i,j位置是否是米字形中唯一的数且在中心
def single_detect(x: nn.Tensor, i, j):
    row_sum = x[i,:].sum()
    col_sum = x[:,j].sum()
    dia_sum = x.flip(0).diagonal(offset = i+j -bs+1).sum()
    idia_sum = x.diagonal(offset = j-i).sum()
    num = row_sum + col_sum + dia_sum + idia_sum
    if x[i,j]==1 and num == 4:
        return True
    else :
        return False


def all_detect(x:nn.Tensor, address):
         if  not single_detect(x,0,address[0]) :
             return False
         elif not single_detect(x,1,address[1]):
             return False
         elif not single_detect(x,2,address[2]):
             return False
         elif not single_detect(x,3,address[3]):
             return False
         elif not single_detect(x,4,address[4]):
             return False
         elif not single_detect(x,5,address[5]):
             return False
         elif not single_detect(x,6,address[6]):
             return False
         elif not single_detect(x,7,address[7]):
             return False

         else :

            global to_num
            to_num+=1
            print('这是第：',to_num,'种解法')
            print('此时的棋盘：',x)
            print('此时的位置向量：',address)


            return True

##检测整个棋盘是否符合要求。符合就返回True。
def put_queen(x:nn.Tensor,address):
    x = nn.zeros(bs,bs)
    for i in range(bs):
        x[i, address[i]] = 1
    return x

while address[7] != 7  :
    for a in range(bs):
        for b in range(bs):
            for c in range(bs):
                for d in range(bs):
                    for e in range(bs):
                        for f in range(bs):
                            for g in range(bs):
                                for h in range(bs):
                                    address[0] = a
                                    address[1] = b
                                    address[2] = c
                                    address[3] = d
                                    address[4] = e
                                    address[5] = f
                                    address[6] = g
                                    address[7] = h

                                    board = put_queen(board,address)
                                    all_detect(board, address)

end_time = time.time()
print('用时为：',end_time-start_time,'秒')





