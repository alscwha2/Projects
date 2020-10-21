javac JavaFunctional\FileInfoUtility.java
ECHO "********JavaFunctional********"
java -cp JavaFunctional FileInfoUtility %*

javac JavaOO\*.java
ECHO "********JavaOO********"
java -cp JavaOO FileInfoUtility %*

gcc CImperative\FileInfoUtility.c -o CImperative\FileInfoUtility 

ECHO "********CImperative********"
CImperative\FileInfoUtility %*


gcc CFunctional\FileInfoUtility.c -o CFunctional\FileInfoUtility 
ECHO "********CFunctional********"
CFunctional\FileInfoUtility %*

ECHO "********PythonOO********"
PythonOO\FileInfoUtility.py %*

ECHO "********PythonFunctional********"
PythonFunctional\FileInfoUtility.py %*

ECHO "********JSFunctional********"
node JSFunctional\FileInfoUtility.js  %*