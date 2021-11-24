for t in range(int(input())):
    n, m, k = map(int, input().split())

    if n == 1:
        t = input()
        print("yes")
    else:
        # print("ph")
        h = list(map(int, input().split()))
        # print(h)
        ck = 0
        for i in range(n - 1):
            if h[i] - h[i + 1] >= k:
                if h[i+1]==0:
                    m+=h[i]
                else:
                    m += (h[i] - h[i + 1])
                    if h[i+1]>=k:m+=k
                    else:m+=h[i+1]
                #print(11,i,m)
            elif h[i + 1] - h[i] >k:
                # print(h[i+1]-h[i]-k)
                if h[i]==0:
                    m-=h[i+1]-k
                else:
                    m-=(h[i+1]-k-h[i])
                #m-=(h[i+1])
                #m -= (h[i + 1] - h[i] - k)
                if m < 0:
                    print("no")
                    ck = 1
                    break
                #print(22,i,m)
            elif abs(h[i] - h[i + 1]) >= 0:
                if h[i] - h[i + 1] > 0:
                    if h[i + 1] == 0:
                        m += h[i]
                    else:
                        m += (h[i] - h[i + 1])
                        if h[i + 1] >= k:
                            m += k
                        else:
                            m += h[i + 1]
                    #m += h[i] - h[i + 1] + k
                else:


                    if h[i+1]>=k:
                        m+=(h[i]-h[i + 1] + k)
                    else:
                        #h[i+1]-=k
                        m += h[i]
                #print(33,i,m)

        if ck != 1:
            print("yes")



