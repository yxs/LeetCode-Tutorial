from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        existed = set()  # set 查找快
        ans = []
        last = dict()
        for name in names:
            if name not in existed:
                existed.add(name)
                ans.append(name)
                continue
            i = last.get(name, 1)  # 当前存在的 name 个数
            while True:
                new_name = f"{name}({i})"  # 拼凑字符串好过 list 分片或 re
                if new_name not in existed:
                    existed.add(new_name)
                    ans.append(new_name)
                    last[name] = i
                    break
                i += 1

        return ans


names = ["kaido", "kaido(1)", "kaido", "kaido(1)"]
sol = Solution()
print(sol.getFolderNames(names))
