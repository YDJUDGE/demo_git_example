import csv

CARS_CSV_FILE = "cars.csv"
BIRTH_MONTH_FILE = "birth_months.csv"

def read_csv_cars():
    with open(CARS_CSV_FILE, "r") as f:
        csv_reader = csv.reader(f, delimiter=" ")

        for line in csv_reader:
            print(line)

            print(line[1], line[-1])

def read_csv_as_dict():
    with open(CARS_CSV_FILE) as f:
        csv_reader = csv.DictReader(f, delimiter=",")

        print("headers:", csv_reader.fieldnames)

        for line in csv_reader:
            print(line)

def write_csv_dict():
        NAME = "name"
        MONTH = "birth_month"
        DEPARTMENT = "department"
        fieldnames = [NAME, MONTH, DEPARTMENT]

        with open(BIRTH_MONTH_FILE, "w", newline="") as f:
            csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
            csv_writer.writeheader()

            row = {
                NAME: "Sam",
                MONTH: "Jan",
                DEPARTMENT: "IT"
                }
            row2 = {
                NAME: "Jack",
                MONTH: "March",
                DEPARTMENT: "Marketing"
            }

            row3 = {
                NAME: "Peter",
                MONTH: "April",
                DEPARTMENT: "Cashier"
            }

            rows = [row2, row3]
            csv_writer.writerow(row)
            csv_writer.writerows(rows)

def main():
    # read_csv_cars()
    # read_csv_as_dict()
    write_csv_dict()

if __name__ == "__main__":
    main()
