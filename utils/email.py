from django.core.mail import send_mail


def account_created_mail(user):
    print("email send ",user)
    response  = send_mail(
        'Welcome To Shelter Of Dream',
        "Hi {},\n\nIt our pleasure welcoming you to the shelter of dream please use the Otp given below in order to verify your account.\n\nOTP : {}\n\n\n\nIn case if you are facing any problem please reachout to us on support@sod.com\n\n\nThanks,\nShelter Of Dream\n\n\n".format(user["name"],user["otp"]),
        'donotrely@sod.com',
        [user["email"]],
        fail_silently=False,
    )
    print("EMIAL RESP : :",response)