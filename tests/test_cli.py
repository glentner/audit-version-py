# SPDX-FileCopyrightText: 2022 Geoffrey Lentner
# SPDX-License-Identifier: Apache-2.0

"""Unit tests for command-line interface."""


# type annotations
from __future__ import annotations

# external libs
from pytest import mark, CaptureFixture

# internal libs
from audit_version import AuditVersionApp, __version__


@mark.unit
class TestAuditVersionApp:
    """Unit tests for basic command-line interface."""

    @mark.parametrize('flag', ['-h', '--help'])
    def test_help(self: TestAuditVersionApp, capsys: CaptureFixture, flag: str) -> None:
        """Print help statement when -h/--help is given."""
        AuditVersionApp.main([flag, ])
        out, err = capsys.readouterr()
        assert out.strip() == AuditVersionApp.interface.help_text.strip()
        assert err == ''

    @mark.parametrize('flag', ['-v', '--version'])
    def test_version(self: TestAuditVersionApp, capsys: CaptureFixture, flag: str) -> None:
        """Print help statement when -h/--help is given."""
        AuditVersionApp.main([flag, ])
        out, err = capsys.readouterr()
        assert out.strip() == __version__
        assert err == ''
