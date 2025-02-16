import doctest
from typing import Union


class Online_cinema:
    """
    Создание и подготовка к работе объекта "Online_cinema" - это базовый класс

    :param subscription: Есть ли подписка на данный сервис (True/False)
    :param mobile_support: Есть ли поддержка мобильньных устрйств (True/False)

    Примеры:
    >>> online_cinema = Online_cinema(True, True)
    """

    def __init__(self, subscription: bool, mobile_support: bool):
        if not isinstance(subscription, bool):
            raise TypeError('Подписка на онлайн сервис должна быть типа bool')
        self.subscription = subscription

        if not isinstance(mobile_support, bool):
            raise TypeError('Поддержка мобильных устройств должна быть типа bool')
        self._mobile_support = mobile_support  # непубличный, так как поддержка устройств либо есть, либо нет

    def get_subscription_status(self) -> str:
        """Возвращает статус подписки на данный момент"""
        return "Активна" if self.subscription else "Не активна"

    def __str__(self):
        return (f"Активность подписки на данный момент {self.subscription}, "
                f"Поддержка мобильных устройств {self._mobile_support}")

    def __repr__(self):
        return f"{self.__class__.__name__}(subscription={self.subscription!r}, mobile_support={self._mobile_support!r})"


class KinoPoisk(Online_cinema):
    """
    Создание и подготовка к работе объекта "KinoPoisk" - это дочерний класс

    :param subscription: Есть ли подписка на Кинопоиск (True/False)
    :param mobile_support: Есть ли поддержка мобильных устрoйств у Кинопоиска (True/False)
    :param rating: Рейтинг Кинопоиска (от 0 до 10)
    :param trial_period: Есть ли пробный период подписки (True/False)

    Примеры:
    >>> kino = KinoPoisk(True, True, 8.5, True)
    """

    def __init__(self, subscription: bool, mobile_support: bool, rating: Union[float, int], trial_period: bool):
        super().__init__(subscription, mobile_support)

        if not isinstance(rating, (int, float)):
            raise TypeError('Рейтинг Кинопоиска должен быть типа int или float')
        if (rating < 0) or (rating > 10):
            raise ValueError('Рейтинг Кинопоиска должен находиться в промежутке от 0 до 10')
        self.rating = rating

        if not isinstance(trial_period, bool):
            raise TypeError('Пробный период должен быть типа bool')
        self._trial_period = trial_period  # непубличный, так как задается при регистрации и один раз обычно

    def get_subscription_status(self) -> str:
        """
        Перегруженный метод получения статуса подписки
        В отличие от базового класса, учитывает пробный период
        """

        if self.subscription:
            return "Активна"
        elif self._trial_period:
            return "На пробном периоде"
        return "Не активна"

    def __str__(self):
        return (f"Активность подписки на данный момент {self.subscription}, "
                f"Поддержка мобильных устройств {self._mobile_support}, "
                f"Рейтинг Кинопоиска {self.rating}, Пробный период {self._trial_period}")

    def __repr__(self):
        return (f"{self.__class__.__name__}(subscription={self.subscription!r}, mobile_support={self._mobile_support!r}, "
                f"rating={self.rating!r}, trial_period={self._trial_period!r})")


if __name__ == "__main__":
    doctest.testmod()
pass
