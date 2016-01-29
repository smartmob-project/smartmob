# -*- coding: utf-8 -*-

import unittest.mock
import pytest

from smartmob import main, version

@unittest.mock.patch('sys.argv', ['smartmob', '--version'])
def test_main_sys_argv(capsys):
    with pytest.raises(SystemExit) as error:
        main()
    assert error.value.args[0] == 0
    stdout, _ = capsys.readouterr()
    assert stdout.strip() == version

def test_main_explicit_args(capsys):
    with pytest.raises(SystemExit) as error:
        main(['--version'])
    assert error.value.args[0] == 0
    stdout, _ = capsys.readouterr()
    assert stdout.strip() == version
