import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ContactMessage

@csrf_exempt
def contact_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    company = data.get("company", "")
    project_type = data.get("project-type", "")
    message = data.get("message")

    if not all([name, email, phone, message]):
        return JsonResponse({"error": "Missing required fields"}, status=400)

    ContactMessage.objects.create(
        name=name,
        email=email,
        phone=phone,
        company=company,
        project_type=project_type,
        message=message,
    )

    return JsonResponse({"success": True, "message": "Message received!"})
