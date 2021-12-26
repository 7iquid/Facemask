from rest_framework.response import Response
from .models import McDailyRecordingArea
from datetime import datetime

def getByDate(request):
    #format YY MM DD
    date = datetime(request.GET.get('getByDate'))
    # pk =McDailyRecordingArea.objects.get(date = request.GET.get('getByDate'))
    
    return Response(data=pk)


# def getNoteDetail(request, pk):
#     notes = Note.objects.get(id=pk)
#     serializer = NoteSerializer(notes, many=False)
#     return Response(serializer.data)


# def createNote(request):
#     data = request.data
#     note = Note.objects.create(
#         body=data['body']
#     )
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)

# def updateNote(request, pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note, data=data)

#     if serializer.is_valid():
#         serializer.save()

#     return serializer.data


# def deleteNote(request, pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#     return Response('Note was deleted!')
