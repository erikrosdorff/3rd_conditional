
# num_duration, time, time_period_comp, compound, compound_repitition
print("Enter time period you would like to compound") #t
time_period = input("Enter either Y M W: ")
def convert_time_period(time_period):  # t in the equation // amount of times in a period
    #Choose a time period
    if time_period.upper() == 'Y':
        years = int(input("Enter amount of years: "))
        time_period = int(years)
    elif time_period.upper() == 'M':
        months = int(input("Enter amount of months: "))
        time_period = int(months)  # find for different months
    elif time_period.upper() == 'W':
        weeks = int(input("Enter amount of weeks: "))
        time_period = int(weeks)
    else:
        print("Not a valid time period.")
        quit()
    return time_period

time_conversion = int(convert_time_period(time_period))
#a = p*(1 + (r/n))**(n*t)
print("Enter number of times interest is compounded: ") #find n - number of times the compound will be invested
num_times_interest_compounded_n = input(
    "Daily 'D' Weekly 'W' Monthly 'M' Yearly 'Y' or any number: ")  # Daily Weekly Monthly Yearly
# create flexibility in amount of time to compound (e.g. 2 times a week)
def find_num_of_compound(num_times_interest_compounded_n):
    if num_times_interest_compounded_n.isnumeric():
        return float(num_times_interest_compounded_n)

    char = num_times_interest_compounded_n.upper()
    if char == 'D' or char == 'DAILY':
        return 365 * time_conversion
    elif char == 'W' or char == 'WEEKLY':
        return 52 * time_conversion
    elif char == 'M' or char == 'Monthly':
        return 12 * time_conversion
    elif char == 'Y' or char == 'Yearly':
        return 1 * time_conversion

num_of_compound = int(find_num_of_compound(num_times_interest_compounded_n))