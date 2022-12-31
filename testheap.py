import heapq

H = []

heapq.heapify(H)

heapq.heappush(H,(0,50))
heapq.heappush(H,(30,75))
heapq.heappush(H,(40,80))
heapq.heappush(H,(10,87))
heapq.heappush(H,(100,120))
heapq.heappush(H,(150,200))
print(heapq.heappop(H))
print(heapq.heappop(H))
print(heapq.heappop(H))
print(heapq.heappop(H))