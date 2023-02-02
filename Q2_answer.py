# 재귀 함수를 통해 사이클 수 구하기
    # 재귀 할때마다 cnt += 1
    # 재귀 중 원래의 값과 같은 값이 나오면 return
        # 단, 사이클이 1 이상일 경우
    # x // 10 -> x의 앞 숫자, x % 10 -> 뒷 숫자

def find_cycle(origin, now, cnt):
    if cnt > 0:
        if origin == now:
            return cnt

    temp = now // 10 + now % 10
    nxt = 10 * (now % 10) + temp % 10
    
    return find_cycle(origin, nxt, cnt + 1)

N = int(input())

count = find_cycle(N, N, 0)

print(count)