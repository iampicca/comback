from rest_framework import serializers
from . import models


class StaffProfileSerializer(serializers.ModelSerializer):
    """A serializer for our staff user profile objects."""

    class Meta:
        model = models.StaffProfile
        fields = ('id','email', 'password', 'business_id', 'first_name', 'last_name', 'gender')
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        """Create and return a new staff user."""

        user = models.StaffProfile(email=validated_data['email'], business_id=validated_data['business_id'], first_name=validated_data['first_name'], last_name=validated_data['last_name'], gender=validated_data['gender'],is_staff=True, )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def retrieve(self, request, pk='id'):
        pass

    def update(self, request, pk='id'):
        pass

    def partial_update(self, request, pk='id'):
        pass

    def destroy(self, request, pk='id'):
        pass

    def list(self, request):
        pass

class AdminBusProfileSerializer(serializers.ModelSerializer):
    """A serializer for our Comback Admin user profile objects."""

    class Meta:
        model = models.AdminBusProfile
        fields = ('id','email','business_id','password', 'business_id', 'first_name', 'last_name', 'gender')
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        """Create and return a new admins user."""
        user = models.AdminBusProfile(email=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name'], gender=validated_data['gender'], is_admin=True)
        user.set_password(validated_data['password'])
        user.save()

        return user

    def retrieve(self, request, pk='id'):
        pass

    def update(self, request, pk='id'):
        pass

    def partial_update(self, request, pk='id'):
        pass

    def destroy(self, request, pk='id'):
        pass

    def list(self, request):
        pass

class AdminProfileSerializer(serializers.ModelSerializer):
    """A serializer for ourComback Admin user profile objects."""

    class Meta:
        model = models.AdminProfile
        fields = ('id','email', 'password', 'first_name', 'last_name', 'gender')
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        """Create and return a new comback admins user."""

        user = models.AdminProfile(email=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name'], gender=validated_data['gender'], is_admin=True,is_superuser=True,is_staff=True,is_customer=True)
        user.set_password(validated_data['password'])
        user.save()

        return user

    def retrieve(self, request, pk='id'):
        pass

    def update(self, request, pk='id'):
        pass

    def partial_update(self, request, pk='id'):
        pass

    def destroy(self, request, pk='id'):
        pass

    def list(self, request):
        pass

class CustomerProfileSerializer(serializers.ModelSerializer):
    """A serializer for our customer user profile objects."""

    class Meta:
        model = models.CustomerProfile
        fields = ('id','email', 'password', 'first_name', 'last_name', 'gender')
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        """Create and return a new customer user."""

        user = models.CustomerProfile(email=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name'], gender=validated_data['gender'], is_customer=True)
        user.set_password(validated_data['password'])
        user.save()

        return user

    def retrieve(self, request, pk='id'):
        pass

    def update(self, request, pk='id'):
        pass

    def partial_update(self, request, pk='id'):
        pass

    def destroy(self, request, pk='id'):
        pass

    def list(self, request):
        pass

class BusinessSerializer(serializers.ModelSerializer):
    """A serializer for our business objects."""

    class Meta:
        model = models.Business
        fields = ('id','name', 'linked_to')

        def create(self, validated_data):
            """Create and return a new business."""

            business = models.Business(name=validated_data['name'],linked_to=validated_data['linked_to'])
            business.save()

            return business

        def retrieve(self, request, pk='id'):
            pass

        def update(self, request, pk='id'):
            pass

        def partial_update(self, request, pk='id'):
            pass

        def destroy(self, request, pk='id'):
            pass

        def list(self, request):
            pass

class FeedbackSerializer(serializers.ModelSerializer):
    """A serializer for our feedback objects."""

    class Meta:
        model = models.Feedback
        fields = ('id','answer','rating','made_by', 'made_to', 'date_made', 'anonymous')

        def create(self, validated_data):
            """Create and return a new feedback."""

            feedback = models.Feedback(answer=validated_data['answer'],rating=validated_data['rating'],made_by=validated_data['made_by'], made_to=validated_data['made_to'], date_made=validated_data['date_made'], anonymous=validated_data['anonymous'])
            feedback.save()

            return feedback

        def retrieve(self, request, pk='id'):
            pass

        def update(self, request, pk='id'):
            pass

        def partial_update(self, request, pk='id'):
            pass

        def destroy(self, request, pk='id'):
            """delete a feedback"""

            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
            pass

        def list(self, request):
            pass

        def perform_destroy(self, instance):
            instance.delete()

class ComplainSerializer(serializers.ModelSerializer):
    """A serializer for our complain objects."""

    class Meta:
        model = models.Complain
        fields = ('id','message', 'made_by', 'made_to', 'linked_to', 'type', 'date_made', 'anonymous')

        def create(self, validated_data):
            """Create and return a new complain."""

            complain = models.Complain(message=validated_data['message'], made_by=validate_data['made_by'], made_to=validated_data['made_to'], linked_to=validated_data['linked_to'], type=validated_data['type'], date_made=validated_data['date_made'], anonymous=['anonymous'])
            complain.save()

            return complain

        def retrieve(self, request, pk='id'):
            pass

        def update(self, request, pk='id'):
            pass

        def partial_update(self, request, pk='id'):
            pass

        def destroy(self, request, pk='id'):
            """delete a complain"""

            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

        def list(self, request):
            pass

        def perform_destroy(self, instance):
            instance.delete()

class AnalyzeComplainSerializer(serializers.Serializer):
    """A serializer for analyzing our complain objects."""

    class Meta:
        model = models.Complain
        fields = ('made_to', 'made_by', 'message')
h
        def create(self, validated_data):
            self.create(request)
            count = 0
            ranking = {}
            complaints = [Complain.message for complain in Complain.objects.all.filter(made_to=validated_data['made_to'])]
            for item in complaints:
                my_id = complaints[0]
                sentence = complaints.split(" ")
                for word in sentence:
                    if word == validated_data['message']:
                        count+=1
                rank = (count/len(message))*100
                ranking[my_id]=ranking

            max = 60
            for key,value in ranking:
                if value > max:
                    max = key
                else:
                    max is NULL
            return Response({'linked_to':max})

        def retrieve(self, request, pk='id'):
            pass

        def update(self, request, pk='id'):
            pass

        def partial_update(self, request, pk='id'):
            pass

        def destroy(self, request, pk='id'):
            """delete a complain"""

            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

        def list(self, request):
            pass

        def perform_destroy(self, instance):
            instance.delete()
