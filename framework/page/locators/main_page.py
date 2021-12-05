from enum import Enum


class MainPageLocator(str, Enum):
    COMPARE_BTN = 'many__price-btn'
    BUY_BTN = '/html/body/div/div/div/div[3]/div[3]/div[3]/div[3]/div[2]/div[2]/div/div[4]/a[2]'


class Category(str, Enum):
    COMPUTERS = 'computer'
    AUTO = 'auto'
    HOME = 'dom'
    HOUSEHOLD = 'bt'


class CategoryLink(str, Enum):
    COMPUTERS = 'https://hotline.ua/computer/'
    AUTO = 'https://hotline.ua/auto/'
    HOME = 'https://hotline.ua/dom/'
    HOUSEHOLD = 'https://hotline.ua/bt/'


class HouseholdSubcategory(str, Enum):
    WASHING_MACHINES = 'Пральні та сушильні машини'
    REFRIGERATORS = 'Холодильники'
    OWENS = 'Духовки'


class HouseholdSubcategoryLink(str, Enum):
    WASHING_MACHINES = 'https://hotline.ua/bt/stiralnye-i-sushilnye-mashiny/'
    REFRIGERATORS = 'https://hotline.ua/bt/stiralnye-i-sushilnye-mashiny/'
    OWENS = 'https://hotline.ua/bt/duhovki/'
