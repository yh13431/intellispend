from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import json
from .models import Goal
from .serializers import GoalSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_goal(request):
    data = json.loads(request.body)
    data['user'] = request.user.id
    serializer = GoalSerializer(data=data, context={'request': request})

    if serializer.is_valid():
        serializer.save(user=request.user)
        return JsonResponse({'goal': serializer.data}, status=201)

    return JsonResponse({'error': 'Goal could not be created'}, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_goals(request):
    goals = Goal.objects.filter(user=request.user)
    serializer = GoalSerializer(goals, many=True, context={'request': request})
    return JsonResponse({'goals': serializer.data}, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_goal(request, goalId):
    try:
        goal = Goal.objects.get(pk=goalId, user=request.user)
    except Goal.DoesNotExist:
        return JsonResponse({'error': 'Goal not found'}, status=404)

    serializer = GoalSerializer(goal, context={'request': request})
    return JsonResponse({'goal': serializer.data})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_goal(request, goalId):
    try:
        goal = Goal.objects.get(pk=goalId, user=request.user)
    except Goal.DoesNotExist:
        return JsonResponse({'error': 'Goal not found'}, status=404)

    data = json.loads(request.body)
    serializer = GoalSerializer(
        goal,
        data=data,
        partial=True,
        context={'request': request}
    )

    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'goal': serializer.data})

    return JsonResponse({'error': serializer.errors}, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_goal(request, goalId):
    try:
        goal = Goal.objects.get(pk=goalId, user=request.user)
    except Goal.DoesNotExist:
        return JsonResponse({'error': 'Goal not found'}, status=404)

    goal.delete()
    return JsonResponse({'message': 'Goal deleted successfully'}, status=204)