from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from datacenter.helpers import format_duration


def storage_information_view(request):
    non_closed_visits_query = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in non_closed_visits_query:
        non_closed_visit = {
            "who_entered": visit.passcard.owner_name,
            "entered_at": timezone.localtime(visit.entered_at),
            "duration": format_duration(visit.get_duration()),
            "is_strange": visit.is_visit_long()
        }
        non_closed_visits.append(non_closed_visit)
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
