from datetime import datetime
from random import choice
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from datacenter.models import Schoolkid, Mark, Сhastisement, Lesson, \
    Commendation


class SchoolHack:
    def __init__(self, full_name):
        try:
            self.schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
        except ObjectDoesNotExist:
            print('Не нашли ученика с таким параметром!')
        except MultipleObjectsReturned:
            print('В базе несколько учеников c таким параметром!')

    def fix_marks(self):
        Mark.objects.filter(schoolkid=self.schoolkid, points__in=[2, 3]).update(points=5)
        print(f'Исправили у {self.schoolkid} все 2 и 3 на 5')

    def remove_chastisements(self):
        Сhastisement.objects.filter(schoolkid=self.schoolkid).delete()
        print('Удалили у {self.schoolkid} все замечания')

    def set_commendation(self, subject_title, date_commendation):
        list_of_commendations = [
            'Молодец!',
            'Отлично!',
            'Хорошо!',
            'Гораздо лучше, чем я ожидал!',
            'Ты меня приятно удивил!',
            'Великолепно!',
            'Прекрасно!',
            'Ты меня очень обрадовал!',
            'Именно этого я давно ждал от тебя!',
            'Сказано здорово – просто и ясно!',
            'Ты, как всегда, точен!',
            'Очень хороший ответ!',
            'Талантливо!',
            'Ты сегодня прыгнул выше головы!',
            'Я поражен!',
            'Уже существенно лучше!',
            'Потрясающе!',
            'Замечательно!',
            'Прекрасное начало!',
            'Так держать!',
            'Ты на верном пути!',
            'Здорово!',
            'Это как раз то, что нужно!',
            'Я тобой горжусь!',
            'С каждым разом у тебя получается всё лучше!',
            'Мы с тобой не зря поработали!',
            'Я вижу, как ты стараешься!',
            'Ты растешь над собой!',
            'Ты многое сделал, я это вижу!',
            'Теперь у тебя точно все получится!',]
        random_commendation = choice(list_of_commendations)

        lesson = Lesson.objects.filter(year_of_study=self.schoolkid.year_of_study,
                                       group_letter=self.schoolkid.group_letter,
                                       subject__title=subject_title).order_by('-date').first()

        Commendation.objects.create(text=random_commendation,
                                    schoolkid=self.schoolkid,
                                    teacher=lesson.teacher,
                                    subject=lesson.subject,
                                    created=datetime.strptime(date_commendation,'%d.%m.%Y'))
