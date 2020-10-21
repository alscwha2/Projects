javac JavaFunctional\FileInfoUtility.java
ECHO "********JavaFunctional********"
java -cp JavaFunctional FileInfoUtility %* > csv\JavaFunctional.csv

javac JavaOO\*.java
ECHO "********JavaOO********"
java -cp JavaOO FileInfoUtility %* > csv\JavaOO.csv

gcc CImperative\FileInfoUtility.c -o CImperative\FileInfoUtility 

ECHO "********CImperative********"
CImperative\FileInfoUtility %* > csv\CImperative.csv


gcc CFunctional\FileInfoUtility.c -o CFunctional\FileInfoUtility 
ECHO "********CFunctional********"
CFunctional\FileInfoUtility %* > csv\CFunctional.csv

ECHO "********PythonOO********"
PythonOO\FileInfoUtility.py %* > csv\PythonOO.csv

ECHO "********PythonFunctional********"
PythonFunctional\FileInfoUtility.py %* > csv\PythonFunctional.csv

ECHO "********JSFunctional********"
node JSFunctional\FileInfoUtility.js  %* > csv\JSFunctional.csv