from django.shortcuts import render, redirect

from help.models import Help

# 작성하는 창을 띄우는 함수
def show_post_write(request): # 글쓰기 창에 내용을 적어주면에 저장되어 요청을 보낸다
    return render(request, 'help/showpostwrite.html')

# 작성버튼을 눌렀을 때 글쓰기 버튼에 해당하는 함수
# 등록을 누르면 등록이 되는 함수
def post_write(request):
    # Help class에 있는 post_insert 함수가 돌아가고
    Help().post_insert(request.POST)
    # 게시글 작성이 끝나면 help앱의 showpostlist라는 이름이 달린 url로 가라
    return redirect('help:showpostlist')

# post list - 글 목록 창을 띄우는 함수
def show_post_list(request):
    # Help에 있는 post_list 함수를 post_list에 담아주고
    post_list = Help().post_list()
    # 'help/showpostlist.html'을 보여줄건데 post_list를 post_list라는 이름으로 갈거다
    return render(request, 'help/showpostlist.html', {'post_list': post_list})
# show_post_list함수가 호출이 되면 help().post_list()가 post_list에 담긴다. post_list를 post_list라는 이름으로 갈거다
# render가 help/showpostlist.html을 띄워준다.

# post detail - 상세페이지 창을 띄우는 함수
def show_post_detail(request, post_seq):
    # Help앱에 있는 post_detail에 있는 함수를 호출해서 post_detail에 넣어 준다
    post_info = Help().post_detail(post_seq)
    # sql 쿼리에 데이터가 들어가는 자리이기 때문에 post_detail 에 있는 함수에 있는 쿼리문을 실행 시켜준다.
    reply_detail = [('알겠습니다.', 'dada', '22/01/23 20:21:00,', 0),
                    ('저는 아닙니다.', 'jaejae', '22/01/23 20:22:00,', 0)]
    return render(request, 'help/showpostdetail.html', {'post_seq': post_seq, 'post_detail': post_info, 'reply_detail': reply_detail})

def show_post_update(request, post_seq):
    post_detail = Help().post_update_detail(post_seq)
    return render(request, 'help/showpostupdate.html', {'post_detail': post_detail, 'post_seq': post_seq})

def post_update(request, post_seq):
    Help().post_update(post_seq, request.POST)
                                        # 수정된 번호를 기억하기 위해서 post_seq=post_seq에 써준다.
    return redirect('help:showpostdetail', post_seq=post_seq)

def post_delete(request, post_seq):
    Help().post_delete(post_seq)
    return redirect('help:showpostlist')
