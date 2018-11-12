# grades updater
A program which can search and update the content of the TAB file generated by the grade book in CCLE of UCLA grading system

How to use it 

step0 install python 3.7
step1 run gradesupdater.py in command prompt
step2 enter part of UID or student name, the feedback is all record containing input 
step3 if the feed back is one record, the next input is assumed to be grades
step4 repeat step 3 until all record is updated. Clode command prompt. upload the TAB file to gradebook of ucla

More about program:
1 input is not case sensive
2 wrong input in step 2 or 3 will let the status of program go back to step2
3 input with less than three digits or equal to 100 will be identify as grade, input will be identified as UID or name otherwise.
4 the TAB is modified instantly after a correct input.

Example

&gt;&gt;405

123456789  Kahler，Jack 0

123456799  Kobayashi，Mary 0

Too many records. Please try a more detailed input

&gt;&gt;Kahler

123456789  Kahler，Jack 0

One record is found. Please enter grade

&gt;&gt;10

Record updated

123456789  Kahler，Jack 10

Please input part of UID or name

&gt;&gt;Kahler

123456789  Kahler，Jack 0

One record is found. Please enter grade

&gt;&gt;Kobayashi

Wrong input

Please input part of UID or name