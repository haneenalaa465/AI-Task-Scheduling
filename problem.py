class Problem:
    def __init__(self, tasks):
        self.tasks = tasks
        self.schedule = []
        self.today = 0

    def action(schedule):
        # list of possible tasks w/o dependencies with their costs
        possible_routes = []
        for i in range(len(self.tasks)):
            if tasks[i].dependcies == []:
                cost = tasks[i].deadline - tasks[i].duration - self.today
                possible_routes.append([tasks[i], cost])
        

        


            
    
    def result(state):
        if state == 1:
            print(f"Task {} choosed")
        else:
            print(f"Task {} ignored")
