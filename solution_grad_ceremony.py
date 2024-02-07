import argparse

def calculate_ways_and_miss_probability(n):
    # dp[i][0] stores the count of sequences ending with 'A' up to day i
    # dp[i][1] stores the count of sequences ending with 'N' up to day i
    # dp[i][2] stores the count of all valid sequences up to day i
    dp = [[0, 0, 0] for _ in range(n+1)]
    
    dp[0] = [1, 0, 1]  # No days means only one way to 'attend' (doing nothing) -initialize in Attending
    
    for i in range(1, n+1):
        print("\n", "=" * 100)
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in dp]))
        # Attend on day i
        dp[i][0] = dp[i-1][2]  # All sequences from previous day are valid if attending today
        
        # Not attend on day i, can't follow three consecutive Ns
        if i-1 >= 0:
            dp[i][1] += dp[i-1][0]  # Can miss today if yesterday was attended
        if i-2 >= 0:
            dp[i][1] += dp[i-2][0]  # Can miss two days if day before yesterday was attended
        if i-3 >= 0:
            dp[i][1] += dp[i-3][0]  # Can miss three days if three days ago was attended
        
        # Total valid sequences up to day i
        dp[i][2] = dp[i][0] + dp[i][1]
    
    # Answer of 1: Total number of ways to attend classes over N days
    total_ways = dp[n][2]
    
    # Answer of 2: Number of ways leading to missing graduation
    # All sequences ending with N on the last day + special handling for four consecutive Ns
    missing_graduation = dp[n][1]

    print("\n", "=" * 100)
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in dp]))
    
    answer = f"{missing_graduation}/{total_ways}"
    return answer


def main():
    parser = argparse.ArgumentParser(description="Calculate the number of ways to attend classes and the probability of missing the graduation ceremony.")
    parser.add_argument('N', type=int, help='The number of days until the graduation ceremony.')

    args = parser.parse_args()

    print(calculate_ways_and_miss_probability(args.N))

if __name__ == "__main__":
    main()
