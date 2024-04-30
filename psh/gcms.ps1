function Get-PackageSource {
    param (
        [string[]]$Packages
    )

    (Get-Command $Packages).Source
}

New-Alias -Name gcms -Value Get-CommandSource #alias make; set-alias which where.exe