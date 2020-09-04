from card_maker_app.models.named_model import NamedModel


class BaseSet(NamedModel):
    class Meta:
        db_table = NamedModel._meta.app_label + "_base_set"
