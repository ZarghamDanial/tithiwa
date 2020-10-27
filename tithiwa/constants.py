import os

from selenium.webdriver.common.by import By

MODULEDIR = os.path.dirname(__file__)
SESSIONDIR = os.path.join(MODULEDIR, 'sessions')

DEFAULT_WAIT = 89


class SELECTORS(object):
    MAIN_SEARCH_BAR = (By.CSS_SELECTOR, '._3FRCZ')
    MAIN_SEARCH_BAR_DONE = (By.CSS_SELECTOR, '.MfAhJ')
    MAIN_SEARCH_BAR_SEARCH_ICON = (By.CSS_SELECTOR, '._3e4VU')
    MAIN_SEARCH_BAR_BACK_ARROW = (By.CSS_SELECTOR, '._3e4VU')
    MESSAGE_INPUT_BOX = (By.CSS_SELECTOR, '#main footer ._3FRCZ')
    TURN_ON_DESKTOP_NOTIFICATIONS = (By.CSS_SELECTOR, '.zKq5Y')
    CLOSE_INFO = (By.CSS_SELECTOR, '[data-testid="x-alt"]')
    MAIN_MENU_OPTIONS__MENU_ICON = (By.CSS_SELECTOR, '[data-testid=menu]')
    MAIN_MENU_OPTIONS__NEW_GROUP = (By.CSS_SELECTOR, '[title="New group"]')
    CREATE_NEW_GROUP__TYPE_CONTACTS_INPUT_BOX = (By.CSS_SELECTOR, '._17ePo')
    CREATE_NEW_GROUP__RESULT_CONTACT = (By.CSS_SELECTOR, '._210SC')
    CREATE_NEW_GROUP__OK_CONTACTS_TYPE = (By.CSS_SELECTOR, '[data-testid="arrow-forward"]')
    CREATE_NEW_GROUP__TYPE_GROUP_NAME = (By.CSS_SELECTOR, '._3FRCZ')
    CREATE_NEW_GROUP__OK_GROUP_NAME_TYPE = (By.CSS_SELECTOR, '._3y5oW')
    CREATE_NEW_GROUP__ENCRYPTED_LOCK_SIGN = (By.CSS_SELECTOR, '._2VO5X')
    CHATROOM__NAME_AND_INFO = (By.CSS_SELECTOR, '._33QME')
    CHATROOM__NAME = (By.CSS_SELECTOR, '.DP7CM')
    CHATROOM__INFO = (By.CSS_SELECTOR, '._3-cMa._3Whw5')
    CHATROOM__INFO__NUMBER = (By.CSS_SELECTOR, '._9l3wT')
    CHATROOM__CLOSE_INFO = (By.CSS_SELECTOR, '[data-testid="x"]')
    CHATROOM__OPTIONS = (By.CSS_SELECTOR, '[data-testid="menu"]')
    CONTACTS__NAME_IN_CHATS = (By.CSS_SELECTOR, '._357i8 > ._3ko75._5h6Y_._3Whw5')
    GROUPS__MEMBERS_SEARCH_ICON = (By.CSS_SELECTOR, '._3lS1C')
    GROUPS__SEARCH_CONTACTS_INPUT_BOX = (By.CSS_SELECTOR, '._9a59P ._3FRCZ')
    GROUPS__CONTACTS_SEARCH_NAME = (By.CSS_SELECTOR, '._3ko75')
    GROUPS__CLOSE_CONTACTS_SEARCH = (By.CSS_SELECTOR, '._2HE5l .t4a8o')
    GROUPS__ADMIN_ICON = (By.CSS_SELECTOR, '.LwCwJ')
    GROUPS__MAKE_ADMIN = (By.CSS_SELECTOR, '.Ut_N0')
    GROUPS__REMOVE = (By.CSS_SELECTOR, '.Ut_N0[title="Remove"]')
    GROUPS__EXIT_FROM_GROUP = (By.CSS_SELECTOR, '._3wAoe._3DSZk[title="Exit group"]')
    GROUPS__EXIT_DIALOG_BOX = (By.CSS_SELECTOR, '._9a59P')
    GROUPS__EXIT_BUTTON_EXIT_DIALOG_BOX = (By.CSS_SELECTOR, '.S7_rT.FV2Qy')
    GROUPS__NO_LONGER_A_PARTICIPANT = (By.CSS_SELECTOR, '._3ge3i')
    GROUPS__NAME_IN_CHATS = (By.CSS_SELECTOR, '._3CneP > ._3ko75._5h6Y_._3Whw5')


class STRINGS(object):
    CHECK_CHAR = '✔'
    CROSS_CHAR = '❌'