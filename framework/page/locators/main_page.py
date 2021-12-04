from enum import Enum


class MainPageLocator(str, Enum):
    COMPARE_BTN = 'many__price-btn'
    BUY_BTN = '/html/body/div/div/div/div[3]/div[3]/div[3]/div[3]/div[3]/div[2]/div/div[4]/a[2]'


class Category(str, Enum):
    COMPUTERS = 'computers'
    AUTO = 'auto'
    HOME = 'dom'
    HOUSEHOLD = 'bt'


class HouseholdSubcategory(str, Enum):
    WASHING_MACHINES = 'Пральні та сушильні машини'
    REFRIGERATORS = 'Холодильники'
    OWENS = 'Духовки'
