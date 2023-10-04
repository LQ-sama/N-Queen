import torch as nn
import time
##用回溯法进行查找
start_time = time.time()
to_num = 0
board_size = 8
bs = board_size
board = nn.zeros(bs,bs)
device = 'cuda:0'
board = board.to(device)
board[0,0]=1

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

##检测整个棋盘是否符合标准
def all_detect(x: nn.Tensor):
        for i in range(bs):
            for j in range(bs):
                if x[i,j]==1:
                    if not single_detect(x,i,j):
                        return False

        else:
            return True

num = 0
#放单个皇后
def put(board:nn.Tensor,i):
    global  num
    for j in range(bs):

        board[i,j]=1
        if all_detect(board) and i<bs-1 :
            put(board,i+1)
        if all_detect(board) and i==bs-1:
            num+=1
            print('这是第：',num,'种解法')
            print(board)
        board[i,j]=0
    if j==bs-1 and not all_detect(board):
        for k in range(bs):
            if board[k]==1 and k!=0:
                board[k-1]=1
                board[k]=0
                put(board,i)

put(board,0)
end_time = time.time()
print('用时为：',end_time-start_time,'秒')



