ABOUT_BOT = """
🤖 Бот для отслеживания номерков к врачам Санкт-Петербурга.
✏ Поддерживает автоматическую запись по критериям
"""

HELP = """
📋 Список доступных команд

🧩 Общие:
/start - Об этом боте
/help - Список доступных команд
/cancel - Отменить текущую операцию

👤 Управление профилями
/profiles - Список профилей
/create_profile - Создать профиль
"""

UNKNOWN_COMMAND = "❌ Неизвестная команда: {command}"

CANCELED = "✅ Текущая операция отменена"

GORZDRAV_ERROR = "❗ Ошибка на стороне портала \"Здоровье Петербуржца\". Попробуйте позже"

DISTRICT_SELECT = "📍 Выбери район учреждения"
UNKNOWN_DISTRICT = "❌ Неизвестный район: {district}."

CLINIC_SELECT = "🏥 Выбери учреждение"
UNKNOWN_CLINIC = "❌ Неизвестное учреждение: {clinic}."

SPECIALITY_SELECT = "📃 Выбери специальность"
UNKNOWN_SPECIALITY = "❌ Неизвестная специальность: {speciality}."

DOCTOR_SELECT = "🧑‍⚕️ Выбери врача"
UNKNOWN_DOCTOR = "❌ Неизвестный врач: {doctor}."

APPOINTMENT_SELECT = "🕐 Выбери время"
UNKNOWN_APPOINTMENT = "❌ Неизвестная дата записи: {appointment}."
NO_APPOINTMENTS = "❌ Нет доступных талонов."

# PROFILES
PROFILE = "👤 {last_name} {first_name} {middle_name} ({birthdate})"
PROFILE_KEYBOARD = "{last_name} {first_name} {middle_name} ({birthdate})"
NO_PROFILES = "❌ Нет сохраненных профилей"

SELECT_PROFILE = "📋 Выбери профиль"
PROFILE_CREATED = "✅ Профиль создан"
PROFILE_DELETED = "✅ Профиль удалён"

CREATE_PROFILE = "📋 Регистрация нового профиля"
DELETE_PROFILE = "Удалить профиль"

CONFIRM_DELETE_PROFILE = "❗ Подтвердите удаление профиля {profile}"
DELETE_PROFILE_CANCELED = "✅ Удаление профиля отменено"

UNKNOWN_PROFILE = "❌ Неизвестный профиль: {profile}."

ENTER_LAST_NAME = "✏ Введи фамилию"
ENTER_FIRST_NAME = "✏ Введи имя"
ENTER_MIDDLE_NAME = "✏ Введи отчество"
ENTER_BIRTHDATE = "📅 Введи дату рождения в формате ДД.ММ.ГГГГ"

WRONG_DATE = "❌ Неправильный формат даты"

CONFIRM = "Да"
CANCEL = "Отменить"
