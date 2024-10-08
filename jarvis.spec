import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

a = Analysis(['jarvis.py'],
             pathex=['/path/to/your/project'],
             binaries=[],
             datas=[('Automation', 'Automation'),
                    ('Brain', 'Brain'),
                    ('Data', 'Data'),
                    ('Features', 'Features'),
                    ('NetHyTechSTT', 'NetHyTechSTT'),
                    ('TextToSpeech', 'TextToSpeech'),
                    ('Time_Operations', 'Time_Operations'),
                    ('Vision', 'Vision'),
                    ('Alam_data.txt', '.'),
                    ('Alert.py', '.'),
                    ('chat_hystory.txt', '.'),
                    ('chromedriver.exe', '.'),
                    ('co_brain.py', '.'),
                    ('demo.py', '.'),
                    ('explain.drawio', '.'),
                    ('explain1.drawio', '.'),
                    ('greetingtext.py', '.'),
                    ('history.txt', '.'),
                    ('input.txt', '.'),
                    ('internet_check.py', '.'),
                    ('jarvis.py', '.'),
                    ('logo.png', '.'),
                    ('MAKE_req.py', '.'),
                    ('Matthew.mp3', '.'),
                    ('README.md', '.'),
                    ('requirements.txt', '.'),
                    ('schedule.txt', '.'),
                    ('setup.py', '.'),
                    ('text.py', '.')], # Include all required files
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='YourAppName',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          version='',
          icon='',
          specpath=None,
          console=True)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               runtime_tmpdir=None,
               excludes=None,
               cipher=block_cipher,
               noarchive=False,
               )