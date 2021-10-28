# CodingInterview_absolutereality
Recursion coding interview for application at https://www.absolutereality.de/
# Description:
The program reads a set of employee data from the input file and creates a schedule and atleast 10 permutations where possible. Employees are required to fulfil their minimum time requirements but are not allowed to exceed their maximum time. If there are empty timeslots leftover employees are assigned these time slots with overtime.

# Usage:
```
compute.exe <filename> [options]
Options:
    -max <value> specify number of permutations. default 10
```

## Releases:
Source code and exe file can be found here:
[v1.0](https://github.com/JonathanWu1/CodingInterview_absolutereality/releases/tag/v1.0.0).
[v1.1](https://github.com/JonathanWu1/CodingInterview_absolutereality/releases/tag/v1.1).
    
## Issues with generating permutations:
The permutation algorithm was made by me so there are limitations to it's usage.
The correct way to implement the permutations would be to use itertools.permutations function
or to use a known algorithm (Heap's Permutation Algorithm),
I decided to not use I think it defeats the purpose of the project.

The current permutation algorithm is limited to a max of 16 permutations. 
Going higher than 16 will make it search for 32 permutations and my terminal is not able to process it
This is because the schedule is permutated after being created instead of permutating on during the creation phase, it ensures the maximum number of employees are able to fulfill the minimum required hours for the week.

## Edge Cases

Case1: High Employee Count each with High Work hours
high_employee_high_hours.json
```
{ 
	"Name":"",
	"Person":[	{"Id":1,"Name":"A", "MinHoursPerWeek":"40","MaxHoursPerWeek":"40" },
				{"Id":2,"Name":"B", "MinHoursPerWeek":"40","MaxHoursPerWeek":"40" },
				{"Id":3,"Name":"C", "MinHoursPerWeek":"40","MaxHoursPerWeek":"40" },
				{"Id":4,"Name":"D", "MinHoursPerWeek":"40","MaxHoursPerWeek":"40" },
				...
				{"Id":20,"Name":"T", "MinHoursPerWeek":"40","MaxHoursPerWeek":"40" }]
}
```
In the scenario every employee is working every hour of the week each of the timeslots are exactly the same and more permutations cannot be created

Case2: Each employee has more minimum hours than the number of working time slots in the week so the same problem occurs where each timeslot is exacly the same permutations cannot be created
too_many_min_hours.json
```
    { 
	"Name":"configuration1",
	"Person":[	{"Id":1,"Name":"Tim", "MinHoursPerWeek":"100","MaxHoursPerWeek":"1" },
				{"Id":2,"Name":"Kim", "MinHoursPerWeek":"100","MaxHoursPerWeek":"1" },
				{"Id":3,"Name":"Tom", "MinHoursPerWeek":"100","MaxHoursPerWeek":"1" }
	    ]
    }
```

