from dataclasses import dataclass

@dataclass
class Employee:
    #Class to keep track of employee work hours

    id : int
    name : str
    min_hours : int
    max_hours : int
    hours_worked : int = 0
    
    def __str__(self):
        return self.name

    #Some get methods for class variables
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_hours_worked(self):
        return self.hours_worked
    
    def get_max_hours(self):
        return self.max_hours

    def get_min_hours(self):
        return self.min_hours

    def can_still_work(self):
        #checks if employee has reached their maximum number of hours
        if self.hours_worked < self.max_hours:
            return True
        return False

    def finished_minimum_hours(self):
        #checks if employee has completed their minimum required hours
        if self.hours_worked >= self.min_hours:
            return True
        return False

    def add_hours_worked(self, hours):
        self.hours_worked = self.hours_worked + hours

