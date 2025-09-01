from django.http import HttpResponseForbidden

class RequestKwargToForm(object):
    # add the request to the kwargs
    def get_form_kwargs(self):
        kwargs = super(RequestKwargToForm, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class StaffOnly(object):
    '''
    Mixins returns Forbidden if user is not stuff
    '''
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_active or not request.user.is_staff:
            return HttpResponseForbidden()
        else:
            return super(StaffOnly, self).dispatch(request, *args, **kwargs)