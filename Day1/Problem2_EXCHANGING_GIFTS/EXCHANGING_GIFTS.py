def solve():
    # Prompt for n and m
    print("Enter total members (n) and gift exchanges (m):")
    n, m = map(int, input("> ").split())

    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)

    # Prompt for each gift exchange
    print(f"\nEnter {m} gift exchanges (format: giver receiver):")
    for i in range(1, m + 1):
        giver, receiver = map(int, input(f"Exchange {i}: ").split())
        out_degree[giver] += 1
        in_degree[receiver] += 1

    # Find the youngest member
    for i in range(1, n + 1):
        if out_degree[i] == 0 and in_degree[i] == n - 1:
            print(f"\nThe youngest member is: {i}")
            return

    print("\nNo valid youngest member found: -1")


if __name__ == "__main__":
    solve()