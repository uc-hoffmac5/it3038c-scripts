$path = Read-Host -Prompt 'Input the directory you want to clean up'
"`n"
$Recurse
While(($Recurse = Read-Host -Prompt "Would you like the deleteion to affect any subdirectories? Type Y for yes and N for no" ) -ne "Y" -and $Recurse -ne "N" )
{
"`n"
Write-Output 'Whatever you just entered was not one of the two options. Read carefully and try again bud.'
"`n"
}
if($Recurse -eq 'Y')
{
$currentDate = Get-Date
[int]$numberOfDays = Read-Host -Prompt 'Input how far back you want to keep your files in days'
"`n"
if($numberOfDays -lt 0) 
    {
    Write-Output 'Ok well you just entered a negative number which means everything is gonna be deleted so I hope you meant to do that'
    "`n"
    }
$dateToDelete = $currentDate.AddDays(-$numberOfDays)
$input
While(($input = Read-Host -Prompt "This Will delete all files that havent been written to since $dateToDelete in the directory $path is that ok? Type Y for yes and N for no" ) -ne "Y" -and $input -ne "N" )
{
"`n"
Write-Output 'Whatever you just entered was not one of the two options. Read carefully and try again bud.'
"`n"
}
if($input -eq 'Y')
{
    Get-ChildItem $path -Recurse| where {$_.LastWriteTime -lt $dateToDelete} | Write-Output
    "`n"
    $input2
    While(($input2 = Read-Host -Prompt "These are the files that are about to be gone forever are you sure you want to get rid of these? Type Y for yes and N for no." ) -ne "Y" -and $input2 -ne "N" )
    {
    "`n"
    Write-Output 'Whatever you just entered was not one of the two options. Read carefully and try again bud.'
        "`n"
    }
    
    if($input2 -eq 'Y')
        {
         Get-ChildItem $path -Recurse | where {$_.LastWriteTime -lt $dateToDelete} | Remove-Item
         "`n"
         Write-Output 'The files have been deleted'
         Start-Sleep -s 5
        }
    elseif($input2 -eq 'N')
        {
        "`n"
        Write-Output 'That was a close one then. Run this again once you move the files or whatever'
        Start-Sleep -s 5
}
}

elseif($input -eq 'N')
{
"`n"
Write-Output 'Alright then, try inputting the right path/date next time'
Start-Sleep -s 5
}
}
Elseif($Recurse -eq 'N')
{
$currentDate = Get-Date
[int]$numberOfDays = Read-Host -Prompt 'Input how far back you want to keep your files in days'
"`n"
if($numberOfDays -lt 0) 
    {
    Write-Output 'Ok well you just entered a negative number which means everything is gonna be deleted so I hope you meant to do that'
    "`n"
    }
$dateToDelete = $currentDate.AddDays(-$numberOfDays)
$input
While(($input = Read-Host -Prompt "This Will delete all files that havent been written to since $dateToDelete in the directory $path is that ok? Type Y for yes and N for no" ) -ne "Y" -and $input -ne "N" )
{
"`n"
Write-Output 'Whatever you just entered was not one of the two options. Read carefully and try again bud.'
"`n"
}
if($input -eq 'Y')
{
    Get-ChildItem $path | where {$_.LastWriteTime -lt $dateToDelete} | Write-Output
    "`n"
    $input2
    While(($input2 = Read-Host -Prompt "These are the files that are about to be gone forever are you sure you want to get rid of these? Type Y for yes and N for no." ) -ne "Y" -and $input2 -ne "N" )
    {
    "`n"
    Write-Output 'Whatever you just entered was not one of the two options. Read carefully and try again bud.'
        "`n"
    }
    
    if($input2 -eq 'Y')
        {
         Get-ChildItem $path | where {$_.LastWriteTime -lt $dateToDelete} | Remove-Item
         "`n"
         Write-Output 'The files have been deleted'
         Start-Sleep -s 5
        }
    elseif($input2 -eq 'N')
        {
        "`n"
        Write-Output 'That was a close one then. Run this again once you move the files or whatever'
        Start-Sleep -s 5
}
}

elseif($input -eq 'N')
{
"`n"
Write-Output 'Alright then, try inputting the right path/date next time'
Start-Sleep -s 5
}
}