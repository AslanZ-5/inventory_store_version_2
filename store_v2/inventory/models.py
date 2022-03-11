from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    """
    Inventory Category table implimented with MPTT
    """

    name = models.CharField(
        max_length=100,
        verbose_name=_("category name"),
        help_text=_("format: required, max_length=100"),
    )
    slug = models.SlugField(
        max_length=150,
        verbose_name=_("category safe URL"),
        help_text=_(
            "format: required letters, numbers, underscore, or hyphens"
        ),
    )
    is_active = models.BooleanField(default=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="children",
        verbose_name=_("parent of category"),
        help_text=_("format: not required"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("product category")
        verbose_name_plural = _("product categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product details table
    """

    web_id = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=_("product website ID"),
        help_text=_("format: reqired, unique"),
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name=_("product sage URL"),
        help_text=_(
            "format: required, letters numbers, underscores or hyphens"
        )
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("product name"),
        help_text=_("format: required, max-255"),
    )
    description = models.TextField(
        verbose_name=_("product description"),
        help_text=_("format: required")
    )
    category = TreeManyToManyField(Category)
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("product visibility"),
        help_text=_("format: true:product visible")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_('date product created'),
        help_text=_("format: Y-m-d H:M:S")
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_('date product created'),
        help_text=_("format: Y-m-d H:M:S")
    )
    
    def __str__(self):
        return self.name 
        