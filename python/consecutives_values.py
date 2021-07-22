if __name__ == '__main__':
    n = int(input())
    def consecution(n):
        nums = list(range(1,(n+1)))
        onum=str()
        for x in nums:
            onum+=str(x)
        print(onum)
    consecution(n)