#
#  --------------------------------------------------------------------------
#   Gurux Ltd
#
#
#
#  Filename: $HeadURL$
#
#  Version: $Revision$,
#                $Date$
#                $Author$
#
#  Copyright (c) Gurux Ltd
#
# ---------------------------------------------------------------------------
#
#   DESCRIPTION
#
#  This file is a part of Gurux Device Framework.
#
#  Gurux Device Framework is Open Source software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; version 2 of the License.
#  Gurux Device Framework is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#  See the GNU General Public License for more details.
#
#  More information of Gurux products: http://www.gurux.org
#
#  This code is licensed under the GNU General Public License v2.
#  Full text may be retrieved at http://www.gnu.org/licenses/gpl-2.0.txt
# ---------------------------------------------------------------------------
from pathlib import Path
import os
import subprocess
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

class build_py_with_mo(_build_py):
    def run(self):
        # Convert .po to .mo
        for dirpath, dirnames, filenames in os.walk('my_package/locale'):
            for filename in filenames:
                if filename.endswith('.po'):
                    po_path = os.path.join(dirpath, filename)
                    mo_path = po_path[:-3] + '.mo'
                    subprocess.run(['msgfmt', po_path, '-o', mo_path], check=True)
        super().run()

setup(
    name="gurux_net",
    version="1.0.23",
    author="Gurux Ltd",
    author_email="gurux@gurux.fi",
    description="Gurux network media is used to commmunication with TCP/IP or UDP connections.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gurux/gurux.net.python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    package_data={
        "gurux_net": ["locale/*/LC_MESSAGES/*.mo"],
    },
    cmdclass={
        'build_py': build_py_with_mo
    },
    install_requires=['gurux-common'],
)
