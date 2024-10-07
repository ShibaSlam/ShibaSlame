from referral_system import register_user

import random
import string

# Генерация уникального идентификатора для реферальной ссылки
def generate_referral_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Пример базы данных пользователей (в реальности используйте базу данных)
users = {}

# Начальное количество токенов у обычного пользователя и премиум пользователя
initial_tokens_regular = 100000  # 100,000 токенов у обычного пользователя
initial_tokens_premium = 100000  # 100,000 токенов у премиум пользователя

# Регистрация нового пользователя с реферальной ссылкой
def register_user(username, referrer=None, is_premium=False):
    referral_code = generate_referral_code()
    # Определяем начальное количество токенов в зависимости от статуса
    initial_tokens = initial_tokens_premium if is_premium else initial_tokens_regular
    users[username] = {
        'referral_code': referral_code,
        'referrer': referrer,
        'tokens': initial_tokens,
        'rewarded': False  # Для отслеживания, получил ли реферер награду
    }
    
    if referrer:
        # Наградить реферера
        reward_referrer(referrer, is_premium)
        
        # Наградить приглашённого пользователя в зависимости от его статуса
        reward_amount = 100000 if is_premium else 50000  # 100,000 токенов для премиум и 50,000 для обычного
        users[username]['tokens'] += reward_amount
        print(f"{username} получил {reward_amount} ShibaSlam токенов за регистрацию по реферальной ссылке!")

    print(f"Пользователь {username} зарегистрирован с реферальным кодом {referral_code}.")

# Функция награждения реферера
def reward_referrer(referrer, is_premium):
    reward_amount = 100000 if is_premium else 50000  # 100,000 токенов для премиум и 50,000 для обычного
    users[referrer]['tokens'] += reward_amount
    users[referrer]['rewarded'] = True  # Обновление статуса награды
    print(f"{referrer} получил {reward_amount} ShibaSlam токенов за привлечение {users[referrer]['referral_code']}!")

# Пример регистрации пользователей
register_user("user1", is_premium=True)  # Премиум пользователь
register_user("user2", referrer="user1")  # Обычный пользователь
register_user("user3", referrer="user1", is_premium=True)  # Премиум пользователь