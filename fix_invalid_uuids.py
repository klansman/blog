import uuid
from blog.models import Reply

def fix_invalid_uuids():
    for reply in Reply.objects.all():
        try:
            # Check if the UUID is valid
            uuid.UUID(str(reply.id))
        except ValueError:
            # Replace with a new valid UUID
            print(f"Fixing invalid UUID for reply with body: {reply.body}")
            reply.id = uuid.uuid4()
            reply.save()

if __name__ == "__main__":
    fix_invalid_uuids()
    print("UUID validation and fixes completed.")
