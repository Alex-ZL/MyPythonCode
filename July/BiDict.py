class BiDict:

    def __init__(self):
        self.forward = {}
        self.backward = {}

    def Add(self, one, two):
        self.forward[one] = two
        self.backward[two] = one

    def __len__(self):
        return len(self.forward)

    def __getitem__(self, key):
        return self.GetForward(key)

    def __delitem__(self, key):
        if key in self.forward:
            del self.backward[self.forward[key]]
            del self.forward[key]
        else:
            del self.forward[self.backward[key]]
            del self.backward[key]

    def GetForward(self, key):
        return self.forward[key]

    def HasForward(self, key):
        return key in self.forward

    def GetBackward(self, key):
        return self.backward[key]

    def HasBackward(self, key):
        return key in self.backward

xdict = BiDict()
xdict.Add('name','alex')
xdict.Add('genda','male')
print len(xdict)
print xdict.HasForward('name')
print xdict.HasBackward('alex')
print xdict.GetBackward('male')
