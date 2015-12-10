class Page:

    def __init__(self, id, pid):
        self.frame= None
        self.frecuencyCount= 0
        self.id= id
        self.pid= pid

    def registryFrame(self, frame):
        self.frame= frame

    def incrementFrecuencyCount(self):
        self.frecuencyCount += 1