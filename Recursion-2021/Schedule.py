import math
import numpy
from itertools import permutations
class Schedule:
    def __init__(self, employees, schedule = [],  **kwargs):
        self.employees = employees
        self.schedule = schedule
        self.total_work_week_hours = kwargs.get("total_work_week_hours")

        #set default work week hours 
        if self.total_work_week_hours == None:
            self.total_work_week_hours = 40

    #Some get methods for class variables
    def get_schedule(self):
        return self.schedule

    def get_employees(self):
        return self.employees

    def get_employee_hours(self):
        #Returns list of employee data for employees in the schedule
        return [[employee.get_name(), employee.get_min_hours(), employee.get_max_hours(), employee.get_hours_worked()] for employee in self.employees]

    def create_minimal_schedule(self):
        #Only assigns hours to fill the minimum required work hours for each employee
        #for each employee add them once for each hour in their minimum required hours

        #iniitalize empty schedule
        self.schedule = [[] for _ in range(self.total_work_week_hours)]

        next_available_slot = 0

        for employee in self.employees:
            if not employee.finished_minimum_hours():
                #only add employees who have not finished their minimum hours
                for _ in range(employee.get_min_hours()):
                    self.schedule[next_available_slot].append(employee.get_name())
                    next_available_slot = next_available_slot +1

                    #if there are no more slots available reset to start of schedule
                    if next_available_slot >= self.total_work_week_hours:
                        next_available_slot = 0

                employee.add_hours_worked(employee.get_min_hours())

        return next_available_slot


    def fill_empty_slots(self, next_available_slot):
        #Fill any remaining slots with employees who have not reached max working hours
        for employee in self.employees:
            if employee.can_still_work():
                for _ in range(employee.get_max_hours()):
                    #if schedule is full stop trying to add employees
                    if next_available_slot >= self.total_work_week_hours:
                        break
                    self.schedule[next_available_slot].append(employee.get_name())
                    employee.add_hours_worked(1)
                    next_available_slot = next_available_slot +1
                    

    def create_schedule(self):
        #Creates a schedule fulfilling the minimum requirements for the week 
        next_available_slot = self.create_minimal_schedule()

        #If there are empty slots then try and fill it with employees
        if next_available_slot < len(self.schedule):
            self.fill_empty_slots(next_available_slot)
    
    
    def get_formatted_schedule(self, shape= (8,5)):
        #returns a reshaped list of employees in the order of the schedule
        return numpy.array([(", ").join(i) for i in self.schedule]).reshape(shape)






    
    
