class Twitter:
    class Node:
        def __init__(self):
            self.followee = set()
            self.tweet = list()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.recentMax = 10
        self.tweetTime = dict()
        self.user = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.user:
            self.user[userId] = Twitter.Node()
        self.user[userId].tweet.append(tweetId)
        self.time += 1
        self.tweetTime[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.user:
            return list()
        ans = self.user[userId].tweet[-10:][::-1]
        for followeeId in self.user[userId].followee:
            if followeeId in self.user:
                opt = self.user[followeeId].tweet[-10:][::-1]
                i, j, combined = 0, 0, list()
                while i < len(ans) and j < len(opt):
                    if self.tweetTime[ans[i]] > self.tweetTime[opt[j]]:
                        combined.append(ans[i])
                        i += 1
                    else:
                        combined.append(opt[j])
                        j += 1
                combined.extend(ans[i:])
                combined.extend(opt[j:])
                ans = combined[:10]
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId not in self.user:
                self.user[followerId] = Twitter.Node()
            self.user[followerId].followee.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId in self.user:
                self.user[followerId].followee.discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
