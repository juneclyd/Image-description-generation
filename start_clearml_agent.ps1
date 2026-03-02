<#
Simple PowerShell helper to install dependencies and start ClearML Agent on Windows.
Run in project root with administrator or appropriate execution policy.
#>

python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Убедитесь, что вы настроили clearml.conf в домашней папке или задали переменные окружения с ключами."
Write-Host "Запускаю clearml-agent daemon (очистите очередь в конфиге при необходимости)..."

clearml-agent daemon --queue default
