# Create your views here.
from django.shortcuts import render


def bb_write(request):
    return render(request,"used/bb_write.html")


def used(request):
    return render(request,"used/used.html")

UPLOAD_DIR = '/home/kosmo100/ws/chemistrry/used/static/images/'
def bb_insert(request):
    if 'file1' in request.FILES:
        file = request.FILES['file1']
        file_name = file._name
        fp = open(UPLOAD_DIR + file_name,'wb')
        # chunks는 1byte단위로 읽어들이는 함수다.
        for chunk in file.chunks():
            # 이게 파일 저장하는거였나?
            fp.write(chunk) #저장된 파일을 fp라는 파일에 쓴다.
        fp.close() # open후 꼭 닫아야 함.
    else:
        # file_name 의 '-' 이거 뭐였지? file에 이미지가 없다면?
        # 이미지가 없다면 DB picture_url 컬럼에 - 이 들어온다는 의
        file_name = '-'
    dto = Product(product_name=request.POST['product_name'],
                  price=request.POST['price'],
                  description=request.POST['description'],
                  picture_url=file_name)
    dto.save()
    # 근데 왜 내용도 없는데(success.html) 이 경로를 지정해주는거죠? 오류 안나게한다고요?
    return redirect('/shop/product_list')

