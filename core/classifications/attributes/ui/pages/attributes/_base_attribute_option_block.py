# core/classifications/attributes/ui/pages/attributes/_base_attribute_option_block.py

from core.ui.schema.block import TableBlock
from core.ui.schema.action import Action
from core.ui.schema.field import Field


def build_attribute_option_block(*, parent_id: str):
    return TableBlock(
        title="Options",
        data_source="/entities/core/attribute.options.list/query/",
        query={
            "parent_id": parent_id,
        },
        columns=[
            Field(key="code", label="Code", type="text"),
            Field(key="name", label="Name", type="text"),
            Field(key="is_active", label="Active", type="boolean"),
        ],
        actions=[
            Action(
                type="navigate",
                label="Edit",
                to=f"/settings/classifications/attributes/{parent_id}/options/{{id}}/edit/?parent_id={parent_id}",
            ),
            Action(
                type="delete",
                label="Delete",
                endpoint=f"/attributes/{parent_id}/options/{{id}}/",
                confirm={
                    "title": "Delete Option",
                    "message": "Are you sure you want to delete this option?",
                    "level": "danger",
                },
            ),
        ],
        top_actions=[
            Action(
                type="navigate",
                label="Create Options",
                to=f"/settings/classifications/attributes/{parent_id}/options/create?parent_id={parent_id}",
                permission="core.attributes.add",
            )
        ],
    )
