from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    golf 게시글추천등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 신청할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('golf:detail', question_id=question.id)