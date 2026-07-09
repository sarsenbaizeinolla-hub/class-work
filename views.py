from django.views.generic import UpdateView

class AdUpdateView(LoginRequiredMixin, UpdateView):
    model = Ad
    fields = ['title', 'description', 'image']
    template_name = 'ad_form.html'
    success_url = reverse_lazy('ads_list')