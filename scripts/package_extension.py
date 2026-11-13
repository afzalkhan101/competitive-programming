#!/usr/bin/env python3
"""Package the dependency-free local VS Code extension as VSIX."""
from pathlib import Path
import zipfile
import json
ROOT = Path(__file__).resolve().parent.parent
version = json.loads((ROOT/'vscode-practice/package.json').read_text())['version']
output = ROOT / f'build/codeforces-practice-{version}.vsix'
output.parent.mkdir(exist_ok=True)
manifest = '''<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011"><Metadata><Identity Language="en-US" Id="codeforces-practice" Version="1.0.0" Publisher="local"/><DisplayName>Your Practice Path</DisplayName><Description xml:space="preserve">Local 500-problem Codeforces practice dashboard</Description><Tags>education,codeforces</Tags><Categories>Education</Categories><GalleryFlags>Public</GalleryFlags><Properties><Property Id="Microsoft.VisualStudio.Code.Engine" Value="^1.85.0"/><Property Id="Microsoft.VisualStudio.Code.ExtensionDependencies" Value=""/><Property Id="Microsoft.VisualStudio.Code.ExtensionPack" Value=""/></Properties></Metadata><Installation><InstallationTarget Id="Microsoft.VisualStudio.Code"/></Installation><Dependencies/><Assets><Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true"/></Assets></PackageManifest>'''
manifest = manifest.replace('Version="1.0.0"', f'Version="{version}"')
content = '''<?xml version="1.0" encoding="utf-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="json" ContentType="application/json"/><Default Extension="js" ContentType="application/javascript"/><Default Extension="css" ContentType="text/css"/><Default Extension="md" ContentType="text/markdown"/><Default Extension="vsixmanifest" ContentType="text/xml"/></Types>'''
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as archive:
    archive.writestr('extension.vsixmanifest',manifest)
    archive.writestr('[Content_Types].xml',content)
    for file in (ROOT/'vscode-practice').rglob('*'):
        if file.is_file(): archive.write(file, 'extension/'+str(file.relative_to(ROOT/'vscode-practice')))
print(output)
