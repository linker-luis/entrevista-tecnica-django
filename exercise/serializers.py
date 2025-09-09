from rest_framework import serializers
from .models import Exercise, Routine

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["id", "name", "description"]


class RoutineSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)
    exercise_ids = serializers.PrimaryKeyRelatedField(
        queryset=Exercise.objects.all(),
        many=True,
        write_only=True
    )

    class Meta:
        model = Routine
        fields = [
            "id",
            "user",
            "name",
            "exercises",
            "exercise_ids",
            "weekday",
            "time",
            "created_at",
            "updated_at"
        ]
        read_only_fields = ["user"]

    def create(self, validated_data):
        exercise_ids = validated_data.pop("exercise_ids", [])
        routine = Routine.objects.create(**validated_data)
        routine.exercises.set(exercise_ids)
        return routine

    def update(self, instance, validated_data):
        exercise_ids = validated_data.pop("exercise_ids", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if exercise_ids is not None:
            instance.exercises.set(exercise_ids)
        return instance
