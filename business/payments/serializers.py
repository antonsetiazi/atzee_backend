from rest_framework import serializers
from business.payments.models import Payment
from business.payments import services


class PaymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "direction",
            "amount",
            "currency",
            "method",
            "payment_date",
            "status",
        ]


class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class PaymentCreateSerializer(serializers.Serializer):
    direction = serializers.ChoiceField(choices=Payment.DIRECTION_CHOICES)
    amount = serializers.DecimalField(max_digits=18, decimal_places=2)
    currency = serializers.CharField(required=False)
    method = serializers.CharField(max_length=50)
    payment_date = serializers.DateField()
    reference_number = serializers.CharField(required=False, allow_blank=True)
    document_id = serializers.IntegerField(required=False)
    notes = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        request = self.context["request"]

        return services.create_payment(
            tenant=request.tenant,
            created_by=request.user,
            **validated_data
        )