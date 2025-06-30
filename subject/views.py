from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from subject.models import Lecture, Practice, Laboratory, Test, Videos


def main(request):
    return render(request, 'main.html')


def lesson_list(request):
    lectures = Lecture.objects.all()
    practices = Practice.objects.all()
    laboratories = Laboratory.objects.all()
    videos = Videos.objects.all()

    context = {
        'lectures': lectures,
        'practices': practices,
        'laboratories': laboratories,
        'videos': videos,
    }
    return render(request, 'lesson_list.html', context)


def test(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    tests = Test.objects.filter(lesson=lecture).prefetch_related("options")

    return render(request, 'test.html', {
        'lesson': lecture,
        'tests': tests
    })
