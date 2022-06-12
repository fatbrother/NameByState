class TrieNode:
    def __init__(self):
        self.isWord = False
        self.next = {}

class TrieTree:
    def __init__(self):
        self.root = TrieNode()        

    def append(self, word: str):
        n = self.root
        for i in word:
            if i not in n.next:
                n.next[i] = TrieNode()
            n = n.next[i]
        n.isWord = True     

    def extend(self, l: list):
        for v in l:
            self.append(v)
        return   

    def __contains__(self, word: str):
        n = self.root
        for i in word:
            if i not in n.next:
                return False
            else:
                n = n.next[i]
        return n.isWord

    def startsWith(self, prefix: str):
        n = self.root
        for i in prefix:
            if i not in n.next:
                return
            else:
                n = n.next[i]
        return n

    def getBelow(self, v):

        def DFS(now: TrieNode, v: str):

            res = []

            if now == None:
                return

            if v in self:
                res.append(v)

            for key, value in now.next.items():
                res.extend(DFS(value, v + key))

            return res

        list = DFS(self.startsWith(v), v)
        if list:
            list.sort()
        return list