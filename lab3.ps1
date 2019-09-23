function getIP { (get-netipaddress).ipv4address | select-string "192.*" }
$IP = getIP
$Username= $env:Username
$Hosnamet= $env:COMPUTERNAME
$Version=$host.version
$date=Get-Date
$body=("This machine's IP is $IP. User is $Username. Hostname is $Hosnamet. Powershell version is $Version.
Today's date is $date.")

Send-MailMessage -To "hoffmac5@mail.uc.edu" -From "choffman0918@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $body -smtpserver smtp.gmail.com -port 587 -UseSSL -Credential(Get-Credential)