import json
import argparse
import csv
import numpy

from Employee import Employee
from Schedule import Schedule
from permutations import create_permutations
               
def main():
    parser = argparse.ArgumentParser(description="Employee data")

    #employee config file name parser
    parser.add_argument("config_file_name", default = "configuration.json")

    #let the user specify number of variations. default max variations: 20
    parser.add_argument("-max", default = 10, type=int, required=False)

    args = parser.parse_args()

    #Try opening file in current directory
    try:
        with open(args.config_file_name) as ed:
            file_data = json.load(ed)
    except FileNotFoundError as e:
        print(f"File {args.config_file_name} not found in directory")
        return

    #Create list of employee objects
    employees = [Employee(e.get("Id"), e.get("Name"),int(e.get("MinHoursPerWeek")),int(e.get("MaxHoursPerWeek"))) for e in file_data.get("Person")]
    
    #Create initial schedule
    schedule = Schedule(employees)
    schedule.create_schedule()

    #Permutate the initial schedule
    permutations_ = create_permutations(schedule, args.max, 40)
    
    #write to csv
    file_name = file_data.get("Name")
    if not file_name:
        file_name = args.config_file_name
    with open(f"{file_name}.csv", "w", newline='') as output:
        output_writer = csv.writer(output, delimiter=",")
        for i,permutation in enumerate(permutations_):
            #reshape schedule
            reshaped_permutation = permutation.get_formatted_schedule()

            #Get employee work hour data
            employee_data = numpy.array(permutation.get_employee_hours())

            #Create list of time slots to be printed to csv
            time_slot = numpy.array([f"{10+j}-{10+j+1} hrs" for j in range(reshaped_permutation.shape[0])])
            time_slot = time_slot.reshape((reshaped_permutation.shape[0], 1))

            #Add the time slot to front of employee names
            reshaped_permutation = numpy.hstack((time_slot, reshaped_permutation))

            #Add empty column at the end of the schedule data
            reshaped_permutation = numpy.pad(reshaped_permutation, ((0,0),(0,1)), 'constant', constant_values="")

            #Pad end of the x-axis of the the smaller array to match the dimension of the larger array
            if employee_data.shape[0] > reshaped_permutation.shape[0]:
                reshaped_permutation = numpy.pad(reshaped_permutation, ((0,employee_data.shape[0]-reshaped_permutation.shape[0]),(0, 0)), 'constant', constant_values="")
            else:
                employee_data = numpy.pad(employee_data, ((0,reshaped_permutation.shape[0]-employee_data.shape[0]),(0, 0)), 'constant', constant_values="")
                
            #Horizontal stack the schedule and work hours
            data = numpy.hstack((reshaped_permutation, employee_data))
            
            #Write Headers
            output_writer.writerow([f"Distribution {i+1}", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "", "", "WorkingHoursMin", "WorkingHoursMax", "TotalWorkingHours", "Overtime"])
            
            #Print schedule data
            for row in data:
                output_writer.writerow(row)

            output_writer.writerow([""])


if __name__ == "__main__":
    main()
    