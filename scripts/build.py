from pathlib import Path

import nox


@nox.session(python=['3.9'])
def build_bdist(session: nox.Session) -> None:
    session.install('numpy', 'setuptools', 'Cython')

    # expand environment variables
    session.chdir('..')
    session.env['AMGX_DIR'] = Path(session.env.get('AMGX_DIR1', 'AMGX')).absolute().resolve().__str__()
    session.env['AMGX_BUILD_DIR'] = Path(session.env.get('AMGX_BUILD_DIR1', 'build')).absolute().resolve().__str__()

    session.chdir('pyamgx')
    session.run('python', 'setup.py', 'bdist_wheel')
