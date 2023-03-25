import pytest
from pytest_mock import MockerFixture
from src import bot
from telegram import Update, Message, Chat
from datetime import datetime

def test_clear(mocker: MockerFixture) -> None:
    # arrange
    chat=Chat(0, 'private')
    mock_update = Update(0, message=Message(0, text="/clear", chat=chat, date=datetime.now()))
    bot.shopping_lists = {0: ['birra ', 'biscotti ', 'pomodori ', 'formaggio ']}
    mocker.patch.object(mock_update.message, 'reply_text', return_value=None)
    spy = mocker.spy(mock_update.message, 'reply_text')
    
    # act
    bot.clear(mock_update, None)

    # assert
    assert bot.shopping_lists == {0: []}
    assert spy.call_count == 1
    assert spy.spy_return == None