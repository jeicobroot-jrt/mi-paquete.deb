#!/data/data/com.termux/files/usr/bin/bash

echo "Configurando el repositorio de JEICOB_ROOT..."

# 1. Crear el archivo de lista para el repo
# CAMBIA 'tu-usuario' por tu nombre de usuario real de GitHub
# CAMBIA 'nombre-repo' por el nombre que le pusiste al repo
REPO_URL="https://tu-usuario.github.io/nombre-repo"

echo "deb [trusted=yes] $REPO_URL ./" > $PREFIX/etc/apt/sources.list.d/packit.list

# 2. Actualizar e instalar
pkg update
pkg install mi-herramienta -y

echo "¡Instalación completada! Escribe 'packit' para empezar."

