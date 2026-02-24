few_shots_students = [
    {
        'Question': "How many students are there in the AI class?",
        'SQLQuery': "SELECT COUNT(*) FROM STUDENT WHERE CLASS = 'AI'",
        'SQLResult': "Result of the SQL query",
        'Answer': "6"
    },
    {
        'Question': "What is the average marks of students in the Machine Learning class?",
        'SQLQuery': "SELECT AVG(MARKS) FROM STUDENT WHERE CLASS = 'Machine Learning'",
        'SQLResult': "Result of the SQL query",
        'Answer': "90.0"
    },
    {
        'Question': "Which student has the highest marks and which subject did they choose?",
        'SQLQuery': "SELECT NAME, CLASS, MARKS FROM STUDENT ORDER BY MARKS DESC LIMIT 1",
        'SQLResult': "Result of the SQL query",
        'Answer': "Riya, AI, 99"
    },
    {
        'Question': "What is the total marks of all students in the Web Dev class?",
        'SQLQuery': "SELECT SUM(MARKS) FROM STUDENT WHERE CLASS = 'Web Dev'",
        'SQLResult': "Result of the SQL query",
        'Answer': "629"
    },
    {
        'Question': "What is the average marks of students in Cyber Security class, section B?",
        'SQLQuery': "SELECT AVG(MARKS) FROM STUDENT WHERE CLASS = 'Cyber Security' AND SECTION = 'B'",
        'SQLResult': "Result of the SQL query",
        'Answer': "79.5"
    },
    {
        'Question': "What is the total marks of students in Cloud Computing class, section A?",
        'SQLQuery': "SELECT SUM(MARKS) FROM STUDENT WHERE CLASS = 'Cloud Computing' AND SECTION = 'A'",
        'SQLResult': "Result of the SQL query",
        'Answer': "267"
    },
    {
        'Question': "Who is the student with the lowest marks in Data Science class?",
        'SQLQuery': "SELECT NAME FROM STUDENT WHERE CLASS = 'Data Science' ORDER BY MARKS ASC LIMIT 1",
        'SQLResult': "Result of the SQL query",
        'Answer': "Isha"
    }
]