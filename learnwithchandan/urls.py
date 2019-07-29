
from django.contrib import admin
from django.urls import path,include,re_path
from blog.views import ShowPosts,ShowDetail
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ShowPosts.as_view(),name='show_posts'),
    re_path(r'^(?P<pk>\d+)/$',ShowDetail.as_view(),name='post_detail'),
    # re_path(r'^(?P<pk>\d+)/$',commentform,name='form_view')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)