import pytest
from src import bot


def test_new_user():
    # arrange
    chat_id = 0
    bot.shopping_lists = {}
    
    # act
    bot.new_user(chat_id)
    
    # assert
    assert bot.shopping_lists == {0: []}
