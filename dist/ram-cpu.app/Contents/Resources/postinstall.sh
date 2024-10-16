#!/bin/bash

# plist dosyasını doğru yere kopyalayın
cp /Applications/Ram-Cpu.app/Contents/Resources/com.cybersurgeon.ram-cpu.plist ~/Library/LaunchAgents/

# Launch Agent'ı yükleyin ve başlatın
launchctl load ~/Library/LaunchAgents/com.cybersurgeon.ram-cpu.plist
launchctl start com.cybersurgeon.ram-cpu

exit 0
