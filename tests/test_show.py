import pytest
from pytest_mock import MockerFixture
from src import bot
from telegram import Update, Message, Chat
from datetime import datetime

def test_show(mocker: MockerFixture) -> None:
    # arrange
    chat=Chat(0, 'private')
    mock_update = Update(0, message=Message(0, text="/show", chat=chat, date=datetime.now()))
    bot.shopping_lists = {0: ['pasta ', 'latte ', 'fagioli ', 'burro ']}
    mocker.patch.object(mock_update.message, 'reply_text', return_value='Lista:\n- '+'\n- '.join(bot.shopping_lists[0]))
    spy = mocker.spy(mock_update.message, 'reply_text')
    
    # act
    bot.show(mock_update, None)

    # assert
    assert spy.call_count == 1
    assert spy.spy_return == 'Lista:\n- '+'\n- '.join(bot.shopping_lists[0])