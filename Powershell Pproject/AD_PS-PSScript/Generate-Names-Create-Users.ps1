
function generate-random-name {
    $consonants = @('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')
    $vowels = @('a', 'e', 'i', 'o', 'u', 'y')
    $nameLength = Get-Random -Minimum 3 -Maximum 7
    $count = 0
    $name = ""
    while ($count -lt $nameLength) {
        if ($($count % 2) -eq 0) {
            $name += $consonants[$(Get-Random -Minimum 0 -Maximum ($consonants.Count - 1))]
        } else {
            $name += $vowels[$(Get-Random -Minimum 0 -Maximum ($vowels.Count - 1))]
        }
        $count++
    }
    return $name
}


$names = @()
for ($i = 1; $i -le 100; $i++) {
    $firstName = generate-random-name
    $lastName = generate-random-name
    $fullName = "$firstName $lastName"
    $names += $fullName
}


$names | ForEach-Object { Write-Host $_ }
