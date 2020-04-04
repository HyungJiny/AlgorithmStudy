def solution(board, moves):
    answer = 0
    board_stack = [[] for i in range(len(board[0]))]
    for b in board:
        for i, d in enumerate(b):
            if d == 0: continue
            board_stack[i].append(d)
    box = []
    for move in moves:
        if len(board_stack[move-1]) == 0: continue
        doll = board_stack[move-1].pop(0)
        if len(box)==0 or box[-1] != doll:
            box.append(doll)
        else:
            box.pop(-1)
            answer += 1

    return answer*2