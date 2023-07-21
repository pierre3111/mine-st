from django.shortcuts import render

def registration_form(request):
    if request.method == 'POST':
        # Process the submitted form data here (e.g., save to the database)
        # Replace the code below with your actual form processing logic
        name = request.POST.get('name')
        email = request.POST.get('email')
        job_role = request.POST.get('job_role')
        topics_interest = request.POST.getlist('topics_interest')
        card_number = request.POST.get('card_number')
        zip_code = request.POST.get('zip_code')
        cvv = request.POST.get('cvv')
        expiration_date = request.POST.get('expiration_date')

        # Add your form processing logic here
        # ...

        # For now, let's just return a simple success message
        return render(request, 'registration/registration_success.html', {'name': name})

    # If the request method is GET, display the registration form
    return render(request, 'registration/registration.html')


def registration_success(request):
    # Retrieve the registration details from the database or session
    name = 'John Doe'  # Replace with the actual user's name
    email = 'john@example.com'  # Replace with the actual user's email

    # Render the registration success page with the user's details
    return render(request, 'conferences/registration_success.html', {'name': name, 'email': email})