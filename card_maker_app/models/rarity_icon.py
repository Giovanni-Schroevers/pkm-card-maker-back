from card_maker_app.models.named_model import NamedModel


class RarityIcon(NamedModel):
    class Meta:
        db_table = NamedModel._meta.app_label + "_rarity_icon"
