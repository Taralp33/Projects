# Path to the Notepad file containing the usernames
$userList = Get-Content -Path ".\names.txt"

# Loop through each username and enable the account
foreach ($n in $userList) {
    $first = $n.Split(" ")[0].ToLower()
    $last = $n.Split(" ")[1].ToLower()
    $username = "$($first.Substring(0,1))$($last)".ToLower()
    Enable-ADAccount -Identity $username
    Write-Host "Activated user: $username"
}

Write-Host "All specified users have been activated."
