import os
import re
from django.core.management.base import BaseCommand
from docx import Document

from subject.models import Lecture, Test, TestOption


class Command(BaseCommand):
    help = "Import Word fayldagi testlarni Lecture modeliga biriktirib yuklash."

    def add_arguments(self, parser):
        parser.add_argument('folder_path', type=str, help='Testlar saqlangan Word fayllar papkasi yo‘li')

    def handle(self, *args, **kwargs):
        folder_path = kwargs['folder_path']
        files = [f for f in os.listdir(folder_path) if f.endswith('.docx')]

        for file_name in files:
            lecture_name = file_name.replace('.docx', '').strip()
            try:
                lecture = Lecture.objects.get(name__iexact=lecture_name)
            except Lecture.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Lecture topilmadi: {lecture_name}"))
                continue

            doc_path = os.path.join(folder_path, file_name)
            document = Document(doc_path)

            full_text = '\n'.join([p.text for p in document.paragraphs if p.text.strip()])

            question_blocks = re.findall(
                r'(\d+)\.\s*(.*?)\nA\)(.*?)\nB\)(.*?)\nC\)(.*?)\nD\)(.*?)(?=\n\d+\.|\Z)',
                full_text, re.DOTALL
            )

            for block in question_blocks:
                number, question, a, b, c, d = [item.strip() for item in block]
                test = Test.objects.create(lesson=lecture, question=question)
                TestOption.objects.bulk_create([
                    TestOption(test=test, text=a, is_correct=True),   # A har doim to‘g‘ri
                    TestOption(test=test, text=b, is_correct=False),
                    TestOption(test=test, text=c, is_correct=False),
                    TestOption(test=test, text=d, is_correct=False),
                ])
                self.stdout.write(self.style.SUCCESS(f"{lecture.name} uchun {number}-savol import qilindi."))

        self.stdout.write(self.style.SUCCESS("Barcha testlar muvaffaqiyatli yuklandi."))
