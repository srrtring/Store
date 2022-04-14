# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import date, timedelta

class Store:
    # Variables de clase

    Warehouse = dict()
    Warehouse = {
        'store_1': {"open_cases": 4, "closed_cases": 10},
        'store_2': {"open_cases": 22, "closed_cases": 5}
    }

    # Constructor
    def __init__(self, date_first, date_end):
        # Variables de instancia
        self.date_first = date_first
        self.date_end = date_end

    # Métodos
    def incident_status(self):
        stats_store = []

        for i in self.Warehouse:
            open_cases = self.Warehouse[i]['open_cases']
            closed_cases = self.Warehouse[i]['closed_cases']
            n_cases = open_cases + closed_cases
            average_solved_cases = round(closed_cases / n_cases)
            max_current_solution = (open_cases / n_cases)

            stats_store.append(
                {
                    'Store': i,
                    'open_cases': open_cases,
                    'closed_cases': closed_cases,
                    'average_solved_cases': average_solved_cases,
                    'max_current_solution': max_current_solution
                }
            )

        return stats_store

current_date = date.today()
old_date = current_date - timedelta(3)

stores_incident = Store(old_date, current_date)

print(stores_incident.incident_status())

