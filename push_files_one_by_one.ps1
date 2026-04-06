# Get the list of modified and untracked files
$items = git status --porcelain

foreach ($line in $items) {
    if ($line.Trim() -eq "") { continue }
    
    # Extract status (first two characters) and file path (from 3rd character onwards)
    $status = $line.Substring(0, 2)
    $file = $line.Substring(3).Replace('"', '').Trim() # remove quotes if any
    
    # Determine the commit message based on the status
    if ($status.Contains("??")) {
        $msg = "Add $file"
    } else {
        $msg = "Update $file"
    }
    
    Write-Host "Processing file: $file with message: $msg"
    
    # Stage the file
    git add "$file"
    
    # Commit with the specific message
    git commit -m "$msg"
    
    # Push to origin main (quietly to avoid long output logs)
    git push origin main --quiet
    
    # Brief pause to be respectful to the server/API
    Start-Sleep -Seconds 1
}
