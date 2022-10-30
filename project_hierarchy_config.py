#!/usr/bin/env python
"""
This module is used configurate the hierarchy of the directories of the project so the
scripts inside a specific directory can use the ones located at the parent directory as
packages.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Victor Vinci Fantucci"
__email__ = "victor.v.fantucci@gmail.com"
__date__ = "2022/10/30"
__deprecated__ = False
__license__ = "GPLv3"
__maintainer__ = "VictorFantucci"

import os
import sys

def add_parent_directory_to_path() -> None:
    """
    Function that add the parent directory where the this file is present to sys.path variable.
    """
    # Getting the name of the directory where the this file is present.
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Getting the parent directory name where the current directory is present.
    parent_directory = os.path.dirname(current_directory)

    # Adding the parent directory to the sys.path variable.
    sys.path.append(parent_directory)
