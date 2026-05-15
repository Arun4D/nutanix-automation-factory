param(
    [Parameter(Mandatory=$false)]
    [int]$MaxSignatureAgeDays = 1
)

$ErrorActionPreference = "Stop"

try {
    Write-Output "Starting Defender Validation..."

    # Get current Defender definitions info
    $DefenderInfo = Get-MpComputerStatus

    $SignatureAge = (Get-Date) - $DefenderInfo.AntivirusSignatureLastUpdated

    Write-Output "Antivirus Signature Last Updated: $($DefenderInfo.AntivirusSignatureLastUpdated)"
    Write-Output "Antivirus Signature Age (Days): $($SignatureAge.Days)"

    if ($SignatureAge.Days -gt $MaxSignatureAgeDays) {
        Write-Output "WARNING: Defender signatures are older than $MaxSignatureAgeDays days."
        Write-Output "Attempting to force an update..."
        
        Update-MpSignature
        
        # Re-check
        $DefenderInfo = Get-MpComputerStatus
        $NewAge = (Get-Date) - $DefenderInfo.AntivirusSignatureLastUpdated
        if ($NewAge.Days -gt $MaxSignatureAgeDays) {
            Write-Output "FAIL: Defender signatures still out of date after forced update."
            exit 1
        } else {
            Write-Output "SUCCESS: Defender signatures updated successfully."
        }
    } else {
        Write-Output "SUCCESS: Defender signatures are compliant."
    }

    # Ensure Real-Time Protection is ON
    if ($DefenderInfo.RealTimeProtectionEnabled -eq $false) {
        Write-Output "FAIL: Real-Time Protection is DISABLED. Compliance violation."
        exit 1
    } else {
        Write-Output "SUCCESS: Real-Time Protection is Enabled."
    }
} catch {
    Write-Error "A fatal error occurred during Defender validation: $_"
    exit 1
}
