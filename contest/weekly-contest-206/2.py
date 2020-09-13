from typing import List


class Solution:
    def unhappyFriends(
        self, n: int, preferences: List[List[int]], pairs: List[List[int]]
    ) -> int:
        preferences_dict = []
        for pt in preferences:
            # value: index
            preferences_dict.append({t: i for i, t in enumerate(pt)})
        # print(preferences_dict)
        unhappy = set()

        for i, (x, y) in enumerate(pairs):
            for j in range(i + 1, len(pairs)):
                u, v = pairs[j]
                if (
                    preferences_dict[x][u] < preferences_dict[x][y]
                    and preferences_dict[u][x] < preferences_dict[u][v]
                ):
                    unhappy.add(x)
                    unhappy.add(u)
                if (
                    preferences_dict[x][v] < preferences_dict[x][y]
                    and preferences_dict[v][x] < preferences_dict[v][u]
                ):
                    unhappy.add(x)
                    unhappy.add(v)
                if (
                    preferences_dict[y][u] < preferences_dict[y][x]
                    and preferences_dict[u][y] < preferences_dict[u][v]
                ):
                    unhappy.add(y)
                    unhappy.add(u)
                if (
                    preferences_dict[y][v] < preferences_dict[y][x]
                    and preferences_dict[v][y] < preferences_dict[v][u]
                ):
                    unhappy.add(y)
                    unhappy.add(v)
        return len(unhappy)


n = 4
preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]

sol = Solution()

print(sol.unhappyFriends(n, preferences, pairs))
