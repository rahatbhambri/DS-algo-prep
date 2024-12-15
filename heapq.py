class heapq:
    
    def getLeft(self, hp, i):
        return hp[2*i + 1] if (2*i + 1) < len(hp) else 10**5
    
    def getRight(self, hp, i):
        return hp[2*i + 2] if (2*i + 2) < len(hp) else 10**5
    
    def getParent(self, hp, i):
        return hp[i//2]
    
    def heapify(self, l):
        n = len(l)
        for i in range(n//2, -1, -1):
            self.siftDown(l, i)
    
    
    def siftDown(self, hp, i):
        
        left = self.getLeft(hp, i)
        right = self.getRight(hp, i)
        
        curr = hp[i]
        if left and left < curr and left < right:
            hp[i], hp[2*i+1] = hp[2*i+1], hp[i] 
            self.siftDown(hp, 2*i+1)
        elif right and right < curr and right < left:
            hp[i], hp[2*i+2] = hp[2*i+2], hp[i]
            self.siftDown(hp, 2*i+2)
    
    def heappop(self, hp):
        
        ans = hp[0]
        m = len(hp)
        lel = hp.pop()
        if m == 1:
            return ans
        
        hp[0] = lel
        self.siftDown(hp, 0)
        
        print(hp)
        return ans
        
    
    def heappush(self, hp, val):
        
        hp.append(val)
        n = len(hp)
        i = n-1
        
        while self.getParent(hp, i) > hp[i]:
            hp[i//2], hp[i] = hp[i], hp[i//2]
            i = i//2


l = [12, 6, 3, 7, 9, 4, -1]

hq = heapq()
hq.heapify(l)

print(l)

print(hq.heappop(l))
print(hq.heappop(l))
print(hq.heappop(l))
print(hq.heappop(l))

print(l)

hq.heappush(l, -2)
hq.heappush(l, 1)
hq.heappush(l, 8)

print(l)

print(hq.heappop(l))


        
        
        
