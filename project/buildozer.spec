[app]

# Titel deiner Anwendung
title = EvergreenMeadows

# Paketname
package.name = EvergreenMeadows-demo

# Domain des Paketnamens
package.domain = org.example

# Version deiner Anwendung
version = 1.0

# Verzeichnis, in dem sich deine Quelldateien befinden
source.dir = .

# Dateierweiterungen, die in die Anwendung aufgenommen werden sollen
source.include_exts = py,png,mp3,ttf

# Muster, um den Grafikordner einzubetten
source.include_patterns = ../graphics/*.*, ../Audio/*.*, ../projects/*.*

# Python-Bibliotheken, die deine Anwendung benötigt
requirements = python3,pygame,random,sys,os

[buildozer]

# Protokolllevel für Buildozer
log_level = 2

# Warnung anzeigen, wenn Buildozer als Root ausgeführt wird
warn_on_root = 1

# Plattformspezifische Einstellungen für Android
[android]
# Indikation, ob die Anwendung im Vollbildmodus sein soll oder nicht
fullscreen = 1

# Liste der Architekturen für Android
archs = armeabi-v7a,arm64-v8a

# Berechtigungen für die Anwendung
#android.permissions = INTERNET

# Android API-Ziel
api = 31

# Mindest-API für APK / AAB-Unterstützung
minapi = 21