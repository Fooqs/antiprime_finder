file = open('primes_10000.txt','r')
primes = file.readlines()
primes = [int(x[:-1]) for x in primes]
file.close

print()
print('Finding Whore Numbers')
while True:
    top_fs, top_n = [], 0
    for given in range(1,int(input('Search from 1 to... '))+1):
        if given > 60 and given % 60 != 0: continue
        # if given > 1 and given % 2 != 0: continue
        # if given > 1700 and given % 280 != 0: continue
        # if given > 3000 and given % 1260 != 0: continue

        prime_fs, f_count, save_giv = [], 0, given
        while True:
            for i in primes:
                if given % i == 0:
                    prime_fs.append(i)
                    given /= i
            
            if given == 1: break
            elif f_count == len(prime_fs):
                prime_fs.append(given)
                break
            f_count = len(prime_fs)


        unique_fs, factors = set(prime_fs), [1]
        for f in unique_fs:
            copy = factors.copy()
            for power in range(prime_fs.count(f)+1):
                for i in copy: factors.append(i*(f**power))
        factors = list(set(factors))
        factors.sort()

        if len(factors) > len(top_fs):
            top_fs, top_n = factors.copy(), save_giv
            print('\n\n'+str(save_giv)+':', len(factors), 'Factors\n'+str(factors))
        else:
            print('.',end='')
    print('\n\n\n')
    print('WINNER:', top_n, )
    print('\n\n\n')