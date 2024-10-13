n, m = [int(number) for number in input().split()]

n_set = set(input() for _ in range(n))
m_set = set(input() for _ in range(m))

print(*(n_set & m_set), sep="\n")
