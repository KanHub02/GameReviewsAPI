from django.db import models


class GameQuerySet(models.QuerySet):
    def tag_indie(self):
        return self.filter(tag__name="indie")

    def tag_horror(self):
        return self.filter(tag__name="horror")

    def tag_mmo(self):
        return self.filter(tag__name="mmo")

    def tag_mmorpg(self):
        return self.filter(tag__name="mmorpg")

    def tag_mmofps(self):
        return self.filter(tag__name="mmofps")

    def tag_adventure(self):
        return self.filter(tag__name="adventure")
    
    def tag_moba(self):
        return self.filter(tag__name="moba")


class GameManager(models.Manager):
    def get_queryset(self):
        return GameQuerySet(self.model)

    def tag_horror(self):
        return get_queryset().tag_horror()

    def tag_mmo(self):
        return get_queryset().tag_mmo()

    def tag_mmorpg(self):
        return get_queryset().tag_mmorpg()

    def tag_mmofps(self):
        return get_queryset().tag_mmofps()

    def tag_adventure(self):
        return get_queryset().tag_adventure()

    def tag_moba(self):
        return get_querysey().tag_moba()