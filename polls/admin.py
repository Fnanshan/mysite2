from django.contrib import admin

from .models import Question, Choice


# Register your models here.

class ChoiceInline(admin.TabularInline):        # StackedInline :叠放式的显示关联对象；TabularInline :表格式的单行显示关联对象
    model = Choice
    # 3个Choice选项插槽
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # 列标题排序
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 变更页分页
    list_per_page = 2
    # 过滤器，允许人们以 pub_date 字段来过滤列表
    list_filter = ['pub_date']
    # 搜索框，搜索 question_text 字段
    search_fields = ['question_text']
    # 日期层次结构
    date_hierarchy = 'pub_date'


admin.site.register(Question, QuestionAdmin)
