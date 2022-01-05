from django.views.generic import TemplateView


class ChatIndexView(TemplateView):
    template_name = "chat/index.html"


class ChatRoomView(TemplateView):
    template_name = "chat/room.html"

    def get_context_data(self, **kwargs):
        ctx = super(TemplateView, self).get_context_data(**kwargs)
        ctx['room_name'] = self.kwargs.get('room_name', '')
        return ctx