# Project Description
## RESTful APIs for a University Registrar
![ER Diagram of Registration System](https://github.com/alscwha2/Projects/blob/master/Images/RestfulAPIImage.jpg?raw=true)
## Required for Each Function
1. URIs, including parameters
2. HTTP requests and response headers
	1. You only need to include those headers that appear in these lecture slides, not all headers
3. Payloads wherever the entire message is not contained in the URI and HTTP headers
	1. Use JSON for payloads
## List of Functions for Professors
* Professors and deans can Create Read Update Delete
	* Majors
	* Courses
		* Prerequisites
		* Title
		* Credits
		* Description
	* Classes (i.e. “instances” of a course).
		* Semester, time, day, location, professor, maximum number of students
	* Everyone can read all the above
* Professors give students grades
## List of Functions: Advisors, Students
* Academic advisors approve students’ schedules
	* Students must be cleared to register before doing so
* Students register for class offerings
	* IFF they have the prerequisites and academic advisor approval
	* IFF there are open spots in the class
* All non-student users, and the student himself, can view a student’s past and current courses, including grades
* Department chairs and deans can view
performance statistics on professors, specifically:
1. Grades students get in their various classes / semesters
	* Aggregates
	* Mode, Median
2. How do students who take class X with a given professor perform subsequently
	* E.g. 75% of those who take COM 9999 with Professor X get a B+ when they take COM 8888 with professor Y
