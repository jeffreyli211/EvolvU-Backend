from rest_framework import serializers

from coaches.models import Coach

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ['first_name', 'last_name',
                'focus_health',
                'focus_wellness',
                'focus_health_wellness',
                'focus_holistic',
                'focus_life',
                'focus_behavioral',
                'travel']