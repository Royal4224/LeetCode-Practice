import heapq


class Solution:

    def kWeakestRows(self, mat, k: int):
        queue = []
        output = []
        for i in range(len(mat)):
            soldier_count = 0
            for p in mat[i]:
                if p == 1:
                    soldier_count += 1
            queue.append((soldier_count, len(mat[i]), i))
            heapq.heapify(queue)

        while k >= 1:
            _, _, index = queue.pop(0)
            output.append(index)
            heapq.heapify(queue)
            k -= 1

        return output
