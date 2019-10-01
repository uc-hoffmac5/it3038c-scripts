$path = Read-Host -Prompt 'Input the directory you want to clean up'
"`n"
$currentDate = Get-Date
[int]$numberOfDays = Read-Host -Prompt 'Input how far back you want to keep your files in days'
"`n"
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
Get-ChildItem $path | where {$_.LastWriteTime -lt $dateToDelete} | Remove-Item
"`n"
Write-Output 'The files have been deleted'
Start-Sleep -s 5
}
elseif($input -eq 'N')
{
"`n"
Write-Output 'Alright then, try inputting the right path/date next time'
Start-Sleep -s 5
}