# Path to the Notepad file containing the usernames #
$userList = Get-Content -Path ".\names.txt"

# Loop through each username and disable the account #
foreach ($n in $userList) {
    $first = $n.Split(" ")[0].ToLower()
    $last = $n.Split(" ")[1].ToLower()
    $username = "$($first.Substring(0,1))$($last)".ToLower()
    Disable-ADAccount -Identity $username
    Write-Host "Deactivated user: $username"
}

Write-Host "All specified users have been deactivated."
