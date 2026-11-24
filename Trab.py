def listiren(sequencia):
    n = len(sequencia)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if sequencia[i] > sequencia[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


sequencia = [10, 22, 9, 33, 21, 50, 41, 60]

print(listiren(sequencia))
