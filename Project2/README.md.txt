The goal of this script is to delete any files that havent been written to in a certain timeframe. 
The script can be run just like any other powershell script. 
First the user is prompted for a directory. 
They are then asked if they want the deletion to affect any subdirectories or not. 
Then they are prompted for a number of days back that files should be kept. 
If the user enters a negative number they are warned that they have chosen a future date, meaning the entire directory will be deleted. 
The directory and delteion date are printed and the user is prompted for confirmation. 
They are then shown every file that will be delteted and are given one more chance to back out. 
Any time at which the user enters N for no the script closes. 
If they do not enter Y or N the script will prompt them again untill they choose Y or N.
In the future I wnat to make the script be able to perform the operation on remote computers and clean up some of the scripting.