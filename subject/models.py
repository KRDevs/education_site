from django.db import models


class Lecture(models.Model):
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to="uploads/videolar/", blank=True, verbose_name="Video")
    word = models.FileField(upload_to="uploads/maruza_word/", blank=True, verbose_name="Ma'ruza word")
    presentation = models.FileField(upload_to="uploads/presentations/ma'ruza/", blank=True,
                                    verbose_name="Ma'ruza taqdimot")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = "Ma'ruza"
        verbose_name_plural = "Ma'ruzalar"


class Practice(models.Model):
    name = models.CharField(max_length=255)
    video = models.CharField(max_length=1024, blank=True)
    word = models.FileField(upload_to="uploads/amaliyot_word/", blank=True, verbose_name="Amaliyot word")
    presentation = models.FileField(upload_to="uploads/presentations/amaliyot/", blank=True,
                                    verbose_name="Amaliyot taqdimot")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = "Amaliyot"
        verbose_name_plural = "Amaliyotlar"


class Laboratory(models.Model):
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to="uploads/videolar/", blank=True, verbose_name="Video")
    word = models.FileField(upload_to="uploads/laboratoriya_word/", blank=True, verbose_name="Laboratoriya word")
    presentation = models.FileField(upload_to="uploads/presentations/laboratoriya/", blank=True,
                                    verbose_name="Laboratoriya taqdimot")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = "Laboratoriya"
        verbose_name_plural = "Laboratoriyalar"


class Test(models.Model):
    lesson = models.ForeignKey(Lecture, related_name="tests", on_delete=models.CASCADE)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Test'
        verbose_name_plural = 'Testlar'


class TestOption(models.Model):
    test = models.ForeignKey(Test, related_name="options", on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Variant'
        verbose_name_plural = 'Variantlar'

class Videos(models.Model):
    video = models.FileField(upload_to="uploads/videolar/", blank=True, verbose_name="Video")