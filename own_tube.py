import time
import sys


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age
        self.hash_password = hash(password)

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname
        return False


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        if not None:
            return f'{self.title}'
        # return f'(Название:{self.title}, Время: {self.duration} секунд, adult_mode: {self.adult_mode})'


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.hash_password:
                self.current_user = user
                print(f"Я {nickname} последний Пользователь прошедший авторизацию.")
                return True
        if self.current_user is None:
            print(f"Пользователей прошедших авторизацию не найдено.")
            return False

    def register(self, nickname: str, password: str, age: int):
        new_user = User(nickname, password, age)
        if new_user in self.users:
            print(f'Пользователь {nickname} уже существует')
            return
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошёл.")

    def log_out(self):
        print(f'Пользователь {self.current_user} вышел')
        self.current_user = None

    def add(self, *new_videos):
        for current_video in new_videos:
            duplicate = False
            for existing_video in self.videos:
                if current_video.title == existing_video.title:
                    duplicate = True
                    break
            if not duplicate:
                self.videos.append(current_video)
        return

    def get_videos(self, search_string: str):
        search_string = search_string.lower()
        search_list = []
        for video_in_search in self.videos:
            if search_string in video_in_search.title.lower():
                search_list.append(video_in_search.title)
        if not search_list:
            print('Видео с таким названием не найдено')
            return ""
        return search_list

    def watch_video(self, watch_title: str):
        for video_in_need in self.videos:
            if not self.current_user:
                print('Войдите в аккаунт, чтобы смотреть видео')
                return
            if watch_title == video_in_need.title:
                if video_in_need.adult_mode:
                    if self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        return
                    print(f'Начало просмотра: {video_in_need.title}')
                    print('Секунды')
                    while video_in_need.time_now < video_in_need.duration:
                        time.sleep(1)
                        video_in_need.time_now += 1
                        sys.stdout.write(f"{video_in_need.time_now} ")
                        sys.stdout.flush()
                    print('Конец видео')


# Код для проверки:

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# print(ur.get_videos('не существует'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
