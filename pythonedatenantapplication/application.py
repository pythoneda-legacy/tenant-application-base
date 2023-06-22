#!/usr/bin/env python3
"""
pythonedatenantapplication/application.py

This file provides a way to run Tenant-enabled PythonEDA applications.

Copyright (C) 2023-today rydnr's pythoneda-tenant-application/base

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythonedaapplication.pythoneda import PythonEDA

import asyncio

class TenantApplication(PythonEDA):
    """
    Runs PythonEDA Application with Tenant support enabled.

    Class name: TenantApplication

    Responsibilities:
        - Runs a PythonEDA with tenant support enabled.

    Collaborators:
        - Command-line handlers from pythoneda-tenant-infrastructure/base
    """
    def __init__(self):
        """
        Creates a new TenantApplication instance.
        """
        super().__init__(__file__)

if __name__ == "__main__":

    asyncio.run(TenantApplication.main())
