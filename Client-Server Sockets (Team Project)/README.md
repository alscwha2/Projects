# Functionality
* You will write a simple Java client-server pair of programs
* Your client and server must:
	* each be started in their own Thread
	* be defined in separate classes
	* communicate with each other via Sockets
* The client can make 3 different requests:
	* “GET 3-letter-major-code” – server must return the CRN and titles of all the courses in the given major for Fall 2017 in Y.C.
	* “ADD 3-letter-major-code CRN course-title” – add the given course to the server’s data
	* “DELETE CRN” – delete the given CRN from the server’s data
* You must initialize your server with all the COM, MAT, and BIO courses
# Persistence
Server must load course data from a file on startup.
* File format must be either a Java properties file or JSON (must use GSON for JSON)
* Path to data file must be a command line parameter
* Server must write out a new, numbered version of the file after every client-initiated ADD or DELETE operation
# Build & Test
* Your project must have a Maven build file
* You MUST include a set of JUnit tests that demonstrates that all the above works correctly
* The tests must fail if a feature is broken and provide a clear error message describing what is broken
# Must Work As-Is
* You must check the project in to your private Git repo that I created for you (use the same one as last year)
* Your project must work as-is without me changing ANYTHING
	* I should be able to simply type mvn test in the command prompt and it should compile and run the Junit tests that demonstrate that it works
	* If this is not the case, you immediately lost 50% of the grade on this homework
	* Test for this before submitting!
