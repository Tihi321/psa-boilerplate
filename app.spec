# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# Frontend dist directory (after building)
frontend_dist = os.path.join('frontend', 'dist')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        (frontend_dist, os.path.join('frontend', 'dist')),
    ],
    hiddenimports=[
        'webview',
        'socketio',
        'eventlet.hubs.epolls',
        'eventlet.hubs.kqueue',
        'eventlet.hubs.selects',
        'eventlet.wsgi',
        'eventlet.greenio',
        'eventlet.support',
        'eventlet.corolocal',
        'eventlet.green.BaseHTTPServer',
        'eventlet.green.socket',
        'dns', 
        'dns.dnssec',
        'dns.e164',
        'dns.hash',
        'dns.namedict',
        'dns.tsigkeyring',
        'dns.update',
        'dns.version',
        'dns.versioned',
        'dns.asyncresolver',
        'dns.asyncquery',
        'dns.zone'
        ],
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
    name='PSAApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
