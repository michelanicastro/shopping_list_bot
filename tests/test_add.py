import pytest
from pytest_mock import MockerFixture
from src import bot
from telegram import Update, Message, Chat
from datetime import datetime


def test_add_empty_args(mocker: MockerFixture) -> None:
    # arrange
    chat=Chat(0, 'private')
    mock_update = Update(0, message=Message(0, text="/add", chat=chat, date=datetime.now()))
    mock_context = mocker.MagicMock()
    mock_context.args = ['']
    mocker.patch.object(mock_update.message, 'reply_text', return_value=None)
    spy = mocker.spy(mock_update.message, 'reply_text')

    # act
    bot.add(mock_update, mock_context)

    # assert
    assert spy.call_count == 1
    assert spy.spy_return == None


def test_add_already_in_list(mocker: MockerFixture) -> None:
    # arrange
    chat=Chat(0, 'private')
    mock_update = Update(0, message=Message(0, text="/add pasta", chat=chat, date=datetime.now()))
    mock_context = mocker.MagicMock()
    mock_context.args = ['pasta']
    bot.shopping_lists = {0: ['pasta ']}
    mocker.patch.object(mock_update.message, 'reply_text', return_value=None)
    spy = mocker.spy(mock_update.message, 'reply_text')

    # act
    bot.add(mock_update, mock_context)

    # assert
    assert bot.shopping_lists == {0: ['pasta ']}
    assert spy.call_count == 1
    assert spy.spy_return == None


def test_add_not_in_list(mocker: MockerFixture) -> None:
    # arrange
    chat=Chat(0, 'private')
    mock_update = Update(0, message=Message(0, text="/add latte", chat=chat, date=datetime.now()))
    mock_context = mocker.MagicMock()
    mock_context.args = ['latte']
    bot.shopping_lists = {0: ['pasta ']}
    mocker.patch.object(mock_update.message, 'reply_text', return_value=None)
    spy = mocker.spy(mock_update.message, 'reply_text')

    # act
    bot.add(mock_update, mock_context)
    
    # assert
    assert bot.shopping_lists == {0: ['pasta ', 'latte ']}
    assert spy.call_count == 1
    assert spy.spy_return == None
