

1

Data Structures Semester Project, Fall ‘16

**Due Date: Monday, January 2, 11:59 P.M. (Last Day of Reading Week)**

“One of the most important applications for computers is storing and managing information. The

manner in which information is organized can have a profound effect on how easy it is to access and

manage. Perhaps the simplest but most versatile way to organize information is to store it in tables.

The relational model is centered on this idea: the organization of data into collections of two-

dimensional tables…”

[*-*](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[Foundations*](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[* ](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[of*](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[* ](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[Computer*](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[* ](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[Science*](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[,*](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[ ](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)*page 403*

Table of Contents

[Project](#br1)[ ](#br1)[Goal.............................................................................................................................................................................1](#br1)

[SQL](#br1)[ ](#br1)[Subset](#br1)[ ](#br1)[You](#br1)[ ](#br1)[Are](#br1)[ ](#br1)[Required](#br1)[ ](#br1)[to](#br1)[ ](#br1)[Support](#br1)[ ](#br1)[...............................................................................................................................1](#br1)

[Description](#br4)[ ](#br4)[of](#br4)[ ](#br4)[System](#br4)[ ](#br4)[Behavior..............................................................................................................................................4](#br4)

[Tables](#br4)[ ](#br4)[and](#br4)[ ](#br4)[Indices...................................................................................................................................................................4](#br4)

[Miscellaneous](#br5)[ ](#br5)[.........................................................................................................................................................................5](#br5)

[A](#br5)[ ](#br5)[Suggestion](#br5)[ ](#br5)[on](#br5)[ ](#br5)[How](#br5)[ ](#br5)[to](#br5)[ ](#br5)[Go](#br5)[ ](#br5)[About](#br5)[ ](#br5)[This](#br5)[ ](#br5)[Project......................................................................................................................5](#br5)

[Some](#br5)[ ](#br5)[Additional](#br5)[ ](#br5)[Useful](#br5)[ ](#br5)[materials...........................................................................................................................................5](#br5)

Project Goal

Build a simplistic relational database, and thus get some experience in using trees for real as well as building

software that isn’t just a school/HW toy.

SQL Subset You Are Required to Support

This document does not include a SQL tutorial. If you don’t know SQL already, please see [Intro](https://www.khanacademy.org/computing/computer-programming/sql)[ ](https://www.khanacademy.org/computing/computer-programming/sql)[to](https://www.khanacademy.org/computing/computer-programming/sql)[ ](https://www.khanacademy.org/computing/computer-programming/sql)[SQL:](https://www.khanacademy.org/computing/computer-programming/sql)[ ](https://www.khanacademy.org/computing/computer-programming/sql)[Querying](https://www.khanacademy.org/computing/computer-programming/sql)

[and](https://www.khanacademy.org/computing/computer-programming/sql)[ ](https://www.khanacademy.org/computing/computer-programming/sql)[managing](https://www.khanacademy.org/computing/computer-programming/sql)[ ](https://www.khanacademy.org/computing/computer-programming/sql)[data](https://www.khanacademy.org/computing/computer-programming/sql)[ ](https://www.khanacademy.org/computing/computer-programming/sql)and/or [SQL](http://www.w3schools.com/sql/)[ ](http://www.w3schools.com/sql/)[Tutorial](http://www.w3schools.com/sql/)[.](http://www.w3schools.com/sql/)

*I. CREATE TABLE*

**Example:**

**CREATE TABLE** YCStudent

(

BannerID **int**,

SSNum **int UNIQUE**,

FirstName **varchar**(255),

LastName **varchar**(255) **NOT NULL**,

GPA **decimal**(1,2) **DEFAULT** 0.00,

CurrentStudent **boolean DEFAULT** true;





2

**PRIMARY KEY** (BannerID)

);

**Comments:**

· “UNIQUE”, “NOT NULL”, and “DEFAULT” can be specified for any column.

· For purposes of this project, CREATE TABLEwill always specify a PRIMARY KEY. Primary key

columns, by definition, have unique and not null values, but can NOT have default values. A primary

key column is always indexed.

· For purposes of this project, we will assume that Boolean values are always “NOT NULL”, and can

have only two values – “true” or “false”.

· The data types you must support are: int, varchar, decimal, and boolean.

*II. CREATE INDEX*

**Example:**

**CREATE INDEX** SSNum\_Index **on** YCStudent (SSNum);

This creates a new index on the “SSNum” column in the table called “YCStudent”, and the name of the

index is “SSNum\_Index”.

*III. SELECT – Gets data from the Database*

· Get specific, or all, columns from a table:

o **SELECT** *column1*, *column2* **FROM** *table1*;

o **SELECT \* FROM** *table1;*

· Get specific, or all, columns from a table for rows that meet a certain condition. The condition can be a

complex one. The second example also includes the “distinct” clause, which means only give the

unique values of column1 and column2 – no repeats.

o **SELECT** *column2*, *column1* **FROM** *table1* **WHERE** *condition*;

o **SELECT DISTINCT** *column1*, *column2* **FROM** *table1* **WHERE** *column3=’some*

*value’* **AND** (*column4*=‘some value **OR** *column4*=‘some other value');

· Get some data and sort (**ORDER BY**) the results in ascending (**ASC**) or descending (**DESC**) order

o SELECT \* FROM YCStudent **ORDER BY** GPA **ASC**, Credits **DESC**;

· Get data from two tables by combining (based on the **WHERE** condition) the rows from the two tables

into one result set.

o **SELECT** \* **FROM** YCStudent, RIESTStudent **WHERE** YCStudent.BannerID **=**

RIETS.BannerID;

For any **WHERE** condition above, you must support any arbitrary number of conditions joined by **AND/OR**.

For any comparison, you support the following comparison operators:

· =

· <> (this means “not equal”)

· >

· <

· >=





3

· <=

*IV. SELECT functions*

You must support the following functions in a SELECT statement:

· Get the average of all the values in a column: **SELECT AVG**(column\_name) **FROM**

table\_name;

· Count the number of values in a column: **SELECT COUNT**(column\_name) **FROM** table\_name;

· Count the number of distinct values in a column: **SELECT COUNT**(**DISTINCT** column\_name)

**FROM** table\_name;

· Get the greatest of all the values in a column: **SELECT MAX**(column\_name) **FROM**

table\_name;

· Get the smallest of all the values in a column: **SELECT MIN**(column\_name) **FROM**

table\_name;

· Get the sum of all the values in a column: **SELECT SUM**(column\_name) **FROM** table\_name;

*V. INSERT – add a new row to a table*

**INSERT INTO** *TableName* (column1, column2) **VALUES** (value1,value2);

**Example:**

· **INSERT INTO** *YCStudent* (FirstName, LastName, GPA, Class, BannerID)

**VALUES** (‘Ploni’,’Almoni’,4.0, ‘Senior’,800012345);

**Comments:**

Remember that there can be constraints on what values someone can use in a given column. For example, the

primary key must be unique and not null, strings (a.k.a. varchar) can’t be too long, and decimal numbers can’t

have more digits on either side of the decimal point.

*VI. UPDATE – change values in existing rows*

**Examples:**

· In the row where BannerID is 800012345, set the GPA to 3.0 and class to super senior:

**UPDATE** YCStudent **SET** GPA=3.0,Class=‘Super Senior’ **WHERE**

BannerID=800012345;

· Set the GPA and class of every row (updates are applied to every row when there is now “where”

condition in the query): **UPDATE** YCStudent **SET** GPA=3.0,Class=‘Super Senior’;

*VI. DELETE – remove rows from the database*

**Example:**

· Delete rows that match a condition: **DELETE FROM** YCStudent **WHERE** Class=‘Super

Senior’ **AND** GPA < 3.0;

· Delete all rows: **DELETE \* FROM** YCStudent;





4

Description of System Behavior

\1. **SQL Queries:** Support the SQL subset described in “SQL Subset You Are Required to Support”

**2. Logging and Data Backup:**

\1. Queries that result in modifications to the DB (everything other than SELECT) are logged to a

modification log file, with a timestamp for each query

\2. The entire DB (all tables) must be saved to disk after 5 rows are affected by modifications (Insert,

Update, Delete). The persistent form must include a timestamp that indicates when it was created.

\1. This means you need to keep a running count of how many rows are affected by modifications

\2. A single query can only result in a single backup. So, even if a query affects 100 rows, you will

only do one backup at the end of the query, not 20 while executing the query.

\3. The saved database file should include:

\1. the text of any CREATEqueries that were used to create the DB and index it

\2. the data. You can save your data as JSON or as comma-separated-values

\3. a timestamp indicating when this backup was started

\4. To save: move your previous backup to a different file name, then write out the new data to the

file that you are using as your current/newest backup

**3. On DB startup:**

\1. Load data from current data backup file

\2. Load modification log file, run any modifications whose timestamp is later than data backup file's

timestamp

\4. **Public API:** your API is made up of ONE method: public ResultSet execute(String SQL). The

result and return value of any query is:

\1. For SELECT, a single table of the values that matched the query

\2. For Insert, Update, and Deleteit is a table with one column and one row, whose value is “true” or

“false”, indicating if the query was run successfully. Success for these queries means that the query did

not refer to any non-existent columns or tables.

\3. For CREATE TABLE, return an empty table with the columns that were just created.

\4. CREATE INDEXcauses the DB to create a B+-Tree index for the given column. The return value is

“true” or “false”, just like Insert, Update, Delete

Tables and Indices

\1. Implement database tables as doubly linked lists, with each element in the list being a row of data

\2. Implement indices as B+-Trees

\3. Primary Key columns must be automatically indexed without a separate CREATE INDEX query being run





5

\4. An index must be kept consistent with what’s in the actual DB table. Therefore, modifications that change any

data in an indexed column must result in both the B+-Tree and the DB table being modified

\5. When executing a query which references an indexed column, you must use the index and not go directly to the

table.

\6. A single value can appear multiple times in a column (e.g. 100 students can have GPA = 4.0). Therefore, the

value pointed to by the index of a B+-Tree entry must be able to point to many rows in the DB table, not just one

Miscellaneous

\1. For SELECTqueries, you don’t have to deal with combinations of the syntax other than those I listed earlier,

but the number of clauses in a compound WHEREcondition, the number of columns selected or ordered by, the

number of tables to be joined, etc. can be arbitrary.

\2. Anywhere in a SELECTthat specific columns are selected in the examples, “\*” can be used instead.

\3. The quality of your main method and/or unit tests will not be graded, but you must include one of those to

demonstrate that your code actually works and covers the various types of queries.

**4. Collaboration: you may NOT work on the logic of the project with other Data Structures students. However,**

**1. You ARE allowed to share test queries on piazza**

**2. You ARE allowed to talk to Operating Systems students, who have a much harder form of this project**

**as their semester assignment.**

A Suggestion on How to Go About This Project

Step 1: Think through, and write down, how you would execute a CREATE query which causes the creation of both the

DB table and any indices specified. Forget about Java code – just think through the logic and write it down in English or

pseudo code.

Step 2: Think through, and write down, how you would execute the other types of queries – SELECT, INSERT, UPDATE,

DELETE. Think through what traversals, changes, etc. each query would cause you to do in the B+-Tree and/or DB table.

Still just English / pseudo code.

Step 3: Design the Java classes/interfaces to implement your thoughts from step 1 and 2.

Step 4: think through, pseudo code, and then Java for logging, persistence, and DB startup.

Step 5: code, test, debug, submit!

Some Additional Useful materials

[Disambiguating](https://piazza.com/class/irdya0zwc9l6se?cid=94)[ ](https://piazza.com/class/irdya0zwc9l6se?cid=94)[Databases](https://piazza.com/class/irdya0zwc9l6se?cid=94)[ ](https://piazza.com/class/irdya0zwc9l6se?cid=94)(Communications of ACM)

Chapter 60 in “Handbook of Data Structures and Applications”, Mehta et. Al.

[The](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[ ](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[Relational](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[ ](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[Data](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[ ](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[Model](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)[ ](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)(Foudnations of CS book)

