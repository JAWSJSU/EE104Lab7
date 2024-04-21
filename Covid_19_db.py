import psycopg2

import environ
env = environ.Env()
environ.Env.read_env()



# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    user='postgres',
    password=env('DBPASS'),
    database=env('DATABASE')
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id SERIAL PRIMARY KEY,
             first_name TEXT NOT NULL,
             middle_name TEXT NOT NULL,
             last_name TEXT NOT NULL,  
             phone_number TEXT NOT NULL,
             email TEXT NOT NULL,
             first_vaccination_date DATE,
             second_vaccination_date DATE)''')



# Insert sample tasks into the tasks table
cursor.execute("INSERT INTO tasks (first_name, middle_name, last_name, phone_number, email, first_vaccination_date, second_vaccination_date) VALUES (%s, %s, %s, %s, %s,%s,%s)",
               ('Jacob', "Alan", "Wetmore", "+1(555)453-5678" , 'wetmore.jacob@gmail.com', '2023-05-01', '2023-05-03'))
cursor.execute("INSERT INTO tasks (first_name, middle_name, last_name, phone_number, email, first_vaccination_date, second_vaccination_date) VALUES (%s, %s, %s, %s, %s,%s,%s)",
               ('John', "Michael", "Smith", '+1 (555) 123-4567', "johnsmith@example.com" , '2023-05-10', '2023-06-07'))

cursor.execute("INSERT INTO tasks (first_name, middle_name, last_name, phone_number, email, first_vaccination_date, second_vaccination_date) VALUES (%s, %s, %s, %s, %s,%s,%s)",
               ('Emily', "Jane", "Doe", '+1 (555) 987-6543', "emily.doe@example.com" , '2023-04-15', '2023-05-12'))

cursor.execute("INSERT INTO tasks (first_name, middle_name, last_name, phone_number, email, first_vaccination_date, second_vaccination_date) VALUES (%s, %s, %s, %s, %s,%s,%s)",
               ('David', "Allen", "Johnson", '+1 (555) 321-7890', "david.johnson@example.com" , '2023-03-20', '2023-04-16'))

cursor.execute("INSERT INTO tasks (first_name, middle_name, last_name, phone_number, email, first_vaccination_date, second_vaccination_date) VALUES (%s, %s, %s, %s, %s,%s,%s)",
               ('Sarah', "Elizabeth", "Brown", '+1 (555) 678-9012', "sarah.brown@example.com" , '2023-02-25', '2023-03-25'))

cursor.execute("INSERT INTO tasks (first_name, middle_name, last_name, phone_number, email, first_vaccination_date, second_vaccination_date) VALUES (%s, %s, %s, %s, %s,%s,%s)", 
               ('Jessica', 'Marie', 'Taylor', '+1 (555) 890-1234', 'jessica.taylor@example.com', '2022-12-25', '2023-01-22'))

cursor.execute("INSERT INTO tasks (first_name, middle_name, last_name, phone_number, email, first_vaccination_date, second_vaccination_date) VALUES (%s, %s, %s, %s, %s,%s,%s)", 
               ('Christopher', 'Lee', 'Anderson', '+1 (555) 456-7890', 'chris.anderson@example.com', '2022-11-30', '2022-12-28'))

cursor.execute("INSERT INTO tasks (first_name, middle_name, last_name, phone_number, email, first_vaccination_date, second_vaccination_date) VALUES (%s, %s, %s, %s, %s,%s,%s)", 
                ('Samantha', 'Lynn', 'Martinez', '+1 (555) 789-0123', 'samantha.martinez@example.com', '2022-10-25', '2022-11-22'))

cursor.execute("INSERT INTO tasks (first_name, middle_name, last_name, phone_number, email, first_vaccination_date, second_vaccination_date) VALUES (%s, %s, %s, %s, %s,%s,%s)", 
               ('Daniel', 'Joseph', 'Clark', '+1 (555) 901-2345', 'daniel.clark@example.com', '2022-09-30', '2022-10-28'))

cursor.execute("INSERT INTO tasks (first_name, middle_name, last_name, phone_number, email, first_vaccination_date, second_vaccination_date) VALUES (%s, %s, %s, %s, %s,%s,%s)", 
               ('Ashley', 'Nicole', 'Garcia', '+1 (555) 234-5678', 'ashley.garcia@example.com', '2022-08-15', '2022-09-12'))

# Commit the changes and close the connection
conn.commit()
conn.close()