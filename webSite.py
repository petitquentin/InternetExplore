class WebSite:
    def __init__(self, url, previous = []):
        self.url = url
        self.nbVisit = 1
        self.previous = previous

    def __str__(self):
        return "["+str(self.url)+", "+str(self.nbVisit)+", "+str(self.previous) + "]"

    def __repr__(self):
        return "["+str(self.url)+", "+str(self.nbVisit)+", "+str(self.previous) + "]"

    def __lt__(self, other):
        if (self.nbVisit < other.nbVisit):
            return True
        elif (self.nbVisit == other.nbVisit):
            return self.url < other.url
        else:
            return False

    def __gt__(self, other):
        if (self.nbVisit > other.nbVisit):
            return True
        elif (self.nbVisit == other.nbVisit):
            return self.url > other.url
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, WebSite):
            return self.url == other.url
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def fusion(self, other):

        for i in other.previous:
            if(i not in self.previous):
                self.previous.append(i)
                self.nbVisit = self.nbVisit + 1