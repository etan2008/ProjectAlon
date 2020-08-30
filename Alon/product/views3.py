from django.shortcuts import render
import pandas as pd
from .models import BarangayBuoy, Intruder
from .utils import get_performance_plot
from .alonbackend import *
# Create your views here.

#step 3


def chart_select_view(request):
    barangay_df = pd.DataFrame(BarangayBuoy.objects.all().values())
    intruder_df = pd.DataFrame(Intruder.objects.all().values())
    holder_df = None
    error_message = None

    #databases, add katong optional dropdown list
    if barangay_df.shape[0] > 0 or intruder_df.shape[0] > 0:
        if request.method == 'POST':
            db = request.POST['database']
            level = request.POST['level']
            province = request.POST['province']
            municipality = request.POST['municipality']
            barangay = request.POST['barangay']
            date_from = request.POST['date_from']
            date_to = request.POST['date_to']

            print(db)
            print(level)
            print(province)
            print(municipality)
            print(barangay)
            print(date_from)
            print(date_to)
            if db != "":
                if db == "buoys":
                    if barangay_df.shape[0] > 0 :
                        if level != "":
                            if level == "provincial" or level == "municipal" or level == "barangay":
                                if province != "":
                                    if level == "municipal" or level == "barangay":
                                        if municipality != "":
                                            if level == "barangay": # barangay level
                                                barangay_df = barangay_df[((barangay_df['province'] == province) & (barangay_df['municipality'] == municipality)) & (barangay_df['barangay'] == barangay)]
                                                if barangay_df.shape[0] > 0 and not barangay_df.empty:
                                                    holder_df = barangay_df
                                                else:
                                                    error_message = "No records exist"
                                            else: # municipal level
                                                barangay_df = barangay_df[(barangay_df['province'] == province) & (barangay_df['municipality'] == municipality)]
                                                if barangay_df.shape[0] > 0 and not barangay_df.empty:
                                                    holder_df = barangay_df
                                                else:
                                                    error_message = "No records exist"
                                        else:
                                            error_message = "No municipality selected" # null municipality
                                    else: # provincial level
                                        barangay_df = barangay_df[(barangay_df['province'] == province)]
                                        if barangay_df.shape[0] > 0 and not barangay_df.empty:
                                            holder_df = barangay_df
                                        else:
                                            error_message = "No records exist"
                                else:
                                    error_message = "No province selected" # null provice
                            else:
                                error_message = "No such choice exists" # choice only
                        else:
                            error_message = "No level selected" # null level
                    else:
                        error_message = "barangay Database Empty"
                else:
                    if intruder_df.shape[0] > 0 :
                        intruder_df['date'] = intruder_df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
                        if level != "":
                            if level == "provincial" or level == "municipal" or level == "barangay":
                                if province != "":
                                    if level == "municipal" or level == "barangay":
                                        if municipality != "":
                                            if level == "barangay": # barangay level
                                                intruder_df = intruder_df[((intruder_df['province'] == province) & (intruder_df['municipality'] == municipality)) & (intruder_df['barangay'] == barangay)]
                                                if intruder_df.shape[0] > 0 and not intruder_df.empty:
                                                    holder_df = intruder_df[(intruder_df['date'] > date_from) & (intruder_df['date'] <= date_to)]
                                                else:
                                                    error_message = "No records exist"
                                            else: # municipal level
                                                intruder_df = intruder_df[(intruder_df['province'] == province) & (intruder_df['municipality'] == municipality)]
                                                if intruder_df.shape[0] > 0 and not intruder_df.empty:
                                                    holder_df = intruder_df[(intruder_df['date'] > date_from) & (intruder_df['date'] <= date_to)]
                                                else:
                                                    error_message = "No records exist"

                                        else:
                                            error_message = "No municipality selected" # null municipality
                                    else: # provincial level
                                        intruder_df = intruder_df[(intruder_df['province'] == province)]
                                        if intruder_df.shape[0] > 0 and not intruder_df.empty:
                                            holder_df = intruder_df[(intruder_df['date'] > date_from) & (intruder_df['date'] <= date_to)]
                                        else:
                                            error_message = "No records exist"
                                else:
                                    error_message = "No province selected" # null provice
                            else:
                                error_message = "No such choice exists" # choice only
                        else:
                            error_message = "No level selected" # null level
                    else:
                        error_message = "Intruder Database Empty"
            else:
                error_message = "No database selected"
    else:
        error_message = "No record in the database"

    #what you want to display, used in main html
    if type(holder_df) == pd.DataFrame and not holder_df.empty:
        holder_df = holder_df.to_html()
    else:
        if type(holder_df) == pd.DataFrame:
            error_message = "No records exist"
        holder_df = None

    context = {
        # 'graph' : graph,
        'holder_df' : holder_df,
        'error_message' : error_message,
    }

    return render(request, 'product/main.html',context)

def stats_view(request):
    intruder_df = pd.DataFrame(Intruder.objects.all().values())
    error_message = None
    graph = None

    if intruder_df.shape[0] > 0:
        # pass
    #     if request.method == 'POST':
    #         chart_type = request.POST['sales']
    #         date_from = request.POST['date_from']
    #         date_to = request.POST['date_to']
    #
            intruder_df['date'] = intruder_df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
            print(intruder_df['date'])
    #         merged_df2 = merged_df.groupby('date',as_index=False)['total_price'].agg('sum')
    #
    #         #chart type is necessary
    #         if chart_type != "":
    #             print(chart_type)
    #             if date_from != "" and date_to != "":
    #                 merged_df = merged_df[(merged_df['date']>date_from) & (merged_df['date'<date_to])]
    #                 print(merged_df)
    #             #graphing function
    #
    #             #kwargs: keyword arguments: x, y, data, df
    #             graph = get_performance_plot(chart_type, x=merged_df2['date'], y=merged_df2['total_price'], data=merged_df)
    #         else:
    #             error_message = "No chart selected"
    else:
        error_message = "No record in the database"

    #what you want to display, used in main html
    context = {
        'graph' : graph,
        'error_message' : error_message,
    }

    return render(request, 'product/stats.html',context)

def plots_view(request):
    barangay_df = pd.DataFrame(barangayBuoy.objects.all().values())
    intruder_df = pd.DataFrame(Intruder.objects.all().values())
    error_message = None
    graph = None

    if barangay_df.shape[0] > 0:
        pass
    #     if request.method == 'POST':
    #         chart_type = request.POST['sales']
    #         date_from = request.POST['date_from']
    #         date_to = request.POST['date_to']
    #
    #         merged_df['date'] = merged_df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    #         merged_df2 = merged_df.groupby('date',as_index=False)['total_price'].agg('sum')
    #
    #         #chart type is necessary
    #         if chart_type != "":
    #             print(chart_type)
    #             if date_from != "" and date_to != "":
    #                 merged_df = merged_df[(merged_df['date']>date_from) & (merged_df['date'<date_to])]
    #                 print(merged_df)
    #             #graphing function
    #
    #             #kwargs: keyword arguments: x, y, data, df
    #             graph = get_performance_plot(chart_type, x=merged_df2['date'], y=merged_df2['total_price'], data=merged_df)
    #         else:
    #             error_message = "No chart selected"
    else:
        error_message = "No record in the database"

    #what you want to display, used in main html
    context = {
        'graph' : graph,
        'error_message' : error_message,
    }

    return render(request, 'product/plots.html',context)

    def load_provinces(request):
        province_id = request.GET.get('province')
        provinces = City.objects.filter(province_id=province_id).order_by('name')
        return render(request, 'province_dropdown_list_options.html', {'provinces': provinces})

    def load_cities(request):
        city_id = request.GET.get('city')
        cities = City.objects.filter(city_id=city_id).order_by('name')
        return render(request, 'city_dropdown_list_options.html', {'cities': cities})

    def load_barangay(request):
        barangay_id = request.GET.get('barangay')
        barangays = City.objects.filter(barangay_id=barangay_id).order_by('name')
        return render(request, 'barangy_dropdown_list_options.html', {'barangay': barangays})

    def load_year(request):
        year_id = request.GET.get('year')
        years = City.objects.filter(year_id=year_id).order_by('name')
        return render(request, 'year_dropdown_list_options.html', {'year': years})
