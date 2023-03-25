import pytest
from pytest_mock import MockerFixture
from src.bot import unknown
from telegram import Update, Message, Chat
from datetime import datetime

def test_unknown(mocker: MockerFixture) -> None:
    # arrange
    chat=Chat(0, 'private')
    mock_update = Update(0, message=Message(0, text="*", chat=chat, date=datetime.now()))
    mocker.patch.object(mock_update.message, 'reply_text', return_value=None)
    spy = mocker.spy(mock_update.message, 'reply_text')
    
    # act
    unknown(mock_update, None)

    # assert
    assert spy.call_count == 1
    assert spy.spy_return == None