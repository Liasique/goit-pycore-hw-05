import sys  #this is to get command line arguments

# Function to load logs from a file
def load_logs(file_path: str) -> list:
    try:
        # this is to try open file in read mode
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()  # for read all lines and return as list
    except FileNotFoundError:
        # If file not found, print error message and return empty list
        print("File not found")
        return []

# Function to count how many times each log level appears in log.txt
def count_logs_by_level(logs: list) -> dict:
    levels = ["INFO", "DEBUG", "ERROR", "WARNING"]  
    counts = {level: 0 for level in levels} 
    for line in logs:  
        for level in levels:  # check each level
            if f" {level} " in line:  
                counts[level] += 1  
    return counts  # return the final count for each level

# main function to execute  script
def main():
    # first need to check if user provided the file path as argument
    if len(sys.argv) < 2:
        print("❗ Please provide the path to the log file.")
        return

    file_path = sys.argv[1]  # tthis is to get et file path from the cli
    logs = load_logs(file_path)  
    # Run the program only if this file is the main script
    if not logs:
        return  #this in case if no logs to stop program
    
    counts = count_logs_by_level(logs) 

    
    print(f"Total lines in file: {len(logs)}")
    
  
    print("\nРівень логування  | Кількість")
    print("------------------|-------")
    
    # Print each level and its count
    for level, count in counts.items():
        print(f"{level:<18}| {count}")


if __name__ == "__main__":
    main()
  
#to check in terminal:
"""python task3/logs.py task3/logs.txt"""

#tERMINAL OUTPUT:
"""
Total lines in file: 12

Рівень логування  | Кількість
------------------|-------
INFO              | 4
DEBUG             | 3
ERROR             | 2
WARNING           | 1
"""

       #parse_log_line(line: str) -> dict
      # def parse_log_line(line: str) -> dict:
       #split()
       #load_logs(file_path: str) -> list ----- Завантаження лог-файлів виконує функція +
       #parse_log_line
       #filter_logs_by_level(logs: list, level: str) -> list
       #count_logs_by_level(logs: list) -> dict +
       #display_log_counts(counts: dict)
       #try/except +






       #Приклад використання:
"""python [main.py](<http://main.py/>) /path/to/logfile.log"""


"""
Рівень логування | Кількість
-----------------|----------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1
"""

"""python main.py path/to/logfile.log error"""

"""
Рівень логування | Кількість
-----------------|----------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1

Деталі логів для рівня 'ERROR':
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.
"""