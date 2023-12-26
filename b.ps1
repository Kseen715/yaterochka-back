# Usually this is the version
$tag = "1.0.2"

# Name of the image
# in format "<dockerhub-account-name>/<imange-name>"
# or "ghcr.io/<github-account-name>/<imange-name>" 
# (if you want to push to GitHub Container Registry
# instead of Docker Hub)
$name = "kseen/yaterochka-back"

# Build and push as tagged & latest images
# Then clear dangling images
(Write-Host 'Starting script...' -ForegroundColor Cyan) && (docker build -t ${name} -t ${name}:${tag} . || Write-Error 'Build error.') && (docker push ${name}:${tag} || Write-Error 'Tag push error.') && (docker push ${name} || Write-Error 'Latest tag push error.') && (docker rmi ${name}:${tag} || Write-Error 'Deleting local tagged image error.') && (Write-Host 'Success!' -ForegroundColor Green) && (Write-Host 'Deleting dangling images...' -ForegroundColor Cyan) && (docker image prune -f || Write-Error 'Error in pruning.') && (Write-Host 'Dangling images deleted.' -ForegroundColor Green) && (Write-Host 'Script finished.' -ForegroundColor Cyan)