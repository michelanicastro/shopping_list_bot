import pytest
from pytest_mock import MockerFixture
from src import bot
from telegram import Update, Message, Chat
from datetime import datetime


def test_remove_empty_args(mocker: MockerFixture) -> None:
    # arrange
    chat=Chat(0, 'private')
    mock_update = Update(0, message=Message(0, text="/remove", chat=chat, date=datetime.now()))
    mock_context = mocker.MagicMock()
    mock_context.args = ['']
    mocker.patch.object(mock_update.message, 'reply_text', return_value=None)
    spy = mocker.spy(mock_update.message, 'reply_text')

    # act
    bot.remove(mock_update, mock_context)

    # assert
    assert spy.call_count == 1
    assert spy.spy_return == None


def test_remove_not_in_list(mocker: MockerFixture) -> None:
    # arrange
    chat=Chat(0, 'private')
    mock_update = Update(0, message=Message(0, text="/remove fagioli", chat=chat, date=datetime.now()))
    mock_context = mocker.MagicMock()
    mock_context.args = ['fagioli']
    bot.shopping_lists = {0: ['pasta ']}
    mocker.patch.object(mock_update.message, 'reply_text', return_value=None)
    spy = mocker.spy(mock_update.message, 'reply_text')

    # act
    bot.remove(mock_update, mock_context)

    # assert
    assert bot.shopping_lists == {0: ['pasta ']}
    assert spy.call_count == 1
    assert spy.spy_return == None


def test_remove_while_in_list(mocker: MockerFixture) -> None:
    # arrange
    chat=Chat(0, 'private')
    mock_update = Update(0, message=Message(0, text="/remove fagioli", chat=chat, date=datetime.now()))
    mock_context = mocker.MagicMock()
    mock_context.args = ['fagioli']
    bot.shopping_lists = {0: ['pasta ', 'fagioli ']}
    mocker.patch.object(mock_update.message, 'reply_text', return_value=None)
    spy = mocker.spy(mock_update.message, 'reply_text')

    # act
    bot.remove(mock_update, mock_context)
    
    # assert
    assert bot.shopping_lists == {0: ['pasta ']}
    assert spy.call_count == 1
    assert spy.spy_return == None
