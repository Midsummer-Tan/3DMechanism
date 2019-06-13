from django.core.files.storage import FileSystemStorage
from Myproject import settings
from django.http import HttpResponse
import os, time, random


class ImageStorage(FileSystemStorage):

    def __init__(self, location=settings.MEDIA_ROOT,   base_url=settings.MEDIA_URL):
        super(ImageStorage, self).__init__(location, base_url)

    # 重写 _save方法
    def _save(self, name, content):
        # 文件扩展名
        ext = os.path.splitext(name)[1]
        # 文件目录
        d = os.path.dirname(name)
        # 定义文件名，年月日时分秒随机数
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % (random.randint(0,100))
        # 重写合成文件名
        name = os.path.join(d, fn + ext)
        # 调用父类方法
        return super(ImageStorage, self)._save(name, content)