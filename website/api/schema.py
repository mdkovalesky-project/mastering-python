from website.ext import ma
from website.models import Note

class NoteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Note
        include_fk = True

note_schemas = NoteSchema(many=True)
note_schema = NoteSchema()

