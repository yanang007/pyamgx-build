import os
from pathlib import Path

import nox


@nox.session
def rename_wheels(session: nox.Session) -> None:
    session.chdir('..')  # cd to root directory

    extra_tags = []

    cuda_ver = session.env.get('CUDA_VERSION', None)
    if cuda_ver is not None:
        extra_tags.append(f'cu{cuda_ver}')

    if len(extra_tags) == 0:
        return

    pkg_name = 'pyamgx'
    new_pkg_name = '-'.join([pkg_name, *extra_tags])

    path_to_wheels = Path(session.env.get('PYAMGX_DIR', 'pyamgx')).resolve() / 'dist'

    for filename in path_to_wheels.iterdir():
        new_filename = filename.with_stem(filename.stem.replace(pkg_name, new_pkg_name))
        os.rename(filename, new_filename)
