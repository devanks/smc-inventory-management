from django.contrib import admin

# Register your models here.
from .models import record
from .models import recordSummary

from import_export import resources

from .ModuleAdminSettings import ImportExportActionModelAdmin
# from .ModuleSummaryAdminSettings import recordSummaryAdmin

class RecordResource(resources.ModelResource):

    class Meta:
        model = record
        exclude = ('id', )
class recordSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/record_summary_change_graph.html'
    list_filter = (
        'device','department',Count('id')
    )
		
class recordAdmin(ImportExportActionModelAdmin):
    #resource_class = RecordResource
    list_display = ['name', 'department', 'year', 'device']
    list_filter = ('department', 'year', 'device')
    search_fields = ('name', 'department')
    pass

admin.site.register(record,recordAdmin)
admin.site.register(recordSummary,recordSummaryAdmin)