from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = list(tiles)
        answer = set()
        for i in range(1, len(tiles) + 1):
            answer = answer | set(permutations(tiles, i))

        return len(answer)
