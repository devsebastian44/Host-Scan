# =============================================================================
# scripts/publish.ps1 - Generic Publication Script
# Sanitized Sync: main -> public (GitHub)
# =============================================================================

Write-Host "[*] Iniciando proceso de publicación de Host-Scan..." -ForegroundColor Cyan

# 1. Validaciones Iniciales
$currentBranch = git rev-parse --abbrev-ref HEAD
if ($currentBranch -ne "main") {
    Write-Host "[!] Error: Debes estar en 'main' para publicar." -ForegroundColor Red
    exit
}

if (git status --porcelain) {
    Write-Host "[!] Tienes cambios sin guardar. Haz commit antes de publicar." -ForegroundColor Yellow
    exit
}

# 2. Limpieza Local Previa
Write-Host "[*] Limpiando archivos temporales y logs..." -ForegroundColor Yellow
Remove-Item -Path "*.log", "*.rules", "iptables_backup_*" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "__pycache__", ".pytest_cache" -Recurse -Force -ErrorAction SilentlyContinue

# 3. Sincronización con Remoto Principal (GitHub)
Write-Host "[*] Asegurando estado en GitHub (origin)..."
git pull origin main --rebase
git push origin main

# 4. Estrategia de Rama Pública (Aislamiento de Seguridad)
Write-Host "[*] Creando release sanitizado en rama 'public'..."
git checkout -B public main

# 5. Filtrado de Archivos (Lo que NO va a la versión pública)
Write-Host "[*] Aplicando filtros de seguridad..." -ForegroundColor Cyan
# Eliminamos lo que se considere interno o de desarrollo
git rm -r --cached tests/ -f 2>$null
git rm --cached configs/requirements-dev.txt -f 2>$null
git rm -r --cached scripts/ -f 2>$null

# 6. Commit de Lanzamiento y Push
git commit -m "docs: release update to public portfolio (sanitized)" --allow-empty
Write-Host "[*] Actualizando rama pública en GitHub..." -ForegroundColor Green
git push origin public:main --force

# 7. Retorno Seguro al Entorno de Trabajo
Write-Host "[*] Volviendo a la rama principal (main)..."
git checkout main -f
git clean -fd 2>$null

Write-Host "[*] Publicación completada con éxito" -ForegroundColor Green