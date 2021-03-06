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
        return [[employee.get_name(), employee.get_min_hours(), employee.get_max_hours(), employee.get_hours_worked(), employee.get_overtime_hours()] for employee in self.employees]

    def add_employee_to_slot(self, employee):
        self.schedule[self.next_available_slot].append(employee.get_name())
        employee.add_hours_worked(1)
        self.next_available_slot = self.next_available_slot +1
        
    def create_minimal_schedule(self):
        #Only assigns hours to fill the minimum required work hours for each employee
        #for each employee add them once for each hour in their minimum required hours

        #iniitalize empty schedule
        self.schedule = [[] for _ in range(self.total_work_week_hours)]

        for employee in self.employees:
            if not employee.finished_minimum_hours():
                #only add employees who have not finished their minimum hours
                for _ in range(employee.get_min_hours()):
                    #if there are no more slots available reset to start of schedule
                    if self.next_available_slot >= self.total_work_week_hours:
                        self.next_available_slot = 0
                        
                    if employee.get_name() not in self.schedule[self.next_available_slot]:
                        self.add_employee_to_slot(employee)

                    

    def fill_empty_slots(self):
        #Fill any remaining slots with employees who have not reached max working hours
        for employee in self.employees:
            if employee.can_still_work():
                for _ in range(employee.get_max_hours()-1):
                    #if schedule is full stop trying to add employees
                    if self.next_available_slot >= self.total_work_week_hours:
                        break
                    if employee.get_name() not in self.schedule[self.next_available_slot]:
                        self.add_employee_to_slot(employee)
        
    def fill_overtime(self):
        #Fills any empty slots with employees with overtime
        while self.next_available_slot < self.total_work_week_hours:
            for employee in self.employees:
                #if schedule is full stop trying to add employees
                if self.next_available_slot >= self.total_work_week_hours:
                    break
                if employee.get_name() not in self.schedule[self.next_available_slot]:
                    self.add_employee_to_slot(employee)

    def create_schedule(self):
        self.next_available_slot = 0
        #sort employees based on total hours they can work
        self.employees.sort(key=lambda x: x.get_min_hours(), reverse=True)

        #Creates a schedule fulfilling the minimum requirements for the week 
        self.create_minimal_schedule()

        #If there are empty slots then try and fill it with employees
        if [] in self.schedule:
            self.fill_empty_slots()

        #If there are empty slots then try and fill it with employees with overtime
        if [] in self.schedule:
            self.fill_overtime()

    
    
    def get_formatted_schedule(self, shape= (5,8)):
        #returns a reshaped list of employees in the order of the schedule
        reshaped_schedule = numpy.array([(", ").join(i) for i in self.schedule]).reshape(shape)

        #Sort each day so that employees have consequtive time slots
        for i,x in enumerate(reshaped_schedule):
            reshaped_schedule[i] = sorted(x)
            
        reshaped_schedule = numpy.rot90(reshaped_schedule,-1)
        
        return reshaped_schedule






    
    
