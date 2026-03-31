from django.shortcuts import render, redirect
from .models import Report

def send_sms_confirmation(phone_number, reference_number, issue_type):
    """
    Simulates sending an SMS confirmation to the user.
    In a real system this would connect to BulkSMS or Vonage API.
    The message is printed to the terminal to simulate the SMS.
    """
    message = (
        f"CityMenderSA: Your report has been received.\n"
        f"Reference Number: {reference_number}\n"
        f"Issue: {issue_type}\n"
        f"Track your report at: http://127.0.0.1:8000/tracking/\n"
        f"Save your reference number to check updates."
    )
    print("\n" + "="*50)
    print(f"SMS SENT TO: {phone_number}")
    print("="*50)
    print(message)
    print("="*50 + "\n")
    return True


def report_form(request):
    """
    View 1 — Report Form
    Handles the full reporting flow:
    language selection, mode selection, and report submission.
    """
    if request.method == 'POST':
        language    = request.POST.get('language')
        mode        = request.POST.get('mode')
        issue_type  = request.POST.get('issue_type')
        address     = request.POST.get('address')
        description = request.POST.get('description')
        phone       = request.POST.get('phone_number')

        report = Report.objects.create(
            language=language,
            mode=mode,
            issue_type=issue_type,
            address=address,
            description=description,
            phone_number=phone,
        )

        send_sms_confirmation(
            phone_number=phone,
            reference_number=report.reference_number,
            issue_type=report.get_issue_type_display(),
        )

        return redirect('report_success', ref=report.reference_number)

    return render(request, 'reporting/report_form.html')


def report_success(request, ref):
    """
    View 2 — Success Page
    Shows the generated reference number and confirmation message
    after a report is successfully submitted.
    """
    try:
        report = Report.objects.get(reference_number=ref)
    except Report.DoesNotExist:
        report = None

    return render(request, 'reporting/report_success.html', {'report': report})


