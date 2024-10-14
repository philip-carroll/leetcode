class RecentCounter:

    def __init__(self):
        self.requests = []
        self.t = 0

    def check_t(self, i):
        if i >= self.t - 3000:
            return True

        return False

    def ping(self, t: int) -> int:
        self.t = t
        self.requests.append(self.t)
        self.requests = list(filter(self.check_t, self.requests))
        return len(self.requests)


if __name__ == '__main__':
    # Your RecentCounter object will be instantiated and called as such:
    obj = RecentCounter()

    print(obj.ping(1))
    print(obj.ping(100))
    print(obj.ping(3001))
    print(obj.ping(3002))
