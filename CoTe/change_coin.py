# 프로그래머스 - 거스름돈

# Dynamic Programming (동적 프로그래밍) 사용
def solution(n, money):
    # 인덱스값을 만들 수 있는 경우의 수를 저장할 리스트
    # ex) dp[3] : 3원을 만들 수 있는 경우의 수
    dp = [0 for _ in range(n+1)]    
    dp[0] = 1

    for coin in money:      # money 리스트에 있는 각 동전마다 반복문 실행
        for i in range(coin, n+1):
            dp[i] += dp[i-coin]
            # i원에서 현재의 coin 값을 뺀 금액을 만들 수 있는 경우의 수를
            # i원을 만들 수 있는 경우의 수에 누적해서 더해나간다.
            # (i-coin원을 만드는 경우의 수가 곧 i원을 만드는 경우의 수) * coin마다 반복

    return dp[n]
