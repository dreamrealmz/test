from django.db import models
from django.conf import settings


class SectionEnrollment(models.Model):
    students = models.ManyToManyField(
        to='Student',
        related_name=settings.RELATED_BASE_NAME + 'enrollment'
    )
    section = models.OneToOneField(
        to='Section',
        on_delete=models.CASCADE,
        related_name=settings.RELATED_BASE_NAME + 'enrollment'
    )
    enrollment_date = models.DateField(unique=True)

    def __str__(self):
        return f"Зачисления в секцию {self.section.name} от {self.enrollment_date}"

    class Meta:
        verbose_name = 'Зачисление'
        verbose_name_plural = 'Зачисления'
