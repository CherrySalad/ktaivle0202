def solution(lottos, win_nums):
    cnt_zero = 0
    win_nums_set = set(win_nums)
    correct = 0
    ranking = [6, 6, 5, 4, 3, 2, 1]
    
    for num in lottos:
        if num == 0:
            cnt_zero += 1
        else:
            if num in win_nums_set:
                correct += 1
                
    answer = []
    answer.append(ranking[correct + cnt_zero])
    answer.append(ranking[correct])
    
    return answer

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
answer = solution(lottos, win_nums)
print(answer)