# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.pyw'],
    pathex=[],
    binaries=[('./driver/chromedriver.exe', './driver')],
    datas=[('./resources/xiaomi_bubble.mp3', './resources'), ('./resources/betting.ico', './resources'), ('./resources/redmi.mp3', './resources'), ('./resources/miui_12_notification.mp3', './resources')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='FAILFUCK',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='resources\\betting.ico',
)
