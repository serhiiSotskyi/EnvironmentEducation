from django.shortcuts import render

# View for the Privacy Policy page
def privacyPolicy(request):
    return render(request, "legal/privacyPolicy.html")

# View for the Terms of Use page
def termsOfUse(request):
    return render(request, "legal/termsOfUse.html")
