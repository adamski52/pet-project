import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'storybook.settings'
import sys, django, getopt
django.setup()

from django.conf import settings
import uuid, errno
from PIL import Image
from math import ceil
from datetime import datetime
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string

from api.user.models import UserProfile
from api.invite.models import Invite
from api.dog.models import Dog


def invites():
    pending_invites = Invite.objects.filter(
        processed = False).order_by("recipient_email")

    recipients = pending_invites.values("recipient_email").distinct()

    emails = {}

    for recipient in recipients:
        recipient_email = recipient["recipient_email"]
        invites = pending_invites.filter(
            recipient_email = recipient_email)

        for invite in invites:
            id = str(invite.sender.id)
            emails.setdefault(recipient_email, {})
            emails[recipient_email].setdefault(id, {
                "invite_id": invite.id,
                "sender_first_name": invite.sender.first_name,
                "sender_last_name": invite.sender.last_name,
                "sender_email": invite.sender.email,
                "sender_dogs": []
            })

            emails[recipient_email][id]["sender_dogs"].append(invite.dog.name)


    """
    will now have a data structure like
    {
      "1": {
        "don.johnson@internet.com": {
          "invite_id": "UUID",
          "sender_first_name": "kevin",
          "sender_last_name": "shreve",
          "sender_email": "kevin.shreve@lol.com",
          "sender_dogs": ["xzibit"]
        },
        ...
      }
    }

    where "1" is the unique user ID of the sending user.
    """


            

    # send em off
    for email in emails:
        context = list(emails[email].values())

        if len(context) > 1:
            text_message = render_to_string("templates/invites.txt", context)
            html_message = render_to_string("templates/invites.html", context)
        else:
            original_dogs = context[0]["sender_dogs"]
            sender_dogs = ""
            sender_dogs = sender_dogs.replace(", and ", " and ")

            context[0]["sender_dogs"] = sender_dogs

            text_message = render_to_string("templates/invite.txt", context[0])
            html_message = render_to_string("templates/invite.html", context[0])

    

        send_mail(
            "Storybook Kennels Invite",
            text_message,
            "noreply@jonathanadamski.com",
            [email],
            html_message = html_message)

        print("Email sent to " + email + " with " + str(len(context)) + " invites.")


def crop_image(path, cropped_width, cropped_height):
  # first take smallest of width and height and shrink image to that, in proportion

  img = Image.open(path)
  width, height = img.size

  if width > height:
    ratio = width/height

    #width = cropped_height * ratio
    #height = cropped_height
  else:
    ratio = height/width

    #width = cropped_width
    #height = cropped_width * ratio

  #width = ceil(width)
  #height = ceil(height)

  height = cropped_height
  width = ceil(cropped_height * ratio)
  img = img.resize((width, height))

  #left = ceil((width - cropped_width) / 2)
  #top = ceil((height - cropped_height) / 2)
  #right = ceil((width + cropped_width) / 2)
  #bottom = ceil((height + cropped_height) / 2)

  #return img.crop((left, top, right, bottom))

  return img


def make_dir(new_dir):
    try:
        os.makedirs(new_dir)
    except OSError as exception:
        if exception.errno != errno.EEXIST or not os.path.isdir(new_dir):
            raise


def cleanup_collage_junk():
  make_dir(settings.COLLAGE_PENDING_DIRECTORY)
  make_dir(settings.COLLAGE_JUNK_DIRECTORY)

  os.chdir(settings.COLLAGE_JUNK_DIRECTORY)

  for i in os.listdir(os.getcwd()):
      pending_filepath = settings.COLLAGE_JUNK_DIRECTORY + i

      if os.path.isfile(pending_filepath):
          os.remove(pending_filepath)



def collages():
  filename = ""
  make_dir(settings.COLLAGE_PENDING_DIRECTORY)
  make_dir(settings.COLLAGE_JUNK_DIRECTORY)
  make_dir(settings.COLLAGE_THUMBNAIL_DIRECTORY)
  make_dir(settings.COLLAGE_FULL_DIRECTORY)
  os.chdir(settings.COLLAGE_PENDING_DIRECTORY)

  for pending_filename in os.listdir(os.getcwd()):
      pending_filepath = settings.COLLAGE_PENDING_DIRECTORY + pending_filename
      file_extension = pending_filename.split(".")[-1]
      destination_filename = str(uuid.uuid4()) + "." + file_extension
      #destination_filename = pending_filename

      if pending_filename.endswith(".jpg") or pending_filename.endswith(".jpeg") or pending_filename.endswith(".png"): 
          try:
            cropped_image = crop_image(pending_filepath, settings.COLLAGE_CROPPED_WIDTH, settings.COLLAGE_CROPPED_HEIGHT)
            cropped_image.save(settings.COLLAGE_THUMBNAIL_DIRECTORY + destination_filename)
          except SystemError:
            os.rename(pending_filepath, settings.COLLAGE_JUNK_DIRECTORY + pending_filename)
            continue

          os.rename(pending_filepath, settings.COLLAGE_FULL_DIRECTORY + destination_filename)
      elif os.path.isfile(pending_filepath):
          print("ignoring bullshit file " + pending_filename)
          os.rename(pending_filepath, settings.COLLAGE_JUNK_DIRECTORY + pending_filename)



def main(argv):
    print("argv: " + str(argv))
    if "invites" in argv:
        invites()

    if "collages" in argv:
        collages()

    if "cleanup" in argv:
        cleanup_collage_junk()

if __name__ == "__main__":
    main(sys.argv[1:])


