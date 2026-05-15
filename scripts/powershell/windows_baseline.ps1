param (
    [Parameter(Mandatory=$false)]
    [string]$VMName = $env:COMPUTERNAME
)

$TranscriptPath = "C:\Logs\WindowsBaseline_$($VMName)_$(Get-Date -Format 'yyyyMMdd_HHmmss').log"
if (!(Test-Path "C:\Logs")) { New-Item -ItemType Directory -Path "C:\Logs" | Out-Null }
Start-Transcript -Path $TranscriptPath -Append

Write-Output "Starting Windows Baseline for $VMName"

try {
    # 1. Set Timezone
    Write-Output "Setting Timezone to UTC..."
    Set-TimeZone -Id "UTC" -ErrorAction Stop

    # 2. Disable IE Enhanced Security Configuration
    Write-Output "Disabling IE ESC..."
    $AdminKey = "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components\{A509B1A7-37EF-4b3f-8CFC-4F3A74704073}"
    $UserKey = "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components\{A509B1A8-37EF-4b3f-8CFC-4F3A74704073}"
    Set-ItemProperty -Path $AdminKey -Name "IsInstalled" -Value 0 -ErrorAction SilentlyContinue
    Set-ItemProperty -Path $UserKey -Name "IsInstalled" -Value 0 -ErrorAction SilentlyContinue

    # 3. Configure Windows Defender Basic Settings
    Write-Output "Configuring Windows Defender..."
    Set-MpPreference -DisableRealtimeMonitoring $false -ErrorAction Stop
    Set-MpPreference -MAPSReporting Advanced -ErrorAction Stop

    # 4. Enable Remote Desktop
    Write-Output "Enabling Remote Desktop..."
    Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server" -Name "fDenyTSConnections" -Value 0 -ErrorAction Stop
    Enable-NetFirewallRule -DisplayGroup "Remote Desktop" -ErrorAction Stop

    Write-Output "Windows Baseline Configuration Completed Successfully."
} catch {
    Write-Error "An error occurred during the baseline configuration: $_"
    Stop-Transcript
    exit 1
}

Stop-Transcript
