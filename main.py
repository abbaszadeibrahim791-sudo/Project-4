class Human:
    def __init__(self,name,job):
        self.name=name
        self.job=job
        self.money=0
    def work(self):
        self.money=self.money+self.job.gelir
        print(self.name,"ise gedir",self.job.place)
        print(self.name,"qazandi",self.job.gelir,"Total:",self.money)
class Job:
    def __init__(self,place,gelir):
        self.place=place
        self.gelir=gelir
job=Job("Step Academy",1000)
worker=Human("Ibrahim",job)
worker.work()
worker.work()