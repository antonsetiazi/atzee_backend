from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from business.documents import selectors
from business.documents.models import Document
from business.documents.serializers import (
    DocumentListSerializer,
    DocumentDetailSerializer,
    DocumentCreateSerializer,
    DocumentIssueSerializer,
    DocumentVoidSerializer,
    DocumentTypeSerializer
)


class DocumentViewSet(viewsets.ViewSet):
    """
    Business documents API (tenant scoped).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        documents = selectors.get_documents(
            tenant=request.tenant
        )

        serializer = DocumentListSerializer(documents, many=True)
        return Response(serializer.data)
    

    def retrieve(self, request, pk=None):
        document = selectors.get_document_by_id(
            tenant=request.tenant,
            document_id=pk
        )

        if not document:
            return Response(
                {"detail": "Document not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = DocumentDetailSerializer(document)
        return Response(serializer.data)
    

    def create(self, request):
        serializer = DocumentCreateSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        document = serializer.save()

        output = DocumentDetailSerializer(document)
        return Response(
            output.data,
            status=status.HTTP_201_CREATED
        )
    

    def issue(self, request, pk=None):
        document = selectors.get_document_by_id(
            tenant=request.tenant,
            document_id=pk
        )

        if not document:
            return Response(
                {"detail": "Document not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = DocumentIssueSerializer(
            context={
                "request": request,
                "document": document
            }
        )

        document = serializer.save()

        output = DocumentDetailSerializer(document)
        return Response(output.data)
    

    def void(self, request, pk=None):
        document = selectors.get_document_by_id(
            tenant=request.tenant,
            document_id=pk
        )

        if not document:
            return Response(
                {"detail": "Document not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DocumentVoidSerializer(
            context={
                "request": request,
                "document": document
            }
        )

        document = serializer.save()

        output = DocumentDetailSerializer(document)
        return Response(output.data)
    

class DocumentTypeViewSet(viewsets.ViewSet):
    """
    Read-only document types (tenant scoped).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        types = selectors.get_document_types(
            tenant=request.tenant
        )

        serializer = DocumentTypeSerializer(types, many=True)
        return Response(serializer.data)
