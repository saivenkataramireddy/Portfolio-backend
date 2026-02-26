from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .models import Blog, Projects, Certifications, Contact, Skill, Journey
from .serializers import BlogSerializer, ProjectsSerializer, CertificationsSerializer, SkillSerializer, JourneySerializer

def send_email_to_me(name, email, contact_number, message_text):
    subject = '📩 New Contact Form Submission'
    message = f"""
👤 Name: {name}
📧 Email: {email}
📱 Phone: {contact_number if contact_number else 'N/A'}
💬 Message: {message_text}
"""
    send_mail(
        subject,
        message,
        'yourgmail@gmail.com',  # FROM email
        ['saivenkataramireddykesara@gmail.com'],  # TO email(s)
        fail_silently=False,
    )

@api_view(['GET'])
def get_portfolio_data(request):
    blogs = Blog.objects.all()
    projects = Projects.objects.all()
    certifications = Certifications.objects.all()
    skills = Skill.objects.all()
    journeys = Journey.objects.all().order_by('year')

    return Response({
        'blogs': BlogSerializer(blogs, many=True).data,
        'projects': ProjectsSerializer(projects, many=True).data,
        'certifications': CertificationsSerializer(certifications, many=True).data,
        'skills': SkillSerializer(skills, many=True).data,
        'journeys': JourneySerializer(journeys, many=True).data,
    })

@api_view(['GET'])
def project_detail(request, project_id):
    try:
        project = Projects.objects.get(pk=project_id)
        return Response(ProjectsSerializer(project).data)
    except Projects.DoesNotExist:
        return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def contact_submit(request):
    name = request.data.get("name")
    email = request.data.get("email")
    contact_number = request.data.get("contact_number", "")
    message = request.data.get("message")

    if name and email and message:
        Contact.objects.create(name=name, email=email, contact_number=contact_number, message=message)
        try:
            send_email_to_me(name, email, contact_number, message)
        except Exception as e:
            pass # Continue even if email fails
        return Response({"message": "Your message has been sent successfully!"}, status=status.HTTP_201_CREATED)
    return Response({"error": "Missing fields"}, status=status.HTTP_400_BAD_REQUEST)
