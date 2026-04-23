# business/partners/ui/pages/partner_my_profile_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock, FileBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

from business.enum.permissions import BusinessPermission

UI_PAGES = Page(
    key="partners.my_profile.edit",
    entity="partners",
    domain="business",
    title="Edit My Partner Profile",
    path="/partner/my-profile/edit",
    permissions=[BusinessPermission.PARTNERS_PORTAL_UPDATE],
    data_source="/entities/business/partners.me/query/",
    method="POST",
    blocks=[
        FormBlock(
            title="Update Profile",
            description="Lengkapi dan perbarui informasi profil partner",
            mode="edit",
            submit_to="/entities/business/partners.me.update/execute/",
            method="POST",
            redirect_to={
                "page": "/partner/profile"
            },
            refresh_cache=[
                "partner_portal.my_profile",
                "partners.my_profile.edit"
            ],
            fields=[
                Field(
                    key="name",
                    label="Full Name",
                    type="text",
                    required=True,
                ),
                Field(
                    key="email",
                    label="Email",
                    type="email",
                ),
                Field(
                    key="phone",
                    label="Phone Number",
                    type="text",
                ),
                Field(
                    key="address",
                    label="Address",
                    type="textarea",
                ),

                Field(
                    key="country_id",
                    label="Country",
                    type="select",
                    data_source="/entities/core/countries.select.list/query/",                    
                ),

                Field(
                    key="region_id",
                    label="Province",
                    type="select",
                    data_source="/entities/core/regions.select.list/query/",
                    params={
                        "country_id": "{{country_id}}"
                    }
                ),

                Field(
                    key="city_id",
                    label="City",
                    type="select",
                    data_source="/entities/core/cities.select.list/query/",
                    params={
                        "region_id": "{{region_id}}"
                    }
                ),

                Field(
                    key="specialization",
                    label="Specialization",
                    type="text",
                ),
                Field(
                    key="bio",
                    label="Biography",
                    type="textarea",
                ),

                Field(
                    key="working_hours.start",
                    label="Jam Mulai",
                    type="number",
                ),
                Field(
                    key="working_hours.end",
                    label="Jam Selesai",
                    type="number",
                ),
            ],
            actions=[
                Action(
                    type="submit",
                    label="Save Changes",
                    icon="save",
                ),
                Action(
                    type="redirect",
                    label="Cancel",
                    to="/partner/my-profile",
                ),
            ],
        ),

        FileBlock(
            title="Profile Photos",
            entity_type="partner_image",
            entity_id_from="id",
            multiple=True,
            accept="image/*",
            permissions=[BusinessPermission.PARTNERS_PORTAL_UPDATE],
        ),
    ],
)

register_ui_module_pages("business", UI_PAGES)