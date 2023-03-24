import pytest
from pytest_mock import MockerFixture
from src.bot import unknown
from telegram import Update, Message
from datetime import datetime

def test_unknown(mocker: MockerFixture) -> None:
    # ARRANGE
    mock_update = Update(0, message=Message(0, text="*", chat=0, date=datetime.now()))
    mocker.patch.object(mock_update.message, 'reply_text', return_value=None)
    spy = mocker.spy(mock_update.message, 'reply_text')
    
    # ACT
    unknown(mock_update, None)

    # ASSERT
    assert spy.call_count == 1
    assert spy.spy_return == None