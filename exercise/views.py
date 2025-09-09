from rest_framework import generics, permissions
from .models import Exercise, Routine
from .serializers import ExerciseSerializer, RoutineSerializer


class ExerciseListCreateView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]



class RoutineListCreateView(generics.ListCreateAPIView):
    serializer_class = RoutineSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Routine.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RoutineDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoutineSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Routine.objects.filter(user=self.request.user)


# ========== Esto deberia de estar protegido y verlo solo los admin pero para facilidad se dejo libre ===========
class UserRoutinesView(generics.ListAPIView):
    serializer_class = RoutineSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Routine.objects.filter(user_id=user_id)