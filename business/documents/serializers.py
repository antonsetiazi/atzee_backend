from rest_framework import serializers

from business.documents.models import Document, DocumentType
from business.documents import services


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model= DocumentType
        fields = [
            "id",
            "code",
            "name",
            "description",
        ]


class DocumentListSerializer(serializers.ModelSerializer):
    document_type_code = serializers.CharField(
        source="document_type.code",
        read_only=True
    )

    document_type_name = serializers.CharField(
        source="document_type.name",
        read_only=True
    )
    
    class Meta:
        model = Document
        fields = [
            "id",
            "number",
            "document_type_code",
            "document_type_name",
            "status",
            "issue_date",
            "reference",
        ]


class DocumentDetailSerializer(serializers.ModelSerializer):
    document_type = DocumentTypeSerializer(read_only=True)

    class Meta:
        model = Document
        fields = [
            "id",
            "number",
            "status",
            "issue_date",
            "reference",
            "notes",
            "source_type",
            "source_id",
            "document_type",
            "created_at",
            "updated_at",
        ]


class DocumentCreateSerializer(serializers.Serializer):
    document_type_code = serializers.CharField(max_length=50)
    issue_date = serializers.DateField()
    reference = serializers.CharField(required=False, allow_blank=True)
    notes = serializers.CharField(required=False, allow_blank=True)
    source_type = serializers.CharField(required=False, allow_blank=True)
    source_id = serializers.CharField(required=False)

    def create(self, validated_data):
        request = self.context["request"]

        return services.create_document(
            tenant=request.tenant,
            created_by=request.user,
            **validated_data
        )
    

class DocumentIssueSerializer(serializers.Serializer):
    """
    Issue document (assign number & lock)
    """

    def save(self, **kwargs):
        request = self.context["request"]
        document: Document = self.context["document"]

        return services.issue_document(
            tenant=request.tenant,
            document_id=document.id,
            issued_by=request.user
        )
    

class DocumentVoidSerializer(serializers.Serializer):
    """
    Void issued document.
    """

    def save(self, **kwargs):
        request = self.context["request"]
        document: Document = self.context["document"]

        return services.void_document(
            tenant=request.tenant,
            document_id=document.id,
            voided_by=request.user
        )