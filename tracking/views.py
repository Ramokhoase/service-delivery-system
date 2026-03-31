from django.shortcuts import render
from reporting.models import Report

def track_report(request):
    """
    View 1 — Tracking Form
    Allows the user to enter their reference number
    to look up the status of their report.
    """
    return render(request, 'tracking/track_report.html')


def track_result(request):
    """
    View 2 — Tracking Result
    Displays the current status and details of the report
    matching the entered reference number.
    """
    ref = request.GET.get('ref', '').strip().upper()
    report = None
    error  = None

    if ref:
        try:
            report = Report.objects.get(reference_number=ref)
        except Report.DoesNotExist:
            error = f'No report found with reference number "{ref}". Please check and try again.'
    else:
        error = 'Please enter a reference number.'

    return render(request, 'tracking/track_result.html', {
        'report': report,
        'ref': ref,
        'error': error,
    })
