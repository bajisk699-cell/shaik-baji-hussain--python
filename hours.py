class employee:
    def __work_hours(self, hours):
        if hours > 8:
            return "Overtime"
        else:
            return "Regular"
emp = employee()
print(emp._employee__work_hours(6)) 
