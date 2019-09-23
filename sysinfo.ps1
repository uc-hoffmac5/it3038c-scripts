function getIP { (get-netipaddress).ipv4address | select-string "192.*" }
$IP = getIP
Write-host("This machine's IP address is $IP")
Write-host("This machine's IP address is {0}"-f $IP)