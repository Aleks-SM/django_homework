from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

class Measurement(models.Model):
    measure = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement', verbose_name='Датчик')
    temperature = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Температура')
    time_measure = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')

    def __str__(self):
        return str(self.time_measure)

    class Meta:
        verbose_name = 'Показания датчика'
        verbose_name_plural = 'Показания датчиков'