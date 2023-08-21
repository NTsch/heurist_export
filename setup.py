from cx_Freeze import setup, Executable

includefiles = ['main_flask.py']

setup(
 name='Heurist 2 Ediarum',
 version = '0.1',
 description = 'Heurist 2 Ediarum',
 options = {'build_exe':   {'include_files':includefiles}},
 executables = [Executable('main_flask.py')]
)