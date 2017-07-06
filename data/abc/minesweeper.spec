# -*- mode: python -*-

block_cipher = None


a = Analysis(['..\\..\\..\\Downloads\\python-tkinter-minesweeper-master\\python-tkinter-minesweeper-master\\minesweeper.py'],
             pathex=['C:\\Users\\\xc1\xd6\xce\xa1\\DOWNLO~1\\PYTHON~2\\PYTHON~1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='minesweeper',
          debug=False,
          strip=False,
          upx=True,
          console=False )
