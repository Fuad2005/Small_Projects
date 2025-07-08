with open('passwords.txt', 'w') as f:
    for i in range(0, 10_000_000):
        f.write(str(i) + '\n')