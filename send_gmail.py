# send_gmail.py

"""
https://developers.google.com/gmail/api/quickstart/python
"""

def create_message(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string())}

def send_message(service, user_id, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print(f'Message Id: {message['id']}')
    return message
  except errors.HttpError, error:
    print(f'An error occurred: {error}')

def main():
  sender = 'me@gmail.com'
  to = 'you@gmail.edu'
  subject = 'test email from gmail API'
  message_text = """

  Hello from the Gmail Web API

  best,
  Peter
  """
  user_id = 'my.gmail_id@gmail.com'
  service = 
  m = create_message(sender=sender, to=to, subject=subject, message_text=message_text)
