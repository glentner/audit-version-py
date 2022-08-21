# SPDX-FileCopyrightText: 2022 Geoffrey Lentner
# SPDX-License-Identifier: Apache-2.0

"""Unit tests for auto-version."""


# internal libs
from auto_version import __version__


def test_version():
    assert __version__ == '0.1.0'
